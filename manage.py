#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import os
import sys

from flask.ext.script import Manager, Server
from flask.ext.script.commands import Command, ShowUrls, Clean

from tenki import create_app

def test(integration="-k-integration", web="-k-web"):
    test_args = ['--strict', '--verbose', '--tb=long', 'tests', integration, web]
    import pytest
    errno = pytest.main(test_args)
    sys.exit(errno)

class Test(Command):
    def run(self):
        self.test_suite = True
        test()

class Integration(Command):
    def run(self):
        self.test_suite = True
        test(integration="-kintegration")

class WebTests(Command):
    def run(self):
        self.test_suite = True
        test(web="-kweb")

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('TENKI_ENV', 'dev')
app = create_app('tenki.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server)
manager.add_command("show-urls", ShowUrls)
manager.add_command("clean", Clean)
manager.add_command("test", Test)
manager.add_command("integration", Integration)
manager.add_command("webtest", WebTests)


if __name__ == "__main__":
    manager.run()

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


class Test(Command):
    "Run tests"
    def run(self):
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('TENKI_ENV', 'dev')
app = create_app('tenki.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("test", Test())


if __name__ == "__main__":
    manager.run()

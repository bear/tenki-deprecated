#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean

from tenki import create_app

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('TENKI_ENV', 'dev')
app = create_app('tenki.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


if __name__ == "__main__":
    manager.run()

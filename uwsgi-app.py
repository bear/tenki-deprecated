#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2009-2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import os

from tenki import create_app

env = os.environ.get('TENKI_ENV', 'dev')
application = create_app('tenki.settings.%sConfig' % env.capitalize())

if __name__ == "__main__":
    application.run()

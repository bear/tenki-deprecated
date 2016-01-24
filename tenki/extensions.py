# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension


# Setup flask cache
cache = Cache()

debug_toolbar = DebugToolbarExtension()

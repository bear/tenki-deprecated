# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2017 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import pytest
from tenki import create_app


@pytest.yield_fixture
def app():
    app = create_app('tenki.settings.TestConfig')
    # app.dbRedis = FlaskRedis.from_custom_provider(MockRedisWrapper, app)

    yield app


@pytest.yield_fixture
def app_client(app):
    client = app.test_client()
    yield client

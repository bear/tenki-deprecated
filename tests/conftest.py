# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: MIT, see LICENSE for more details.
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

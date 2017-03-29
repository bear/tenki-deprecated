# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2017 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import json
import pytest


@pytest.mark.usefixtures('app')
def test_weather_clear(app):
    key = '%s%s' % (app.weather.keyRoot, '19021')
    app.weather.db.set(key, json.dumps({"testing": "save"}))

    app.weather.clear('19021')
    value = app.weather.load('19021')
    assert value is None


@pytest.mark.usefixtures('app')
def test_weather_save(app):
    app.weather.clear('19021')
    app.weather.save('19021', {"testing": "save"})

    key = '%s%s' % (app.weather.keyRoot, '19021')
    value = json.loads(app.weather.db.get(key))
    assert len(value.keys()) == 1
    assert value['testing'] == "save"

    app.weather.clear('19021')


@pytest.mark.usefixtures('app')
def test_weather_load_nonexistant(app):
    app.weather.clear('19021')
    value = app.weather.load('19021')
    assert value is None


@pytest.mark.usefixtures('app')
def test_weather_load_existing(app):
    app.weather.save('19021', {"testing": "save"})
    value = app.weather.load('19021')
    assert value['testing'] == 'save'
    app.weather.clear('19021')

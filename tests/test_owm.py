# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

import pytest
from mock import Mock

_result = {u'bear': 'test', u'status': u'Haze', u'visibility_distance': None, u'humidity': 62, u'clouds': 75, u'temperature': {u'temp_kf': None, u'temp_max': 270.15, u'temp': 267.98, u'temp_min': 265.15}, u'dewpoint': None, u'snow': {}, u'detailed_status': u'haze', u'reference_time': 1453626900, u'weather_code': 721, u'humidex': None, u'rain': {}, u'sunset_time': 1453673334, u'pressure': {u'press': 1008, u'sea_level': None}, u'sunrise_time': 1453637695, u'heat_index': None, u'weather_icon_name': u'50n', u'wind': {u'speed': 7.2, u'deg': 330}}

@pytest.mark.integration
@pytest.mark.usefixtures('app')
def testOpenWeatherMap(app):
    app.weather.OpenWeatherMap = Mock(return_value=_result)

    value = app.weather.OpenWeatherMap('19021')

    assert value is not None
    assert value['bear'] == 'test'
    assert len(value.keys()) == 19

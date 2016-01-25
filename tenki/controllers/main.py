# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, render_template, current_app
from flask_restful import reqparse, Resource, Api

from tenki.extensions import cache

main = Blueprint('main', __name__)
api  = Api(main)

zip_parser = reqparse.RequestParser()
zip_parser.add_argument('postalcode', default=None, location="args")

@main.route('/')
@cache.cached(timeout=1000)
def index():
    return render_template('index.jinja')


class CurrentWeather(Resource):
    def get(self):
        args = zip_parser.parse_args()
        postalcode = args.postalcode
        if postalcode is None:
            postalcode = current_app.config['POSTALCODE']
        current_app.logger.info('/weather called %s' % postalcode)

        return current_app.weather.get(postalcode), 200

api.add_resource(CurrentWeather, '/api/v1/weather')

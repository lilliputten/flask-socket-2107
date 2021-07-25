# -*- coding:utf-8 -*-
# @module app
# @since 2020.07.04, 01:43
# @changed 2021.07.25, 18:28

# import pathmagic  # noqa

import os

# sys.path.append('../')

from flask import Flask

from config import config

# from werkzeug.routing import BaseConverter  # For urls transformations (see ListConverter below)


# rootPath = config['rootPath']
clientStaticPath = config['clientStaticPath']
clientTemplatePath = config['clientTemplatePath']

app = Flask(__name__,
            # static_url_path='',
            static_url_path='/flask-static',
            static_folder=clientStaticPath)


@app.template_filter()
def getenv(key):
    return os.getenv(key)


# class ListConverter(BaseConverter):  # Urls transfomations example
#     regex = r'\S+(?:,\d+)*,?'
#
#     def to_python(self, value):
#         return [str(x) for x in value.split(',')]
#
#     def to_url(self, value):
#         return ','.join(str(x) for x in value)
#
#
# app.url_map.converters['list'] = ListConverter

__all__ = [  # Exporting objects...
    'app',
]

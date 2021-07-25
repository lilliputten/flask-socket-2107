# -*- coding:utf-8 -*-
# @module config
# @desc Universal server & client config
# @since 2020.02.23, 02:18
# @changed 2020.10.20, 23:29
# See:
#  - https://docs.python.org/3/library/configparser.html -- ???
#  - https://stackoverflow.com/questions/9590382/forcing-python-json-module-to-work-with-ascii

from os import path
import json
import yaml

rootPath = path.dirname(path.abspath(__file__))  # Project root path

yamlConfigFilename = path.join(rootPath, 'config.yml')
yamlLocalConfigFilename = path.join(rootPath, 'config.local.yml')

buildTagFilename = path.join(rootPath, 'build-tag.txt')
packageFilename = path.join(rootPath, 'package.json')
#  print 'config: packageFilename', packageFilename  # DEBUG

uploadPath = path.join(rootPath, 'uploads')

clientTemplatePath = path.join(rootPath, 'test-build')
# clientStaticPath = path.join(clientTemplatePath, 'static')
clientStaticPath = path.join(rootPath, 'flask-static')

version = 'Testing'
buildTag = 'Testing'

if path.isfile(packageFilename):
    pkgConfigFile = open(packageFilename)
    pkgConfig = json.load(pkgConfigFile)
    version = pkgConfig['version'].encode('ascii')
    pkgConfigFile.close()

if path.isfile(buildTagFilename):
    buildTagFile = open(buildTagFilename, 'rb')
    buildTag = buildTagFile.read()
    buildTagFile.close()

config = {  # Default config

    # Application parameters...

    'version': version,
    'buildTag': buildTag,

    # Path parameters...

    'rootPath': rootPath,
    'uploadPath': uploadPath,

    # Generated client path (see `test-build`)

    'clientStaticPath': clientStaticPath,
    'clientTemplatePath': clientTemplatePath,

    # # Image parameters...
    # #
    # #  - [Camera configuration - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/camera.md)
    # #
    # #  Default dimensions: 2592x1944
    # #  Half size: 1296x972
    # #  Quarter size: 648x486
    #
    # 'imageWidth': 648,
    # 'imageHeight': 486,
    #
    # # Client parameters... (UNUSED)
    #
    # 'localImageFile': 'local-image.jpg',
    # 'remoteUrl': 'https://cam.lilliputten.ru/upload',
    #
    # # Image file paramaters...
    #
    # 'imageExt': '.image',
    # 'imagesIndex': 'index.txt',

    # Logging...

    'outputLog': True,
    'outputColoredLog': True,
    'writeLog': True,
    'clearLogFile': False,

    # Datetime formats...

    'dateTagFormat': '%y%m%d-%H%M',
    'dateTagPreciseFormat': '%y%m%d-%H%M%S',
    'shortDateFormat': '%Y.%m.%d-%H:%M',
    'preciseDateFormat': '%Y.%m.%d-%H:%M:%S',
    'logDateFormat': '%y%m%d-%H%M%S-%f',
    'detailedDateFormat': '%Y.%m.%d-%H:%M:%S.%f',

}


def updateConfigWithYaml(config, file):
    """
    Extend config from file
    """
    if path.isfile(file):
        with open(file) as file:
            #  print 'Extending config with', file
            yamlConfigData = yaml.load(file, Loader=yaml.FullLoader)
            #  print 'yamlConfigData:', yamlConfigData
            config.update(yamlConfigData)


updateConfigWithYaml(config, yamlConfigFilename)
updateConfigWithYaml(config, yamlLocalConfigFilename)

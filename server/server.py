# -*- coding:utf-8 -*-
# @module server
# @since 2021.07.25, 16:43
# @changed 2021.07.25, 16:43

#  import pathmagic  # noqa

#  import os
import traceback

#  from flask import current_app as app
from .app import app

# from flask import redirect
from flask import render_template
# from flask import url_for
# from flask import jsonify
from flask import request

#  from config import config
from .logger import DEBUG

#  Sockets test...
from flask_socketio import SocketIO, emit  # , send

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins='*')

#  DEBUG('Server started', {
#      'FLASK_ENV': os.getenv('FLASK_ENV'),
#      'buildTag': config['buildTag'],
#  })


@app.route('/')
def rootPage():
    """
    Default page
    """
    return render_template('sockets.html')
    #  return redirect('/last')
    #  return listImages.viewLastImage()


# Sockets test 001...


# DEBUG 2021.07.26, 00:42 - Client/server error:
# Client got string: '\x00\x09\x08\xEF\xBF\x220{"pingInterval":25000,"pingTimeout":60000,"upgrades":[],"sid":"27016fffa1b840228db8f4402f1c1faa"} ??42["hello",{"data":"connection - Server Initial Response"}] ??40'
# Encoded: %00%09%08%EF%BF%BD0%7B%22pingInterval%22%3A25000%2C%22pingTimeout%22%3A60000%2C%22upgrades%22%3A%5B%5D%2C%22sid%22%3A%2227016fffa1b840228db8f4402f1c1faa%22%7D%00%05%09%EF%BF%BD42%5B%22hello%22%2C%7B%22data%22%3A%22connection%20-%20Server%20Initial%20Response%22%7D%5D%00%02%EF%BF%BD40
#
# #1 garbage: %00%09%08%EF%BF%BD -- \x00\x09\x08\xEF\xBF\xBD
# #2 digits: 0
# #3 data: {"pingInterval":25000,"pingTimeout":60000,"upgrades":[],"sid":"27016fffa1b840228db8f4402f1c1faa"}
# #3 garbage: %00%05%09%EF%BF%BD -- \x00\x05\x09\xEF\xBF\xBD
# #4 digits: 42
# #5 data: ["hello",{"data":"connection - Server Initial Response"}]
# #6 garbage: %00%02%EF%BF%BD -- \x00\x02\xEF\xBF\xBD
# #7 digits: 40
#
# Packets SEPARATOR: "%1E"
#
# see https://socket.io/docs/v2/internals/index.html

@socketio.on('connect')
def connect():
    foo = request.args.get('foo')
    DEBUG('sockets: connect', {'foo': foo})
    #  emit('hello', 'Test')
    #  emit('hello', {'data': 'connection - Server Initial Response'})
    #  send('OK')


@socketio.on('disconnect')
def test_disconnect():
    DEBUG('sockets: disconnect')
    print('Client disconnected')


@socketio.on('my event')
def test_message(message):
    DEBUG('sockets: my event')
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event')
def test_broadcast_message(message):
    DEBUG('sockets: my broadcast event')
    emit('my response', {'data': message['data']}, broadcast=True)


# Tests...


@app.route('/hello/')
@app.route('/hello/<name>')
def testHello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def testProfile(username):
    return 'User: %s' % username


# Errors processing...

@app.errorhandler(Exception)
def handle_error(e):
    #  errorType, errorValue, errorTraceback = sys.exc_info()
    #  @see https://docs.python.org/2/library/traceback.html
    errorTraceback = traceback.format_exc()
    error = str(e)
    errorRepr = e.__repr__()
    errorData = {
        'error': error,
        'repr': errorRepr,
        'traceback': str(errorTraceback)
    }
    DEBUG('server:Exception', errorData)
    #  return jsonify(errorData), getattr(e, 'code', 500)
    return render_template('error.html', error=error), getattr(e, 'code', 500)


#  socketio.run(app)


if __name__ == '__main__':
    DEBUG('__main__ started')
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()
    #  socketio.run(app)

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
# from flask import request

#  from config import config
from .logger import DEBUG

#  Sockets test...
from flask_socketio import SocketIO, emit
# from flask_sockets import Sockets

# sockets = Sockets(app)
socketio = SocketIO(app)

#  DEBUG('Server started', {
#      'FLASK_ENV': os.getenv('FLASK_ENV'),
#      'buildTag': config['buildTag'],
#  })


@app.route('/')
def testRootPage():
    """
    Default page (last image or all images list)
    """
    return render_template('hello.html', name='Default')
    #  return redirect('/last')
    #  return listImages.listAllImages()
    #  return listImages.viewLastImage()


# # Sockets test 002...
#
#
# @socketio.event
# def my_event(message):
#     emit('my response', {'data': 'got it!'})


# Sockets test 001...


@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event')
def test_broadcast_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


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


if __name__ == '__main__':
    app.secret_key = 'hjAR5HUzijG04RJP3XIqUyy6M4IZhBrQ'
    app.logger.debug('test log')
    # app.debug = True
    app.run()

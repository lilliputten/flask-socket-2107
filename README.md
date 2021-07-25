# Python client/server sockets interchange test


## Build info (auto-generated)

- Version: 0.0.1
- Last changes timestamp: 2021.07.25, 21:15
- Last changes timetag: 210725-2115


## Sockets (Flask-SocketIO)

In case of flask error 'ImportError: cannot import name JSONDecodeError':

> If you really need it for python 2, use a older version.. pip install Flask-SocketIO==4.3.2

```
pip install Flask-SocketIO==4.1.1
pip install -U simplejson
```

In `.venv/Lib/site-packages/engineio/client.py` use #2:

```
from simplejson import JSONDecodeError
```

Or (alternatively) next packets combination can be used:

- Flask-SocketIO==4.3.1
- python-engineio==3.13.2
- python-socketio==4.6.0


## Python 2.7 socket links:

- [Python 2.7 Socket programming ports - Stack Overflow](https://stackoverflow.com/questions/52053884/python-2-7-socket-programming-ports)
- [Socket Programming HOWTO — Python 2.7.6 documentation](https://cpython-test-docs.readthedocs.io/en/latest/howto/sockets.html)
- [python - Using Flask-socketio and the socketIO client - Stack Overflow](https://stackoverflow.com/questions/48160130/using-flask-socketio-and-the-socketio-client)
- [Client Examples (Python 3.5+)](https://python-socketio.readthedocs.io/en/latest/intro.html#client-examples)


## SocketIO:

- [Getting Started — Flask-SocketIO documentation](https://flask-socketio.readthedocs.io/en/latest/getting_started.html#initialization)
- [Socket.io example with jquery and dom manipulation](https://gist.github.com/anandgeorge/2814934)
- [Easy WebSockets with Flask and Gevent - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)


## Server

Demo server runs on python/flask platform.


## Crontab

### Real crontab entry example:

```shell
# # Test entry...
# 30 */1 * * * date >> ~/test_crontab

# Make & upload shots every 15 minutes (with forced logging)...
*/5 * * * * sh /home/pi/cam-client/client-make-and-upload-image.sh >> /home/pi/cam-client/cron-log.txt 2>&1

# Make & upload shots every 20 minutes...
*/20 * * * * sh /home/pi/cam-client/client-make-and-upload-image.sh

# Reboot every 3 hours (00:55, 03:55, etc...)
55 */3 * * * sudo reboot -f
```

### Crontab commands:

Edit crontab:
```shell
crontab -e
```

Show crontab:
```shell
crontab -l
```

See also:

- [Scheduling tasks with Cron - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/cron.md)


### Crontab logging

Uncomment `# cron.*` line in `/etc/rsyslog.conf` (eg. edit with `sudo vim /etc/rsyslog.conf`).

Show crontab log:

```shell
tail -f /var/log/cron.log
```

Or use output reirect in command:

```shell
/home/pi/cam-client/client-make-and-upload-image.sh >> /home/pi/cam-client/cron.log 2>&1
python /home/pi/cam-client/client-make-image.py >>  /home/pi/cam-client/cron.log 2>&1
```


<!--
 @changed 2021.07.25, 21:17
-->

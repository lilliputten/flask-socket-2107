# Cam flask photo receiver server & raspberry camera client


## Build info (auto-generated)

- Version: 0.0.5
- Last changes timestamp: 2021.05.02, 19:16
- Last changes timetag: 210502-1916


## API

Basic api structure (server v.0.0.5+):

- GET `/api/images`: Get all images list.
- GET `/api/images/recent`: Get recent image info.
- GET `/api/images/{id}`: Get specific image info.
- POST `/api/images/add`: Add (upload) new image. (Duplicates `/upload`?)
- DELETE `/api/images`: Delete all images.
- DELETE `/api/images/{id}`: Delete specific image.

See also:

- [JSON:API — Latest Specification (v1.0)](https://jsonapi.org/format/)
- [JSON API – работаем по спецификации / Блог компании Конференции Олега Бунина (Онтико) / Хабр](https://habr.com/ru/company/oleg-bunin/blog/433322/)
- [REST — Википедия](https://ru.wikipedia.org/wiki/REST)

## Sockets (Flask-SocketIO)

> If you really need it for python 2, use a older version.. pip install Flask-SocketIO==4.3.2

```
pip install Flask-SocketIO==4.1.1
pip install -U simplejson
```

In `.venv/Lib/site-packages/engineio/client.py` use #2:

```
from simplejson import JSONDecodeError
```


## Python 2.7 socket links:

- [Python 2.7 Socket programming ports - Stack Overflow](https://stackoverflow.com/questions/52053884/python-2-7-socket-programming-ports)
- [Socket Programming HOWTO — Python 2.7.6 documentation](https://cpython-test-docs.readthedocs.io/en/latest/howto/sockets.html)
- [Client Examples (Python 3.5+)](https://python-socketio.readthedocs.io/en/latest/intro.html#client-examples)

## Server

Images server runs on python/flask platform.

It has 3 interfaces: template-based bootstrap application, api interface (json), react spa application (overt api; in progress).


## Camera interface

Camera shots are taken using the `raspistill` program using commands like:

```shell
# Default:
raspistill -o image.jpg
# Half:
raspistill -w 1296 -h 972 -o image-half.jpg
# Half:
raspistill -w 648 -h 486 -o image-quarter.jpg
```

For commandline reference use `raspistill --help`.

- [Camera configuration - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/camera.md)


## Raspberry camera client

Use `client-make-and-upload-image.sh` script to make & upload image to server.

Use crontab to automate image capture.

### Sample crontab lines:

- Every minute: `* * * * * /home/pi/cam-client/client-make-and-upload-image.sh`
- Every 15th minute: `*/15 * * * * /home/pi/cam-client/client-make-and-upload-image.sh`

## Real crontab entry example:

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


## Crontab logging

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
 @changed 2021.05.02, 21:05
-->

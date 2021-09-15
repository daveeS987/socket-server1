# Python Socket Io Server

## Author: Davee Sok

## Links & Resources

- [Repo to Connected Socket Io Clients](https://github.com/daveeS987/socket-client1)
- [Python Socket Io](https://python-socketio.readthedocs.io/en/latest/server.html)
- [Eventlet/Gunicorn Issues](https://github.com/eventlet/eventlet/issues/702)
- [Miguel Grinberge Youtube](https://www.youtube.com/playlist?list=PLCuWRxjbgFnPZTBMYbz9UNGvTLNggRMjb)

## Overview

A basic python socket IO server

## Tools & Dependencies

- Gunicorn
- Eventlet
- Python Socket IO

## Getting Started

### 1. Enter the following into terminal and hit enter

```iterm
git clone https://github.com/daveeS987/socket-server1.git
cd socket-server1
poetry shell
```

### 2. Once shelled up, install dependencies

```iterm
poetry install
```

### How to run server locally

Run the following command in terminal:

```iterm
gunicorn -k eventlet -w 1 --reload server:app
```

## Deploy To Heroku Notes

- Make sure to have Procfile
- Need requirements.txt
- Add heroku/python buildpack in settings

Heroku cli commands:

- heroku login
- heroku logs --tail --app NAME_OF_APP

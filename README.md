# Python Socket Io Server

## Author: Davee Sok

## Links & Resources

- [Python Socket Io](https://python-socketio.readthedocs.io/en/latest/server.html)
- [Eventlet/Gunicorn Issues](https://github.com/eventlet/eventlet/issues/702)
- [Miguel Grinberge Youtube](https://www.youtube.com/playlist?list=PLCuWRxjbgFnPZTBMYbz9UNGvTLNggRMjb)

## Overview

A socket IO server

## Tools & Dependencies

- Gunicorn
- Eventlet
- Python Socket IO

## Getting Started

- clone repo
- `poetry install`

### How to run server locally

- Run the following command in terminal

```iterm
gunicorn -k eventlet -w 1 --reload server:app
```

## Deploy To Heroku Notes

- Need Procfile
- Need requirements.txt

"""
This script runs the SoniaRizzoDev application using a development server.
"""

from os import environ
from webapp import app

def start(one, two):
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

if __name__ == '__main__':
    start()
from flask import Flask

app = Flask(__name__)

from routes import *
#change to routes again for finale


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5555
    app.debug = True
    app.run(HOST, PORT)

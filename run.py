from app import *


DEBUG = True
PORT = 8080
HOST = '127.0.0.1'

if __name__ == '__main__':
    app = create_app()
    app.run(debug=DEBUG, host = HOST, port = PORT)
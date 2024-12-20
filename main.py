import os

from app import app

if __name__ == '__main__':
    app.run(
        host= os.getenv("DB_API_IP", 'localhost'),
        port= int(os.getenv("DB_API_PORT", '5000')),
        debug=app.config['DEBUG']
    )
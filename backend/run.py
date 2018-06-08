from backend.app import create_app
from backend.db import db
from flask_migrate import Migrate

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

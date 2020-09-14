from app.main import create_apps ,db
from flask_migrate import Migrate, migrate
from app.main.models import *
#inititalizing the server app
app = create_apps()

migrate = Migrate(app, db)

if __name__ == 'main':
    app.run()
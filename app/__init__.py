# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # Importez les routes et les modèles à l'intérieur des fonctions qui en ont besoin
# def create_app():
#     from app import routes, models
#     return app

# Dans app/__init__.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import tasks_bp  # Importez le blueprint depuis le module views

def create_app():
    from app import views, models
    return app

app.register_blueprint(tasks_bp)  # Enregistrez le blueprint dans votre application Flask



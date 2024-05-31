from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    swagger = Swagger(app)

    with app.app_context():
        from .web_routes import web as web_blueprint
        from .api_routes import api as api_blueprint
        app.register_blueprint(web_blueprint)
        app.register_blueprint(api_blueprint, url_prefix='/api')
        db.create_all()

    return app

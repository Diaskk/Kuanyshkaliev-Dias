from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jeofejafoiaejfoihjof'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/full"

    db.init_app(app)


    from .routes import routes
    from .auth import auth
    from .recipe import recipe
    from .custom import custom

    app.register_blueprint(recipe, url_prefix='/')
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(custom, url_prefix='/')

    from .models import User, Food

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


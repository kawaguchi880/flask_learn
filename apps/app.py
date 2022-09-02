from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIOINS = False,
        SECRET_KEY="ABCDEFG"
    )

    csrf.init_app(app)
    db.init_app(app)
    Migrate(app,db)
    from apps.sampleSite import views
    app.register_blueprint(views.sampleSite,url_prefix="/")
    return app

from flask import Flask
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="ABCDEFG"
    )

    csrf.init_app(app)
    from apps.sampleSite import views
    app.register_blueprint(views.sampleSite,url_prefix="/")
    return app

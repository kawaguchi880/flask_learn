from flask import Flask

def create_app():
    app = Flask(__name__)
    from apps.sampleSite import views
    app.register_blueprint(views.sampleSite,url_prefix="/")
    return app
from wtforms import StringField
from flask_wtf import FlaskForm



class KweetForm(FlaskForm):
    message = StringField()
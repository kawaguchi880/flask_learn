from wtforms import StringField,IntegerField,DateTimeLocalField
from flask_wtf import FlaskForm



class KweetForm(FlaskForm):
    message = StringField()


class jankennForm(FlaskForm):
    choice = StringField()

class taipinnguForm(FlaskForm):
    taipunngu = StringField()
    score = IntegerField()
    prequestion = StringField()

class ReserveForm(FlaskForm):
    name = StringField()
    startAt = DateTimeLocalField(format='%Y-%m-%dT%H:%M')
    endAt = DateTimeLocalField(format='%Y-%m-%dT%H:%M')
    count = IntegerField()

class KakeiboForm(FlaskForm):
    date = DateTimeLocalField(format='%Y-%m')
    budget = StringField()
    item = StringField()
    cost = IntegerField()

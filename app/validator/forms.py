from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

from app.libs.enums import ClientTypeEnums


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), len(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnums(value.data)
        except ValueError as e:
            raise e
        pass
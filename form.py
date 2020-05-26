from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import InputRequired


class makeCrossword(FlaskForm):
    words = TextAreaField(render_kw={
        "placeholder": "Words, seperated by spaces"})

    structure = SelectField(choices=[(0, "Structure 0"), (1, "Structure 1"), (
        2, "Structure 2"), (3, "Structure 3")], validate_choice=False)

    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import InputRequired


class makeCrossword(FlaskForm):
    words = TextAreaField(render_kw={
        "placeholder": "Words, separated by spaces"})

    structure = SelectField(choices=[
        (0, "Structure 0"), (1, "Structure 1"), (2, "Structure 2"), (3, "Structure 3"),
        (4, "Structure 4 (Complex)"), (5, "Structure 5 (Complex)"),
        (6, "Structure 6 (Complex)"), (7, "Structure 7 (Complex)")
    ], validate_choice=False)

    submit = SubmitField('Submit')

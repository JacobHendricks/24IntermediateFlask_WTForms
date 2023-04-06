from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class PetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Name",
        validators=[InputRequired(message="Name cannot be blank")])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)])

    notes = StringField(
        "Notes",
        validators=[Optional(), Length(min=10)])


# choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')]


class EditPetForm(FlaskForm):
    """Form for editing an existing pet"""

    name = StringField("Name", validators=[
                       InputRequired(message="Name cannot be blank")])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age")

    notes = StringField("Notes", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")

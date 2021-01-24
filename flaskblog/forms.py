from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired
# from flask_login import current_user
# from flaskblog.models import User


class QuestionnaireForm(FlaskForm):
    genders = RadioField(
        choices=[('M', 'Męski'), ('F', 'Damski'), ('U', 'Unisex')])
    groups = RadioField(choices=[('1', 'Przyprawowej'),
                                 ('2', 'Kwiatowej'), ('3',
                                                      'Drzewnej'), ('4', 'Deserowej'),
                                 ('5', 'Ziołowej'), ('6',
                                                     'Animalnej'), ('7', 'Orientalnej'),
                                 ('8', 'Owocowej'), ('9', 'Cytrusowej'), ('10', 'Morskiej')])
    scents = RadioField(choices=[('1', 'Świeży'),
                                 ('2', 'Słodki'), ('3', 'Ciepły'), ('4', 'Gorzki'),
                                 ('5', 'Wytrawny'), ('6', 'Zimny')])
    submit = SubmitField('Submit')


class AddToFavourites(FlaskForm):
    perfume = SelectField('Perfume', validators=[DataRequired()], coerce=str)
    submit = SubmitField('Submit')

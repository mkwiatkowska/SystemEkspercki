from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired


class QuestionnaireForm(FlaskForm):
    genders = RadioField(
        choices=[('M', 'Męski'), ('F', 'Damski'), ('U', 'Unisex')])
    ages = RadioField(
        choices=[('A', '12-17'), ('B', '18-25'), ('C', '26-39'),('D', '40-65'), ('E', '65+') ])
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

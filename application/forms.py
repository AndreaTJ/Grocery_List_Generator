from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NewDish(FlaskForm): 
    name_dish = StringField("Name of the dish", validators=[DataRequired(), Length(min=3, message="Please, introduce at least 3 characters")])
    ingredient1 = StringField ("Ingredient 1", validators=[DataRequired(), Length(min=3, message="Please, introduce at least 3 characters")])
    ingredient2 = StringField ("Ingredient 2")
    ingredient3 = StringField ("Ingredient 3")
    ingredient4 = StringField ("Ingredient 4")
    ingredient5 = StringField ("Ingredient 5")
    submit = SubmitField('Add')

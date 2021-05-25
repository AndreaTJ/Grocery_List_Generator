from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

Measure = ["kg", "gr", "mg", "tsp (teaspoon)", "tbl (tablespoon)","cup", "pint", "ml", "l"]

class NewDish(FlaskForm): 
    name_dish = StringField("Name of the dish", validators=[DataRequired(), Length(min=3, message="Please, introduce at least 3 characters")])
    ingredient1 = StringField ("Ingredient 1", validators=[DataRequired(), Length(min=3, message="Please, introduce at least 3 characters")])
    ingredient2 = StringField ("Ingredient 2", validators=[DataRequired(), Length(min=3, message="Please, introduce at least 3 characters")])
    qty1 = StringField ("qty", validators=[DataRequired()])
    qty2 = StringField ("qty", validators=[DataRequired()])
    measure1=SelectField (label ="measure1", choices=[(measure, measure) for measure in Measure])
    measure2=SelectField (label ="measure2", choices=[(measure, measure) for measure in Measure])

    submit = SubmitField('Add')

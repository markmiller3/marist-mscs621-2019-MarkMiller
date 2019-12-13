from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, FloatField, StringField
from wtforms.validators import InputRequired


# This defines the class form for the initial pounds
class PoundForm(FlaskForm):
    total_pounds = FloatField("Enter the number of pounds you have: ", [InputRequired()])
    submit = SubmitField('Submit')


# This provides the class form for the First Item
class ItemOneForm(FlaskForm):
    item1_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


# This provides the class form for the Second Item
class ItemTwoForm(FlaskForm):
    item2_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


# This provides the class form for the third item
class ItemThreeForm(FlaskForm):
    item3_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


class ItemFourForm(FlaskForm):
    item4_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


class ItemFiveForm(FlaskForm):
    item5_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


class ItemSixForm(FlaskForm):
    item6_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


class ItemSevenForm(FlaskForm):
    item7_pounds = FloatField("Enter how many pounds you would like to buy:  ", [InputRequired()])
    submit = SubmitField('Add to cart')


class OrderReview(FlaskForm):
    item_delete = StringField("If you would like to delete an item please type in the order name.")
    submit = SubmitField('Continue')


class OrderSummary(FlaskForm):
    submit = SubmitField('Reset Meat Order')

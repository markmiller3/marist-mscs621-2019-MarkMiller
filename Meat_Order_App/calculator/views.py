from flask import Blueprint, render_template, redirect, url_for, session, flash
from Meat_Order_App.calculator.forms import PoundForm, ItemOneForm, ItemTwoForm, ItemThreeForm, ItemFourForm, \
                                            ItemFiveForm, ItemSixForm, ItemSevenForm, OrderReview, OrderSummary
from Meat_Order_App.calculator.api_call import *

# These link the blueprints from this python file to the __init__ file
# That allow the flask_app.py to call the routes
pounds_blueprint = Blueprint('total_pounds', __name__, template_folder='templates/calculator')
item1_info_blueprint = Blueprint('item1_pounds', __name__, template_folder='templates/calculator')
item2_info_blueprint = Blueprint('item2_pounds', __name__, template_folder='templates/calculator')
item3_info_blueprint = Blueprint('item3_pounds', __name__, template_folder='templates/calculator')
item4_info_blueprint = Blueprint('item4_pounds', __name__, template_folder='templates/calculator')
item5_info_blueprint = Blueprint('item5_pounds', __name__, template_folder='templates/calculator')
item6_info_blueprint = Blueprint('item6_pounds', __name__, template_folder='templates/calculator')
item7_info_blueprint = Blueprint('item7_pounds', __name__, template_folder='templates/calculator')
item_review_blueprint = Blueprint('item_delete', __name__, template_folder='templates/calculator')
order_summary_blueprint = Blueprint('order_summary', __name__, template_folder='templates/calculator')

# This is the list that stores the items
cart_list = []
item1_dict = {}
item2_dict = {}
item3_dict = {}
item4_dict = {}
item5_dict = {}
item6_dict = {}
item7_dict = {}


# This is the route for the form that identifies the total pounds of meat you have
@pounds_blueprint.route('/basic_info', methods=['GET', 'POST'])
def total_pounds():
    form = PoundForm()

    if form.validate_on_submit():
        session['remaining_pounds'] = round(form.total_pounds.data)
        session['total_price'] = 0
        return render_template('item_list.html')

    return render_template('basic_info.html', form=form)


# This is the route for the first item in the list
# This asks for a form of how many pounds you would like to order for the item
@item1_info_blueprint.route('/item1_info', methods=['GET', 'POST'])
def item1_info():
    form = ItemOneForm()

    if form.validate_on_submit():
        session['item1_pounds'] = form.item1_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item1_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item1_pounds']
            session['item1_price'] = items_list[2]['price'] * session['item1_pounds']
            session['total_price'] = session['total_price'] + session['item1_price']
            cart_list.append(items_list[2]['item_name'])
            item1_dict['name'] = items_list[2]['item_name']
            item1_dict['pounds'] = session['item1_pounds']
            item1_dict['price'] = session['item1_price']
            return render_template('item_list.html')

    return render_template('item1_info.html', form=form, item1_name=items_list[2]['item_name'],
                           item1_price=round(float(items_list[2]['price']), 2))


# This is the route for the second item in the list
# This asks for a form of how many pounds you would like to order for the item
@item2_info_blueprint.route('/item2_info', methods=['GET', 'POST'])
def item2_info():
    form = ItemTwoForm()

    if form.validate_on_submit():
        session['item2_pounds'] = form.item2_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item2_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
            # print(session['total_price'])
            # print(session['remaining_pounds'])
            # print(cart_list)
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item2_pounds']
            session['item2_price'] = items_list[3]['price'] * session['item2_pounds']
            session['total_price'] = session['total_price'] + session['item2_price']
            cart_list.append(items_list[3]['item_name'])
            item2_dict['name'] = items_list[3]['item_name']
            item2_dict['pounds'] = session['item2_pounds']
            item2_dict['price'] = session['item2_price']
            return render_template('item_list.html')

    return render_template('item2_info.html', form=form, item2_name=items_list[3]['item_name'],
                           item2_price=round(float(items_list[3]['price']), 2))


# This is the route for the third item in the list
# This asks for a form of how many pounds you would like to order for the item
@item3_info_blueprint.route('/item3_info', methods=['GET', 'POST'])
def item3_info():
    form = ItemThreeForm()

    if form.validate_on_submit():
        session['item3_pounds'] = form.item3_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item3_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
            # print(session['total_price'])
            # print(session['remaining_pounds'])
            # print(cart_list)
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item3_pounds']
            session['item3_price'] = items_list[6]['price'] * session['item3_pounds']
            session['total_price'] = session['total_price'] + session['item3_price']
            cart_list.append(items_list[6]['item_name'])
            item3_dict['name'] = items_list[6]['item_name']
            item3_dict['pounds'] = session['item3_pounds']
            item3_dict['price'] = session['item3_price']
            return render_template('item_list.html')

    return render_template('item3_info.html', form=form, item3_name=items_list[6]['item_name'],
                           item3_price=round(float(items_list[6]['price']), 2))


@item4_info_blueprint.route('/item4_info', methods=['GET', 'POST'])
def item4_info():
    form = ItemFourForm()

    if form.validate_on_submit():
        session['item4_pounds'] = form.item4_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item4_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item4_pounds']
            session['item4_price'] = items_list[4]['price'] * session['item4_pounds']
            session['total_price'] = session['total_price'] + session['item4_price']
            cart_list.append(items_list[4]['item_name'])
            item4_dict['name'] = items_list[4]['item_name']
            item4_dict['pounds'] = session['item4_pounds']
            item4_dict['price'] = session['item4_price']
            return render_template('item_list.html')

    return render_template('item4_info.html', form=form, item4_name=items_list[4]['item_name'],
                           item4_price=round(float(items_list[4]['price']), 2))


@item5_info_blueprint.route('/item5_info', methods=['GET', 'POST'])
def item5_info():
    form = ItemFiveForm()

    if form.validate_on_submit():
        session['item5_pounds'] = form.item5_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item5_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item5_pounds']
            session['item5_price'] = items_list[0]['price'] * session['item5_pounds']
            session['total_price'] = session['total_price'] + session['item5_price']
            cart_list.append(items_list[0]['item_name'])
            item5_dict['name'] = items_list[0]['item_name']
            item5_dict['pounds'] = session['item5_pounds']
            item5_dict['price'] = session['item5_price']
            return render_template('item_list.html')

    return render_template('item5_info.html', form=form, item5_name=items_list[0]['item_name'],
                           item5_price=round(float(items_list[0]['price']), 2))


@item6_info_blueprint.route('/item6_info', methods=['GET', 'POST'])
def item6_info():
    form = ItemSixForm()

    if form.validate_on_submit():
        session['item6_pounds'] = form.item6_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item6_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item6_pounds']
            session['item6_price'] = items_list[5]['price'] * session['item6_pounds']
            session['total_price'] = session['total_price'] + session['item6_price']
            cart_list.append(items_list[5]['item_name'])
            item6_dict['name'] = items_list[5]['item_name']
            item6_dict['pounds'] = session['item6_pounds']
            item6_dict['price'] = session['item6_price']
            return render_template('item_list.html')

    return render_template('item6_info.html', form=form, item6_name=items_list[5]['item_name'],
                           item6_price=round(float(items_list[5]['price']), 2))


@item7_info_blueprint.route('/item7_info', methods=['GET', 'POST'])
def item7_info():
    form = ItemSevenForm()

    if form.validate_on_submit():
        session['item7_pounds'] = form.item7_pounds.data

        # This if-else statement checks to see if you have enough meat to order your requested amount
        # The if clause checks if the remaining meat is less than the meat asked for
        # if it holds true the user cannot continue with the order
        # if the user has enough it continues on with the form
        if session['remaining_pounds'] < session['item7_pounds']:
            flash('Sorry, you cannot complete this item order. You do not have enough meat remaining.')
        else:
            session['remaining_pounds'] = session['remaining_pounds'] - session['item7_pounds']
            session['item7_price'] = items_list[1]['price'] * session['item7_pounds']
            session['total_price'] = session['total_price'] + session['item7_price']
            cart_list.append(items_list[1]['item_name'])
            item7_dict['name'] = items_list[1]['item_name']
            item7_dict['pounds'] = session['item7_pounds']
            item7_dict['price'] = session['item7_price']
            return render_template('item_list.html')

    return render_template('item7_info.html', form=form, item7_name=items_list[1]['item_name'],
                           item7_price=round(float(items_list[1]['price']), 2))


@item_review_blueprint.route('/item_review', methods=['GET', 'POST'])
def order_review():
    form = OrderReview()

    if form.validate_on_submit():
        session['item_delete'] = form.item_delete.data
        if session['item_delete'].lower() == 'cancel':
            for item in cart_list:
                cart_list.remove(item)
            session['total_price'] = 0
            session['remaining_pounds'] = 0
            return redirect(url_for('total_pounds.total_pounds'))
        elif session['item_delete'] == '':
            pass
        else:
            cart_list.remove(session['item_delete'])
            return redirect(url_for('item_delete.order_review'))

    return render_template('order_review.html', form=form, cart_list=cart_list)


@order_summary_blueprint.route('/order_summary', methods=['GET', 'POST'])
def summary():
    form = OrderSummary()

    if form.validate_on_submit():
        for item in cart_list:
            cart_list.remove(item)
        item1_dict.clear()
        item2_dict.clear()
        item3_dict.clear()
        item4_dict.clear()
        item5_dict.clear()
        item6_dict.clear()
        item7_dict.clear()
        session['total_price'] = 0
        session['remaining_pounds'] = 0
        return redirect(url_for('homepage'))

    return render_template('order_summary.html',  item1_dict=item1_dict, item2_dict=item2_dict, item3_dict=item3_dict,
                           item4_dict=item4_dict, item5_dict=item5_dict, item6_dict=item6_dict, item7_dict=item7_dict,
                           total_price=session['total_price'], remaining_pounds=session['remaining_pounds'], form=form)

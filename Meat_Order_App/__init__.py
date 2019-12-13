from flask import Flask, render_template
from Meat_Order_App.calculator.views import pounds_blueprint, item1_info_blueprint, item2_info_blueprint, \
                                            item3_info_blueprint, item_review_blueprint, order_summary_blueprint, \
                                            item4_info_blueprint, item5_info_blueprint, item6_info_blueprint, \
                                            item7_info_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'markssecretkey'

app.register_blueprint(pounds_blueprint, url_prefix='/basic_info')
app.register_blueprint(item1_info_blueprint, url_prefix='/item1_info')
app.register_blueprint(item2_info_blueprint, url_prefix='/item2_info')
app.register_blueprint(item3_info_blueprint, url_prefix='/item3_info')
app.register_blueprint(item4_info_blueprint, url_prefix='/item4_info')
app.register_blueprint(item5_info_blueprint, url_prefix='/item5_info')
app.register_blueprint(item6_info_blueprint, url_prefix='/item6_info')
app.register_blueprint(item7_info_blueprint, url_prefix='/item7_info')
app.register_blueprint(item_review_blueprint, url_prefix='/item_review')
app.register_blueprint(order_summary_blueprint, url_prefix='/order_summary')


@app.route('/item_list')
def products():

    return render_template('item_list.html')


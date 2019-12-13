# This is the main Flask app
# This file is located at the top level and will initalize the app

from Meat_Order_App import app
from flask import render_template


@app.route('/')
def homepage():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


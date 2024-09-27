from flask import Flask,render_template
from CustomerDAO import CustomerDAO
app = Flask(__name__)

# flask run --debug
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def customers():
    dao = CustomerDAO('customers_db.db')
    customers = list(dao.find_all())
    return render_template("customers.j2",customers=customers)
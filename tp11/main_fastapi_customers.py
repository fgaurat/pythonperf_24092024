from typing import List
from fastapi import FastAPI
from CustomerDAO import CustomerDAO
from Customer import Customer
from CustomerCreate import CustomerCreate

app = FastAPI()

# fastapi dev main_fastapi_customers.py
@app.get("/",response_model=List[Customer])
def get_customers():
    dao = CustomerDAO('customers_db.db')
    customers = dao.find_all()
    return customers


@app.post("/",response_model=Customer)
def create_customer(customer:CustomerCreate):
    dao = CustomerDAO('customers_db.db')
    c = dao.create(customer)
    return c



from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import cgi

app=FastAPI()

class Info(BaseModel):
    customer_name: str
    age: str
    salary: str
    address: str
    gender: str
    
@app.get("/")
def basic():
    return "This is a Customer Database System"
    
    
@app.post("/name")
def name(customer_name_var:Info):
    cust_name_encoded=jsonable_encoder(customer_name_var)
    print(cust_name_encoded)
    name=cust_name_encoded['customer_name']
    age = cust_name_encoded['age']
    print("Their age is", age)
    salary=cust_name_encoded['salary']
    print("Their salary is",salary)
    address=cust_name_encoded['address']
    print("Their address is",address)
    gender=cust_name_encoded['gender']
    return name,gender,age,salary,address
    

form = cgi.FieldStorage()
d = form.getvalue('customer_details')
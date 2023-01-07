from fastapi import FastAPI, Form
import mysql.connector as msql

app = FastAPI() 

"""
    Run api server
    $uvicorn main:app --reload 
"""

@app.get("/hello-my-web")
def hello_my_web():
    result = 10+20
    return result

@app.get("/sum")
def sum(num1, num2): # parameter
    result = float(num1)+float(num2)
    return result

@app.post("/sum-post")
def sum(num1: float = Form(), num2: float = Form()): # parameter
    result = num1+num2
    return result
    
@app.get("/test-list")
def test_list():
    return [{"firstname": "Aungkoon", "lastname": "Kongpet"}, {"firstname": "Sara", "lastname": "Homes"}]

@app.get("/get-all-income")
def getAllIncome():
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("select * from income_outcome")
    result = cursor.fetchall()
    return result

@app.post("/insert-income")  
def insert_sql(desc: str = Form(),amount: float =Form(),date:  str = Form() ):
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor()
    cursor.execute(f"insert into income_outcome(description,amount,date) values ('{desc}',{amount},'{date}')")
    mydb.commit()
    
    rowcount = cursor.rowcount
    return {"rowcount": rowcount}
@app.delete("/delete-income")  
def delete_sql(id: int = Form()):
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor()
    cursor.execute(f"delete from income_outcome where id={id}")
    mydb.commit()
    
    rowcount = cursor.rowcount
    return {"rowcount": rowcount}  
    





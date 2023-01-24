from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector as msql
from model.IncomeOutcome import IncomeOutcome
import time

app = FastAPI() 

"""
    Run api server
    $uvicorn main:app --reload 
"""

app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:5500"], allow_methods=["GET","POST","PUT","DELETE"])


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
    start = time.time()
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor(dictionary=True)
    error_msg =""
    result = []
    try:
        cursor.execute("select * from income_outcome")
        result = cursor.fetchall()
    except Exception as e:
        error_msg =str(e)
    cursor.close()
    mydb.close()
    took = time.time()-start
    return {"data": result, "took":took ,"error_msg":error_msg}

@app.post("/insert-income")  
def insert_sql(body: IncomeOutcome):
    start = time.time()
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor()
    rowcount = 0
    error_msg= ""
    try:
        cursor.execute(f"insert into income_outcome(description,amount,date) values ('{body.desc}',{body.amount},'{body.date}')")
        mydb.commit()
        rowcount = cursor.rowcount
        insertedID = cursor.lastrowid
    except Exception as e:
        error_msg =str(e)
    cursor.close()
    mydb.close()
    took = time.time()-start
    return {"rowcount": rowcount,"took": took, "insertedID": insertedID, "error_msg":error_msg}

@app.delete("/delete-income")  
def delete_sql(body: IncomeOutcome):
    start = time.time()
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor()
    error_msg=""
    rowcount =0
    try:
        cursor.execute(f"delete from income_outcome where id={body.id}")
        mydb.commit()
        rowcount = cursor.rowcount
    except Exception as e:
        error_msg = str(e)
    cursor.close()
    mydb.close()
    took = time.time()-start
    return {"rowcount": rowcount,"took":took,"error_msg":error_msg}  
    
@app.put("/update-income")
def update_sql(body: IncomeOutcome):
    start_time = time.time()
    err_msg = ""
    rowcount = 0
    mydb = msql.connect(host="localhost", user="root", password="root", port="8889", database="my-web")
    cursor = mydb.cursor()
    
    try:
        sql = f"""update income_outcome set description = '{body.desc}',amount = {body.amount},date = '{body.date}'  
                    where id = {body.id}
                """
        cursor.execute(sql)
        mydb.commit()
        rowcount = cursor.rowcount
    except Exception as e:
        err_msg = str(e)

    cursor.close()
    mydb.close()
    took = time.time() - start_time
    return {"rowcount": rowcount, "took": took, "err_msg": err_msg}





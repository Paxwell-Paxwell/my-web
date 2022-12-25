from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-my-web")
def hello_my_web():
    result = 10+20
    return result

@app.get("/test-list")
def test_list():
    return [{"firstname": "Aungkoon", "lastname": "Kongpet"}, {"firstname": "Sara", "lastname": "Homes"}]



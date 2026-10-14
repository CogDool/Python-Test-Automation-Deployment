from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "COMPLETE", "Message": "All Good Bruh"}

def calculate_total(price: float, tax: float) -> float:
    return price + (price * tax)


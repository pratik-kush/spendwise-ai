
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv('data/transactions.csv')

@app.get("/")
def root():
    return {"msg": "SpendWise AI Running"}

@app.get("/summary")
def summary():
    total_expense = df[df['type']=='debit']['amount'].sum()
    total_income = df[df['type']=='credit']['amount'].sum()
    return {"income": int(total_income), "expense": int(total_expense)}

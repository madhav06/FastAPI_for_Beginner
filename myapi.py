from typing import Optional

from fastapi import FastAPI

app = FastAPI()

'''
GET - GET an Information
POST - Create Something new
PUT - Update
DELETE - Delete something
'''
@app.get("/")
def index():
    return { "name": "First Data" } 

from fastapi import FastAPI
import json
app=FastAPI()

@app.get('/')
def get_schema():
    with open('schema.json','r') as f:
        data=json.load(f)
    print(data)
    return data


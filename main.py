# import libaray 
import uvicorn #ASGI SERVER
from fastapi import FastAPI


#2. create the app object
app  = FastAPI()

# 3. Index route, opens automatically on http://27.0.0.1:8000
@app.get('/') # inidicate homepage inshot 
def index():
    return {'message':"Hello, stranger"}

#4. Route with a single parameter, returns the parameter within a message 
#Located at: http://127.0.0.1:8000/Anywhere

@app.get('/Welcome')
def get_name(name:str): # parameter
    return {'welcome To hs shivania group':f'{name}'}


#5 run the whole above code ith uvicorn server
#will run in http://127.0.0.1:8000




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
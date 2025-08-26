from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Kingo'}}


@app.get('/about')
def about():
    return {'data': 'This is the about page'}
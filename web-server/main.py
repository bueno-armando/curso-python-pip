import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# GET LIST
@app.get('/') # decorator for resource
def get_list():
    return [1, 2, 3]

# GET CONTACT
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return"""
        <h1>NUEVA PAGINA DE SENORBUEN0</h1>
        <p>(WIP)</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
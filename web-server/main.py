import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#instancia de fastapi
app = FastAPI()

# declarador
@app.get('/')
def get_list():
    return [1,2,3]
# ahora estamos devolviendo una variable, lo apropiado
# seria devolver documentos HTML

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Mi primera página en un servidor :)</h1>
        <p>Un paragraph</p>
    """

def run():
    store.get_categories()

if __name__ == "__main__":
    run()
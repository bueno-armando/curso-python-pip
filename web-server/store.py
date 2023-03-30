import requests as rq

def get_categories():
    # comando principal
    myReq  = rq.get("https://api.escuelajs.co/api/v1/categories")
    print(myReq.status_code) #200 = todo está bien
    print(myReq.text)
    print(type(myReq.text)) # String (no nos sirve para manejarlo)
    # con el método json se transforma en lista
    categories = myReq.json()
    for category in categories:
        print(category['name'])
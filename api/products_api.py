import requests

def get_product(product_id):

    return requests.get(
        f"https://dummyjson.com/products/{product_id}"
    )
import requests

from config.config import API_BASE_URL

def get_product(product_id):

    return requests.get(
        f"{API_BASE_URL}/products/{product_id}"
    )
import pytest

from api.products_api import get_product

@pytest.mark.api
def test_get_product():

    response = get_product(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"]==1
    assert "title" in data
    assert isinstance(data["price"],(int,float))

@pytest.mark.api
def test_get_invalid_product():

    response = get_product(9999)

    assert response.status_code == 404
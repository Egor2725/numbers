import pytest
from core.views import find_prime_numbers


def test_status_code(client):
    response = client.get('/number/')
    assert response.status_code


def test_check_number(client):
    response = client.get('/number/')
    number = response.json()['random_prime_number']
    assert number in find_prime_numbers()


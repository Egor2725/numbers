import pytest
from core.views import find_prime_numbers

import logging

LOGGER = logging.getLogger(__name__)


# def test_eggs():
#     LOGGER.info('eggs info')
#     LOGGER.warning('eggs warning')
#     LOGGER.error('eggs error')
#     LOGGER.critical('eggs critical')
#     assert True


def test_status_code(client):
    try:
        response = client.get('/number/')
        assert response.status_code
        LOGGER.info('Test status code')
    except:
        LOGGER.error(f'Error in test status code')


def test_check_number(client):
    try:
        response = client.get('/number/')
        number = response.json()['random_prime_number']
        assert number in find_prime_numbers()
        LOGGER.info(f'Check number {number} is prime.')
    except:
        LOGGER.error(f'Error in test check number')


import uuid
import pytest
import logging

from django.urls import reverse
from django.http.response import HttpResponseForbidden

from core.utils import is_prime

logger = logging.getLogger(__name__)


@pytest.fixture
def test_password():
    logger.info('[FIXTURE] test_password start')
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    logger.info('[FIXTURE] create_user start')

    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    logger.info('[FIXTURE] create_user success')
    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    logger.info('[FIXTURE] auto_login_user start')

    def make_auto_login(user=None):
        if user is None:
            logger.info('[FIXTURE] auto_login_user user is None')
            user = create_user()
        client.login(username=user.username, password=test_password)
        logger.info('[FIXTURE] auto_login_user client successfully login')

        return client, user

    logger.info('[FIXTURE] auto_login_user success')

    return make_auto_login


def test_primary_number(auto_login_user):
    logger.info('[TEST] primary_number start')
    number = 0
    try:
        url = reverse('number')
        client, user = auto_login_user()
        response = client.get(url)
        number = response.json().get('number')

    except Exception as e:
        logger.error(f'[ERROR] primary_number finished with error {e}')
        response = HttpResponseForbidden()
    assert response.status_code == 200
    assert is_prime(number)
    logger.info('[TEST] primary_number success')

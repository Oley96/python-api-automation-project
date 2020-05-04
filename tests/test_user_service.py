from hamcrest import has_length, greater_than
import pytest
from src.conditions import status_code, body, content_type
from src.models import get_user
from src.services import UserApiService


@pytest.mark.api
@pytest.mark.positive
def test_can_register_user_with_valid_credentials(faker):
    user = get_user(faker)

    UserApiService().register_customer(user) \
        .should_have(status_code(200)) \
        .should_have(body("$.id", has_length(greater_than(0))))


@pytest.mark.api
@pytest.mark.negative
def test_can_not_register_user_with_valid_credentials_twice(faker):
    user = get_user(faker)

    UserApiService().register_customer(user) \
        .should_have(status_code(200)) \
        .should_have(body("$.id", has_length(greater_than(0))))

    UserApiService().register_customer(user) \
        .should_have(status_code(500))


@pytest.mark.api
@pytest.mark.positive
def test_user_should_login_with_valid_credentials(faker):
    user = get_user(faker)

    UserApiService().register_customer(user)
    UserApiService().login_with(user) \
        .should_have(status_code(200)) \
        .should_have(content_type("text/html"))


@pytest.mark.api
@pytest.mark.negative
def test_user_should_not_login_without_credentials():
    UserApiService().login() \
        .should_have(content_type("text/plain")) \
        .should_have(status_code(401))


@pytest.mark.api
@pytest.mark.positive
def test_get_customers():
    UserApiService().get_customers() \
        .should_have(status_code(200)) \
        .should_have(content_type("text/plain")) \
        .should_have(body("$._embedded.customer[*]", has_length(greater_than(5)))) \
        .should_have(body("$..id", has_length(greater_than(5)))) \
        .should_have(body("$._embedded.customer[0].username", "Sandy Young"))


@pytest.mark.api
@pytest.mark.positive
def test_get_specific_customer(faker):
    user = get_user(faker)
    id = UserApiService().register_customer(user).json("id")

    UserApiService().get_customer(id) \
        .should_have(status_code(200)) \
        .should_have(content_type("text/plain"))


@pytest.mark.api
@pytest.mark.positive
def test_delete_customer_by_id(faker):
    user = get_user(faker)
    id = UserApiService().register_customer(user).json("id")

    UserApiService().delete_customer(id) \
        .should_have(status_code(200)) \
        .should_have(content_type("text/plain")) \
        .should_have(body("$.status", True))


@pytest.mark.api
@pytest.mark.positive
def test_get_addresses():
    UserApiService().get_addresses() \
        .should_have(status_code(200)) \
        .should_have(content_type("text/plain")) \
        .should_have(body("$._embedded.address[0].street", "my road")) \
        .should_have(body("$._embedded.address[0].country", "UK")) \
        .should_have(body("$._embedded.address[0].city", "London"))

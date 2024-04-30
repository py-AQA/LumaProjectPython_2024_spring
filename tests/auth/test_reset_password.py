import pytest

from pages import forgot_password, message


@pytest.mark.debug
def test_reset_password():
    forgot_password.visit()
    forgot_password.reset("jasonbrown1714146903@example.net")
    message.should_be("you wi111111111ll receive an email")

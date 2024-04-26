from pages import forgot_password, message


def test_reset_password():
    forgot_password.visit()
    forgot_password.reset("sex@sex.com")
    message.should_be("you will receive an email")

from pages import sign_in, my_account, message


def test_sign_in_with_good_credentials():
    sign_in.visit()
    sign_in.login("pamela341714226113@example.com", "@8j%Yltt(E")
    my_account.page_title("My Account")


def test_sign_in_with_bad_credentials():
    sign_in.visit()
    sign_in.login("jasonbrown1714146903@example.net", "wrong_password")
    message.should_be("The account sign-in was incorrect")

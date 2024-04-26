from pages import sign_in, my_account, message


def test_sign_in_with_good_credentials():
    sign_in.visit()
    sign_in.login("jasonbrown1714146903@example.net", "VLK))5JiLA")
    my_account.page_title("The account sign-in was incorrect")


def test_sign_in_with_bad_credentials():
    sign_in.visit()
    sign_in.login("jasonbrown1714146903@example.net", "wrong_password")
    message.should_be("The account sign-in was incorrect")

from pytest import mark


@mark.ui
def test_can_navigate_to_body_page(firefox_browser):
    firefox_browser.get('https://www.motortrend.com/')
    assert True


@mark.ui
def test_function_two(firefox_browser):
    firefox_browser.get('https://www.google.com/')
    assert True


@mark.ui
def test_function_three(firefox_browser):
    firefox_browser.get('https://www.bing.com/')
    assert True

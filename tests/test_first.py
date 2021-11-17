import time


def test_first(browser, url):
    browser.get(url)
    time.sleep(1)
    assert browser.title == "Your Store"

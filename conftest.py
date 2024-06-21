import pytest
from selenium import webdriver
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action='store',
        default='dev',
        help='Test environment (dev, qa)'
    )


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    print(cfg)
    return cfg


@pytest.fixture(scope='session')
def firefox_browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()



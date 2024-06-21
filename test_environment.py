from pytest import mark


@mark.env
def test_enviroment_is_qa(app_config):
    assert app_config.base_url == 'https://myqa-env.com'
    assert app_config.app_port == 8081


@mark.env
def test_enviroment_is_dev(app_config):
    assert app_config.base_url == 'https://mydev-env.com'
    assert app_config.app_port == 8080


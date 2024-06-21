from pytest import mark
# Markers are a wau to mark tests
# We have to import the decorator
# Smoke tests are the bare minimum tests that I have to run after a change


@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

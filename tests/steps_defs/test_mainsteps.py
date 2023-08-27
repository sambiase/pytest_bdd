"""Test Feature feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

scenarios('../features/maintests.feature')

@given('An odd number is typed')
def test_verify_odd_number():
    assert 3==3

@given('this odd number is equal to 3')
def test_numberIs3():
    assert 3==3

@then('Success')
def test_success():
    pass


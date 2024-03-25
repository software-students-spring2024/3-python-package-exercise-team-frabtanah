import pytest
from pyMood.mood import coffee_suggestion
from pyMood.coffee_types import coffee_types



class Test: 
    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        yield 


    def test_coffee_suggestion():

        suggestion = coffee_suggestion()

        assert suggestion.startswith("How about a cup of ")
        coffee_type = suggestion[18:-9]
        assert coffee_type in coffee_types



import pytest 
from pyMood.mood import coffee_suggestion
from pyMood.coffee_types import coffee_types



class Test: 

    def test_coffee_suggestion():

        suggestion = coffee_suggestion()

        assert suggestion.startswith("How about a cup of ")
        coffee_type = suggestion[18:-9]
        assert coffee_type in coffee_types



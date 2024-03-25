import pytest 
from pyMood.mood import coffee_suggestion, relaxation_tip
from pyMood.coffee_types import coffee_types
from pyMood.relaxation_tips import relaxation_tips



class TestMood: 

    def test_coffee_suggestion(self):

        suggestion = coffee_suggestion()

        assert suggestion.startswith("How about a cup of ")
        coffee_type = suggestion[18:-9]
        assert coffee_type in coffee_types


    def test_return_tip_from_specified_category(self):
        """
            Test if the function returns a tip from the specified category.
        """
        for category in relaxation_tips.keys():
            tip = relaxation_tip(category)
            assert tip in relaxation_tips[category], f"The tip should be from the {category} category."

    def test_return_tip_with_no_category(self):
        """
            Test if the function returns a tip when no category is specified.
        """
        tip = relaxation_tip()
        all_tips = [item for sublist in relaxation_tips.values() for item in sublist]
        assert tip in all_tips, "The function should return a valid tip when no category is specified."
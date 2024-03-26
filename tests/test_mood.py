import pytest 
from pyMood.mood import coffee_suggestion, relaxation_tip, cat_mood_generator
from pyMood.coffee_types import coffee_types
from pyMood.relaxation_tips import relaxation_tips



class TestMood: 

    def test_coffee_suggestion(self):

        suggestion = coffee_suggestion()

        assert suggestion.startswith("How about a cup of ")
        prefix = "How about a cup of "
        suffix = " today?"
        coffee_type = suggestion[len(prefix):-len(suffix)]
        assert coffee_type in coffee_types, f"Extracted coffee type was '{coffee_type}'"


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
    

    def test_cat_mood_generator(self):
        expected_moods = ["Playful", "Sleepy", "Hungry", "Grumpy"]
        
        mood = cat_mood_generator()
        
        assert mood in expected_moods, f"The mood {mood} is not in the list of expected moods."
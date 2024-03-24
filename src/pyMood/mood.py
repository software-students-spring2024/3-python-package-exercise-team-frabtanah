import random
from affirmations import affirmations
from coffee_types import coffee_types



def get_affirmation():
    """
    Returns a random positive affirmation to boost the user's mood and confidence.
    """

    return random.choice(affirmations)

def tell_me_a_joke():
    """
        Returns a random joke to lightne up the user's mood. 
    """


def coffee_suggestion():
    """
        Returns a random cup of coffee as a suggestion. 
    """


    suggestion = random.choice(coffee_types)
    return f"How about a cup of {suggestion} today?"


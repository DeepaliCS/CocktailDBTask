import requests


COCKTAILDB_URL = "https://www.thecocktaildb.com/api/json/v1/1"

def get_cocktails(drink_type="Cocktail"):
    """
    Return a list of drinks and their id & image data,
    default is set to Cocktail type drinks, other options
    include "Ordinary_Drink"
    """
    return requests.get(f'{COCKTAILDB_URL}/filter.php?c={drink_type}')

def get_ingredients(id_lookup=11007):
    """
    Return a list of cocktail detail, do a lookup based on the ID.
    Use 11007 if no value is passed as default. (For tests)
    """
    return requests.get(f'{COCKTAILDB_URL}/lookup.php?i={id_lookup}')

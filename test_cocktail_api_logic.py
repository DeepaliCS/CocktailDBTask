
import unittest
from cocktaildbAPI import get_cocktails, get_ingredients
from logic import (
    get_list_of_cocktail_name_and_ids, 
    update_list_for_ingredients, 
    match_ingredients_to_cocktails
)


class TestGetCocktailsDBAPI(unittest.TestCase):
    """
    Test to ensure the cocktail DB API is returning
    with a 200 status.
    """

    def test_get_cocktails(self):
        result = get_cocktails()
        self.assertEqual(result.status_code, 200)

    def test_get_ingredients(self):
        result = get_ingredients()
        self.assertEqual(result.status_code, 200)

class TestCocktailDataLogic(unittest.TestCase):
    """
    Test to ensure the methods in the logic file
    return data lists with validated content.
    """
    
    NAME_AND_IDS = get_list_of_cocktail_name_and_ids()
    UPDATED_LIST = update_list_for_ingredients(NAME_AND_IDS)

    def test_list_include_cocktail_ids(self):
        cocktail_detail = self.NAME_AND_IDS
        result = cocktail_detail[0]
        self.assertIsInstance(int(result[0]), int)

    def test_ingredients_are_placed_correctly(self):

        updated_list = self.UPDATED_LIST
        result = updated_list[0]
        self.assertIsInstance(result[2], dict)

    
    # def test_matches_are_found(self):
    #     """
    #     Ensure that the cocktail search by ingredients process
    #     below, can return cocktails.
    #     """

    #     updated_list = self.UPDATED_LIST
    #     result = match_ingredients_to_cocktails(["Apple Juice, Carrot"], updated_list)
    #     self.assertEqual(result[0], "Apple Karate")

if __name__ == '__main__':
    unittest.main()

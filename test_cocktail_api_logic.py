
import unittest
from cocktaildbAPI import get_cocktails, get_ingredients


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

if __name__ == '__main__':
    unittest.main()

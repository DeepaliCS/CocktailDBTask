import json
import re

from cocktaildbAPI import get_cocktails, get_ingredients


def get_list_of_cocktail_name_and_ids():
    """
    Create a list of cocktail ID and names.
    """

    cocktail_drinks = json.loads(get_cocktails().content)['drinks']
    essential_cocktail_detail = [[drink['idDrink'], drink['strDrink']] for drink in cocktail_drinks]
    return essential_cocktail_detail

def update_list_for_ingredients(essential_cocktail_detail):
    """
    Update the list passed in as argument to include all ingredients
    required to make it.
    """

    for cocktail_detail in essential_cocktail_detail:
        id = int(cocktail_detail[0])
        cocktail_data = json.loads(get_ingredients(id).content)['drinks'][0]

        ingredients_list = []
        ingredients_dict = {}
        for key, value in cocktail_data.items():
            if re.match(r'(strIngredient[0-9])', key) and value != None:
                ingredients_list.append(value.lower())
            ingredients_dict = {"ingredients": ingredients_list}

        cocktail_detail.append(ingredients_dict)
    return essential_cocktail_detail

def match_ingredients_to_cocktails(user_ingredients, updated_list):
    """
    Collect the user's input (ingredients) to find which cocktail(s)
    they can make.
    """
    user_ingredients = ["gin, soda water, lime"]
    return [cocktail_detail[1] for cocktail_detail in updated_list if user_ingredients == cocktail_detail[2]["ingredients"]]


    

# def main():
#     print("***********")

#     this = get_list_of_cocktail_name_and_ids()
#     that = update_list_for_ingredients(this)

#     # print(this)
#     # print("---")
#     # print(that)

#     those = match_ingredients_to_cocktails("", that)
#     print(those)


#     print("***********")


# if __name__ == '__main__':
#     main()
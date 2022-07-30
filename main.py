from logic import (
    get_list_of_cocktail_name_and_ids,
    update_list_for_ingredients,
    match_ingredients_to_cocktails
)


def introduction():
    """
    Take user's input.
    """

    inputted_values = input()
    ingredients = list(inputted_values.lower().split(", "))
    return ingredients


def main():
    print("***********")

    user_ingredients = introduction()

    essential_cocktail_detail = get_list_of_cocktail_name_and_ids()
    updated_list = update_list_for_ingredients(essential_cocktail_detail)
    matches = match_ingredients_to_cocktails(user_ingredients, updated_list)

    print(matches)

    print("***********")


if __name__ == '__main__':
    main()

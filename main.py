from logic import (
    get_list_of_cocktail_name_and_ids,
    update_list_for_ingredients,
    match_ingredients_to_cocktails
)


def introduction():
    """
    Take user's input.
    """

    print("Hi, Welcome to Cocktail Creator! Let's find you a chilling drink to make!")
    print("What ingredients do you have at home? (Please list them as a comma separated list.)")

    inputted_values = input()
    ingredients = list(inputted_values.lower().split(", "))
    return ingredients


def main():
    print("***********")

    user_ingredients = introduction()
    print("Thank you, finding some cocktails for you now .. Give me a second..")

    essential_cocktail_detail = get_list_of_cocktail_name_and_ids()
    updated_list = update_list_for_ingredients(essential_cocktail_detail)
    matches = match_ingredients_to_cocktails(user_ingredients, updated_list)

    if not matches:
        print("Unfortunately, there are no cocktails you can make with those ingredients, go shopping!")
    else:
        print("Cocktail(s) you can make are: ")
        for match in matches:
            print(match)

    print("***********")


if __name__ == '__main__':
    main()

import requests, json


def find_recipes(ingredients):
    """
    Makes json file with info about recipes got from given ingredients
    :param recipes: list
    :return: None
    """
    ing = ''
    for i in ingredients:
        ing += i
        if i != ingredients[-1]:
            ing += '%2C'

    connection = requests.get(
        "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=3&ranking=1&ingredients={}".format(
            ing),
        headers={"X-RapidAPI-Key": "02709a836amshe35a053f36369f1p11274bjsnf37502547767"})
    data_dict = dict()
    data = connection.json()
    for i in data:
        meal = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information".format(i['id']),
            headers={"X-RapidAPI-Key": "02709a836amshe35a053f36369f1p11274bjsnf37502547767"})
        data_dict[i['id']] = meal.json()

    with open("../API_functions/json_files/data.json", "w") as file:
        json.dump(data_dict, file, indent=4, separators=(',', ': '))


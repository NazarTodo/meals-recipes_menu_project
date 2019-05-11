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
        headers={"X-RapidAPI-Key": "9f9fc080c3msh8a9cf2e4d3c73b2p18d065jsn085866fe1f37"})
    data_dict = dict()
    data = connection.json()
    for i in data:
        meal = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information".format(i['id']),
            headers={"X-RapidAPI-Key": "9f9fc080c3msh8a9cf2e4d3c73b2p18d065jsn085866fe1f37"})
        data_dict[i['id']] = meal.json()

    with open("json_files/data.json", "w") as file:
        json.dump(data_dict, file, indent=4, separators=(',', ': '))


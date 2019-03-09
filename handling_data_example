import requests, json


def find_recipes(ingredients):
    """
    :param recipes: list
    :return: None
    Makes json file with info about recipes got from given ingredients
    """
    ing = ''
    for i in ingredients:
        ing += i
        if i != ingredients[-1]:
            ing += '%2C'

    connection = requests.get(
        "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=3&ranking=1&ingredients={}".format(
             ing),
        headers={"X-RapidAPI-Key": "key"})
    data_dict = dict()
    data = connection.json()
    for i in data:
        meal = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information".format(i['id']),
            headers={"X-RapidAPI-Key": "key"})
        data_dict[i['id']] = meal.json()

    with open("data.json", "w") as file:
        json.dump(data_dict, file, indent=4, separators=(',', ': '))
    return None


if __name__ == "__main__":
    find_recipes(['apples', 'flour', 'sugar'])

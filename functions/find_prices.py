import json, pprint


def find_product(filename):
    products = dict()
    recepies = dict()
    with open(filename) as f:
        data = json.load(f)
    for i in data.values():
        recepies[i['title']] = i["instructions"]
        products[i['title']] = [i["pricePerServing"]]
        for j in i["extendedIngredients"]:
            products[i['title']].append(
                (j['name'], j['measures']['metric']['amount'], j['measures']['metric']['unitShort']))
    pprint.pprint(recepies, indent=4)

if __name__ == '__main__':
    find_product("Api_Example/data.json")

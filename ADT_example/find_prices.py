import json, adt


def find_product(filename):
    products = dict()
    recepies = dict()
    with open(filename) as f:
        data = json.load(f)
    for i in data.values():
        products[i['title']] = adt.LinkedList()
        recepies[i['title']] = [i["instructions"]]
        recepies[i['title']].append([i["pricePerServing"]])
        for j in i["extendedIngredients"]:
            products[i['title']].add(
                (j['name'], j['measures']['metric']['amount'], j['measures']['metric']['unitShort']))
        products[i['title']].change_metric()
    for key ,value in products.items():
        print(key)
        print(value)


if __name__ == '__main__':
    find_product("data.json")

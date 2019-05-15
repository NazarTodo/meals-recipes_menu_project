import json
from API_functions.tesco_api import find_price

def price_product(product):
    """
    Returns price of a product using Tesco API
    tuple -> float
    :param Node (tuple)
    :return float
    """
    special = 0.1
    prod = product.item[0]
    quantity = product.item[2]
    amount = product.item[1]
    # making a json file of each product
    find_price(prod)
    with open('API_functions/json_files/products.json', 'r') as f:
        data = json.load(f)
    prices = []
    for item in data['uk']['ghs']['products']['results']:
        if item['UnitQuantity'] == quantity:
            prices.append(item['unitprice'])
        elif quantity == '':
            prices.append(item['price'])
        else:
            prices.append(item['unitprice'])
    if len(prices) == 0:
        return special
    final_price = min(prices) * amount

    return final_price


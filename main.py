from API_functions.spoonacular_api import find_recipes
from Menu_ADT.menu_adt import Menu
from functions.product_price import price_product


def main(ing):
    find_recipes(ing)
    main_dish = Menu('../API_functions/json_files/data.json')
    products = main_dish.get_products()
    images = main_dish.get_image()
    recipes = main_dish.get_instructions()
    prices = dict()
    result = {}
    for key, value in products.items():

        price = []
        current = value._head
        while current is not None:
            price.append(price_product(current))
            current = current.next
        price = sum(price)
        prices[key] = round(price, 2)
    for key in prices:
        result[key] = prices[key], images[key], recipes[key]
    return result


if __name__ == '__main__':
    print(main(['pork', 'potato', 'fries']))

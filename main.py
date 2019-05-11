from spoonacular_api import find_recipes
from menu_adt import Menu
from product_price import price_product

ing = [input() for i in range(3)]
find_recipes(ing)
main_dish = Menu('data.json')
products = main_dish.get_products()
prices = dict()
for key, value in products.items():
    price = []
    current = value._head
    while current is not None:
        price.append(price_product(current))
        current = current.next
    price = sum(price)
    prices[key] = price

if __name__ == '__main__':
    print(prices)

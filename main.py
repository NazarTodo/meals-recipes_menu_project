from API_functions.spoonacular_api import find_recipes
from Menu_ADT.menu_adt import Menu
from functions.product_price import price_product

ing = [input("Enter an ingredient:\n") for i in range(3)]
find_recipes(ing)
main_dish = Menu('API_functions/json_files/data.json')
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


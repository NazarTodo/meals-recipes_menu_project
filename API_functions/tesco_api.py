import json
import requests


def find_price(ing):
    """
    Makes a json file of a certain product request and writes it down
    str -> None
    """
    try:
        conn = requests.get("https://dev.tescolabs.com/grocery/products/?query={}&offset=0&limit=10".format(ing),
                            headers={'Ocp-Apim-Subscription-Key': '025b280758e043b1975d22663917204a'})
        data = conn.json()
        with open("../API_functions/json_files/products.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


import json
import requests


def find_price(ing):
    """
    Makes a json file of a certain product request and writes it down
    str -> None
    """
    try:
        conn = requests.get("https://dev.tescolabs.com/grocery/products/?query={}&offset=0&limit=10".format(ing),
                            headers={'Ocp-Apim-Subscription-Key': 'c5683c24867d481dba0a91e4025d03a0'})
        data = conn.json()
        with open("products.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


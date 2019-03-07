import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('dev.tescolabs.com')
    conn.request("GET", "/grocery/products/?query={query}&offset=0&limit=10&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read().decode()
    info = json.loads(data)
    with open("products.json", "w") as file:
        json.dump(info, file, indent=4, separators=(',', ': '))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

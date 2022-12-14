import requests

website_address = "129.159.151.65:8080"
response = requests.get('http://129.159.151.65:8080')

print(response.status_code)

if response.ok == "200":
    print("Success")
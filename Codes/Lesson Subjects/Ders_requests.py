import requests

a= 20
b = a + 20
response =  requests.get('https://api.github.com')


print(response)

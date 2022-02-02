# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chugtai, Tony Le, Shekar Balasubramaniam

# Links below indicate help found online

# import requests package
import requests
# requests the web adress 
r = requests.get('https://www.charlotte.edu/')
# prints the request
print(r.text)

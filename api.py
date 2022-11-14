import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = 'KZT'
currency_2 = 'USD'
amount = '1000'

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "8daf4e43e0msh92d871d190888c5p1cefddjsn415251d90377",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
converted_amount = data['result']['convertedAmount']
formatted = '{:,.2f}'.format(converted_amount)

print(converted_amount, formatted)
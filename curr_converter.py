import requests
url = "https://api.exchangerate-api.com/v4/latest/USD"
request = requests.get(url)
rate = request.json()['rates']

amount = float(input('Enter your Amount in USD: '))
curr = input('Enter the code of Currency: ').upper()

if curr in rate:
    print(f"{amount} USD = {amount * rate[curr]} {curr}")
else:
    print('Not Avaliable right Now')
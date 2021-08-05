from django.shortcuts import render
import investpy
from .models import BitcoinData

# Create your views here.
def home(request):
    data = investpy.get_crypto_historical_data(crypto='bitcoin',
                                               from_date='01/01/2014',
                                               to_date='01/01/2019')

    return render(request,'index.html',{'data': data} )

def bitcoin(request):
	import requests
	import json

	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH&tsyms=USD")
	price = json.loads(price_request.content)

	# Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'bitcoin.html', {'api': api, 'price': price})


def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})


	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'notfound': notfound})

def bit(request):

    bit=BitcoinData()
    bit.name = 'Bitcoin'
    bit.high_24 = '23.3'

    return render(request, 'bit.html', {'name' : bit.name})

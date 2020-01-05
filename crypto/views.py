from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP,BTC,BCH,ETH,EOS,XLM,LTC&tsyms=USD,INR")
    price=json.loads(price_request.content)
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request,'home.html',{"api":api,"price":price})

def prices(request):
    if request.method =="POST":
        quote=request.POST['quote']
        quote=quote.upper()
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD,INR")
        crypto=json.loads(crypto_request.content)
        return render(request,'prices.html',{"quote":quote,"crypto":crypto})
    else:
        msg="please enter price"
        return render(request,'prices.html',{"msg":msg})



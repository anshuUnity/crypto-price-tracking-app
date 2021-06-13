from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.


def indexView(request):
    data_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    raw_data = requests.get(data_url).json()

    return render(request, 'crypto/index.html', context={'datas': raw_data})

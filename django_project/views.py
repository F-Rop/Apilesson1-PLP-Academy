from django.http import response
import requests
from django.shortcuts import render

def home(request):
    # Using API 1
    response = requests.get('https://api.kanye.rest')
    data = response.json()
    result = data["quote"]

    # Using API 2
    response2 = requests.get('https://randomfox.ca/floof/')
    data2 = response2.json()
    result2 = data2["image"]

    return render(request, 'Templates/index.html', {'result': result, 'result2': result2})

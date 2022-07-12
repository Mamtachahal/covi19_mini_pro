from ast import Global
from urllib import response
from django.shortcuts import render
from pytz import country_names
import requests
# Create your views here.

def  home(request):
    response = None
    data = True
    globaldata = None
    countries = None
    while(data):
        try:
            response=requests.get('https://api.covid19api.com/summary')
            json= response.json()
            globaldata = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    return render(request ,'home.html',{'globaldata':globaldata , 'country':countries})
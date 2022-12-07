from django.shortcuts import render, HttpResponse
import json, requests
from booksStore.models import Books

def index(request):
    url = 'https://run.mocky.io/v3/821d47eb-b962-4a30-9231-e54479f1fbdf'
    r = requests.get(url).json()
    
    for obj in r['items']:
        Books.objects.create(title = obj['volumeInfo']['title'])

    
    return HttpResponse("Data Saved")


   
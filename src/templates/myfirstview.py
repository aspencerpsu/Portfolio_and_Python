# from django.http import HttpResponse
from django.shortcuts import render_to_response

def sometext(request):
    return render_to_response('samplehtml.html', {'owner': 'Akeem Warner', 'books': 'The Kiterunner', 'author': 'Khaled Hosseini'})
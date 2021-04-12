from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def book(request):
    if request.method == "POST":
        #this is dictionary of python to get the values using key.
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        email = request.POST['email']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']

        # printing at console to check wheather we are getting value from book.html
        # print(name +" Email "+ email)
        # printing at console if users submit.
        # print("This is posted")
    return render(request, 'book.html')

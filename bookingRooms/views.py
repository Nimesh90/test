from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, HttpResponse
from bookingRooms.models import Book
# Create your views here.


def home(request):
    return render(request, 'home.html')


def book(request):
    if request.method == "POST":
        # this is dictionary of python to get the values using key.
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        email = request.POST['email']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        form = Book(name=name, phone=phone, description=description,
                    email=email, startDate=startDate, endDate=endDate)
        # to save on database.
        form.save()
        print("The data has been written")
        # printing at console to check wheather we are getting value from book.html
        # print(name +" Email "+ email)
        # printing at console if users submit.
        # print("This is posted")
    return render(request, 'book.html')

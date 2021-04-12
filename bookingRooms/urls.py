from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from bookingRooms import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book',views.book,name='book')
    #if someone comes for request hand that request to bookingRooms.urls.
]
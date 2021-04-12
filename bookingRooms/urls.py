from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from bookingRooms import views

#heading of dashboard of admin page
admin.site.site_header = "Welcome to Hotel Booking System"
#title of webpage.
admin.site.index_title = "log In"

urlpatterns = [
    path('',views.home,name='home'),
    path('book',views.book,name='book')
    #if someone comes for request hand that request to bookingRooms.urls.
]
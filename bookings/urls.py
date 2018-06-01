from django.urls import path

from . import views
from .views import view_bookings, EditBooking, delete_booking

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bookings_list/', view_bookings, name='bookings_list'),
    path('<int:pk>/EditBookings/', EditBooking.as_view(), name="view_bookings"),
    path('<int:pk>/delete_booking/', delete_booking.as_view(), name="delete_booking")
   #path('<int:pk>/EditPackages/', EditPackage.as_view(), name="EditPackage")
]
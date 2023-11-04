from django.urls import path
from .import views 
urlpatterns = [
  path('', views.appointments_main, name='appointments_main'),
  path('createappointment',views.appointment_create, name='createappointment'),

]
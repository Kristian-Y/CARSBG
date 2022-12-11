from django.urls import path
from CARSBG.services import views

urlpatterns = [
    path('', views.services_types, name='services'),
    path('create-car-service/', views.CreateCarService.as_view(), name='create-car-service'),

]

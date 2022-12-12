from django.urls import path
from CARSBG.services import views

urlpatterns = [
    path('', views.services_types, name='services'),
    path('create-car-service/', views.CreateCarService.as_view(), name='create-car-service'),
    path('car-services-posts/', views.CarServicesPost.as_view(), name='car-services-posts'),
    path('rent-a-car-posts/', views.RentACarPosts.as_view(), name='rent-a-car-posts')
]

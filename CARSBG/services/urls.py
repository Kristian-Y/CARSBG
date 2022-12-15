from django.urls import path
from CARSBG.services import views

urlpatterns = [
    path('', views.services_types, name='services'),
    path('create-car-service/', views.CreateCarService.as_view(), name='create-car-service'),
    path('create-rent-a-car/', views.CreateRentACar.as_view(), name='create-rent-a-car'),
    path('car-services-posts/', views.CarServicesPost.as_view(), name='car-services-posts'),
    path('rent-a-car-posts/', views.RentACarPosts.as_view(), name='rent-a-car-posts'),
    path('car-service-details/<str:pk>', views.CarServiceDetails.as_view(), name='car-service-details'),
    path('rent-a-car-details/<str:pk>', views.RentACarDetails.as_view(), name='rent-a-car-details'),
    path('car-service-delete/<str:pk>', views.CarServiceDelete.as_view(), name='car-service-delete'),
    path('rent-a-car-delete/<str:pk>', views.RentACarDelete.as_view(), name='rent-a-car-delete'),
    path('car-service-edit/<str:pk>', views.CarServiceEdit.as_view(), name='car-service-edit'),
    path('rent-a-car-edit/<str:pk>', views.RentACarEdit.as_view(), name='rent-a-car-edit')
]

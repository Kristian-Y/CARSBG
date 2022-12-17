from django.urls import path
from CARSBG.cars import views

urlpatterns = [
    path('catalogue/', views.Catalogue.as_view(), name='catalogue'),
    path('create-car-advert/', views.CreateCarAdvert.as_view(), name='create-car-advert'),
    path('advert/', views.advert, name='advert'),
    path('my-cars', views.MyCars.as_view(), name='my-cars'),
    path('car-details/<str:pk>', views.CarDetails.as_view(), name='car details'),
    path('car-delete/<str:pk>', views.CarDelete.as_view(), name='car-delete'),
    path('car-edit/<str:pk>', views.CarEdit.as_view(), name='car-edit')
]

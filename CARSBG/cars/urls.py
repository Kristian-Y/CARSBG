from django.urls import path
from CARSBG.cars import views

urlpatterns = [
    path('catalogue/', views.Catalogue.as_view(), name='catalogue'),
    path('create-car-advert/', views.CreateCarAdvert.as_view(), name='create-car-advert'),
    path('advert/', views.advert, name='advert'),
]

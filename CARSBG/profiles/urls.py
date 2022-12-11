from django.urls import path
from CARSBG.profiles import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile-details/<str:pk>', views.ProfileDetails.as_view(), name='profile-details'),
    path('profile-edit/<str:pk>', views.ProfileEdit.as_view(), name='profile-edit'),
    path('profile-delete/<str:pk>', views.DeleteProfile.as_view(), name='profile-delete'),
    path('profile-logout/', views.LogOutView.as_view(), name='logout')
]

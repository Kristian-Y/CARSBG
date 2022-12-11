from django.urls import path
from CARSBG.chat import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
    path('send_message/', views.SendMessageView.as_view(), name='send_message'),
]

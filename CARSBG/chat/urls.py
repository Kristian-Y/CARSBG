from django.urls import path
from CARSBG.chat import views

urlpatterns = [
    path('', views.Chats.as_view(), name='chat'),
    path('send_message/<str:pk>', views.SendMessageView.as_view(), name='send_message'),
]

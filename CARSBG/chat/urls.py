from django.urls import path
from CARSBG.chat import views

urlpatterns = [
    path('', views.Chats.as_view(), name='chat'),
    path('send_message/<str:pk>', views.SendMessageView.as_view(), name='send_message'),
    path('open-chat/<str:pk>', views.OpenChatFromProfileDetails.as_view(), name='open-chat')
]

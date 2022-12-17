from django.contrib import admin

from CARSBG.chat.models import ChatRoom, Message


# Register your models here.

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_filter = ("id",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "text", "chat_room", "timestamp")
    list_filter = ("id", "sender", "timestamp",)

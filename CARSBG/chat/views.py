from django.contrib.auth import get_user_model
from django.views.generic import View
from django.shortcuts import render, redirect
from CARSBG.chat.models import Message, ChatRoom

# Create your views here.

User = get_user_model()


class ChatView(View):
    def get(self, request):
        # Get the user from the session
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        # Query the database to get the list of chat rooms
        chat_rooms = ChatRoom.objects.all()

        # Query the database to get the list of messages for the selected chat room


        # Render the chat page
        return render(request, 'chat/chat.html', {'user': user, 'chat_rooms': chat_rooms, 'messages': messages,
                                                  'selected_chat_room': selected_chat_room})


class Chats(View):
    def get(self, request):
        request_user = User.objects.get(id=request.user.id)
        chats = []

        for chat in ChatRoom.objects.all():
            for user in chat.users.all():
                if user == request_user:
                    chats.append([chat, chat.name.split('-')])

        # Query the database to get the list of messages for the selected chat room
        selected_chat_room = ''
        for i in request.GET.items():
            selected_chat_room = i[1]

        if selected_chat_room is not None:
            try:
                selected_chat_room = ChatRoom.objects.get(name=selected_chat_room)
            except ChatRoom.DoesNotExist:
                selected_chat_room = None

            messages = Message.objects.filter(chat_room=selected_chat_room)
        else:
            selected_chat_room = None
            messages = []

        print(chats[0][1])
        context = {
            'chats': chats,
            'messages': list(messages),
            'selected_chat_room': selected_chat_room
        }

        return render(request, 'chat/chat.html', context)


class SendMessageView(View):
    def post(self, request, pk):
        # Get the user from the session
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        # Get the text of the message from the request
        text = request.POST['message']

        # Get the selected chat room
        print(request.POST)
        selected_chat_room = pk
        if selected_chat_room is not None:
            try:
                selected_chat_room = ChatRoom.objects.get(name=selected_chat_room)
            except ChatRoom.DoesNotExist:
                selected_chat_room = None
        else:
            selected_chat_room = None

        # Create a new message and add it to the database
        if selected_chat_room is not None:
            message = Message(sender=user, text=text, chat_room=selected_chat_room)
            message.save()

        # Redirect back to the chat page
        return redirect('chat')


class OpenChatFromProfileDetails(View):
    def get(self, request, pk):
        chats = ChatRoom.objects.all()
        second_user = User.objects.get(id=pk)

        print(second_user)

        for chat in chats:
            if chat.name == request.user.username + '-' + second_user.username or chat.name == second_user.username + '-' + request.user.username:
                return redirect('chat')

        chat_name = request.user.username + '-' + second_user.username

        created_chat_room = ChatRoom.objects.create(name=chat_name)
        created_chat_room.users.add(request.user)
        created_chat_room.users.add(second_user)
        return redirect('chat')

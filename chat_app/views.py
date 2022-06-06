# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatModel
from bulletin_board.models import Users


def chat_page(request, username):
    user_obj = Users.objects.get(username=username)

    if request.user.slug > user_obj.slug:
        thread_name = f'chat_{request.user.slug}-{user_obj.slug}'
    else:
        thread_name = f'chat_{user_obj.slug}-{request.user.slug}'

    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    context = {
        'user': user_obj,
        'messages': message_objs
    }
    return render(request, template_name='chat_app/room.html', context=context )
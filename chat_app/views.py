from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatModel
from bulletin_board.models import Users
from bulletin_board.utils import MENU


def searching_people_in_thread(request):
    messages = ChatModel.objects.filter(thread_name__icontains=request.user)
    list_with_names = []
    for i in messages:
        user = [x for x in i.thread_name.split('-') if x not in ('chat', str(request.user).lower())]
        user_obj = Users.objects.get(username__icontains=user[0])
        if user_obj not in list_with_names:
            list_with_names.append(user_obj)
    return list_with_names


@login_required
def chat_page(request, username):
    user_obj = Users.objects.get(username=username)

    if request.user.slug > user_obj.slug:
        thread_name = f'chat-{request.user.slug}-{user_obj.slug}'
    else:
        thread_name = f'chat-{user_obj.slug}-{request.user.slug}'

    message_objs = ChatModel.objects.filter(thread_name=thread_name).select_related('sender')
    list_with_names = searching_people_in_thread(request)
    if username == request.user.username:
        context = {
            'menu': MENU,
            'message': "You can't text yourself"
        }
    else:
        context = {
            'receiver': user_obj,
            'messages': message_objs,
            'menu': MENU,
            'users': list_with_names,
        }
    return render(request, template_name='chat_app/chat.html', context=context)


# Duplicated SQL queries
@login_required
def all_messages(request):
    list_with_names = searching_people_in_thread(request)
    if len(list_with_names) == 0:
        context = {
            'menu': MENU,
            'users': list_with_names,
            'message': 'There are no messages yet...  Text someone!',
            'title': 'My messages'
        }
    else:
        context = {
            'menu': MENU,
            'users': list_with_names,
            'title': 'My messages'
        }
    return render(request, template_name='chat_app/messages.html', context=context)

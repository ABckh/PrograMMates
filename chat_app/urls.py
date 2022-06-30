from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', all_messages, name='messages'),
    path('<str:username>/', chat_page, name='chat'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:username>/', chat_page, name='chat')

]
from django.contrib.auth.models import User

MENU = [
    {'title': 'Find a teammate', 'url_name': 'index'},
    {'title': 'Add an advert', 'url_name': 'adding'},
    {'title': 'My profile', 'url_name': 'profile'},
    {'title': 'My adverts', 'url_name': 'adverts'},
    {'title': 'My messages', 'url_name': 'messages'},
    {'title': 'Contact service', 'url_name': 'service'},
]

MENU_FOR_NEW_USERS = [
    {'title': 'Find a teammate', 'url_name': 'index'},
    {'title': 'Add an advert', 'url_name': 'registration'},
    {'title': 'Contact service', 'url_name': 'service'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        if self.request.user.is_authenticated:
            context = kwargs
            context['menu'] = MENU
            return context
        else:
            context = kwargs
            context['menu'] = MENU_FOR_NEW_USERS
            return context

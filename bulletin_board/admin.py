from django.contrib import admin
from .models import Users, Advert
from .forms import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username',)
    search_fields = ('username', 'dat_of_pub')
    prepopulated_fields = {'slug': ('username', )}


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username')
    list_display_links = ('id', 'title', 'username')
    search_fields = ('title', 'username')
    prepopulated_fields = {'slug': ('description',)}
    date_hierarchy = 'dat_of_pub'


admin.site.register(Users, UsersAdmin)
admin.site.register(Advert, AdvertAdmin)

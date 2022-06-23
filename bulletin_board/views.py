from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from .forms import *
from .models import Advert, Users
from .utils import DataMixin, MENU
from .filters import AdvertFilter


class StartPageView(DataMixin, generic.ListView):
    template_name = 'bulletin_board/board.html'
    model = Advert
    context_object_name = 'adverts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        ad_filters = AdvertFilter(self.request.GET, queryset)
        # user_filters = UserFilter(self.request.GET, queryset)
        # print(dict(list(context.items()) + list(c_def.items())))
        adverts = self.get_queryset()
        list_length = [x for x in adverts]
        if len(list_length) == 0:
            c_def = self.get_user_context(title='Programmates', ad_filters=ad_filters,
                                          message='Oops, nothing was found.',
                                          message_2='Please, try changing the values in the '
                                                    'filters or add your own advert.')
        else:
            c_def = self.get_user_context(title='Programmates', ad_filters=ad_filters)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        adverts = Advert.objects.all().select_related('username')
        my_filter = AdvertFilter(self.request.GET, queryset=adverts)
        adverts = my_filter.qs
        return adverts


# class DetailView(DataMixin, generic.DetailView):
#     model = Advert
#     template_name = "bulletin_board/detail.html"
#     context_object_name = "ad"
#     slug_url_kwarg = 'ad_slug'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Programmates')
#         return dict(list(context.items()) + list(c_def.items()))


class AddingView(LoginRequiredMixin, DataMixin, generic.CreateView):
    form_class = AddAdvertForm
    template_name = "bulletin_board/adding.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Adding new advert')
        return dict(list(context.items()) + list(c_def.items()))


class UserProfileView(LoginRequiredMixin, DataMixin, generic.DetailView):
    model = Users
    template_name = "bulletin_board/profile.html"
    context_object_name = 'user'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.slug == self.kwargs['user_slug']:
            c_def = self.get_user_context(title='Profile')
        else:
            c_def = self.get_user_context(title='Profile', message="Oops... You don't have permission for this")
        return dict(list(context.items()) + list(c_def.items()))


class AboutUserView(DataMixin, generic.DetailView):
    model = Users
    template_name = "bulletin_board/about_user.html"
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Programmates')
        return dict(list(context.items()) + list(c_def.items()))

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.slug == self.kwargs['user_slug']:
            return redirect(f'/profile/{self.request.user.slug}/')
        else:
            # username = Users.objects.get(slug=self.kwargs['user_slug'])
            adverts = Advert.objects.filter(username__slug=self.kwargs['user_slug']).select_related('username')
            for ad in adverts:
                user = ad.username
            my_context = {
                'adverts': adverts,
                'menu': MENU,
                'user': user,
            }
            return render(request=self.request, template_name=self.template_name, context=my_context)


class UserRegistrationView(DataMixin, generic.CreateView):
    model = Users
    template_name = 'bulletin_board/registration.html'
    form_class = UserRegistrationForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LogInView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'bulletin_board/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Log in')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class ContactService(DataMixin, generic.FormView):
    form_class = ContactServiceForm
    template_name = 'bulletin_board/contact_service.html'
    success_url = reverse_lazy('service')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Contact Service', )
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        message_name = self.request.POST['name']
        message = self.request.POST['message']
        email = self.request.POST['email']
        send_mail(
            subject=message_name + ' ' + email,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
        context = self.get_context_data(message_name=self.request.POST['name'])
        return render(self.request, self.template_name, context=context)


class PageNotFoundView(generic.TemplateView):
    template_name = 'bulletin_board/404.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='404', )
        return dict(list(context.items()) + list(c_def.items()))


class UserAdverts(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'bulletin_board/user_adverts.html'
    model = Advert
    paginate_by = 5
    context_object_name = 'adverts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = self.get_queryset()
        list_length = [x for x in adverts]
        if len(list_length) == 0:
            c_def = self.get_user_context(title="User's adverts",
                                          message='Oops, nothing was found.',
                                          message_2='Try to add your own adverts!')
        else:
            c_def = self.get_user_context(title="User's adverts")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Advert.objects.filter(username=self.request.user).select_related('username')


class DeleteAdvert(LoginRequiredMixin, DataMixin, generic.DeleteView):
    model = Advert
    success_url = reverse_lazy('index')
    slug_url_kwarg = 'ad_slug'
    template_name = 'bulletin_board/delete.html'
    context_object_name = 'ad'

    # SQL queries duplacates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = Advert.objects.all().select_related('username')
        if self.request.user == adverts.get(slug=self.kwargs['ad_slug']).username:
            c_def = self.get_user_context(title='My adverts')
        else:
            c_def = self.get_user_context(title='My adverts', message="Oops... You don't have permission to this page")
        return dict(list(context.items()) + list(c_def.items()))
    #
    # def get_context_object_name(self, obj):
    #     all_adverts = Advert.objects.all().select_related('username')
    #     ad = all_adverts.get(username=self.request.user)
    #     print(str(ad))
    #     return 'advert'


class EditAdvert(LoginRequiredMixin, DataMixin, generic.UpdateView):
    model = Advert
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    slug_url_kwarg = 'ad_slug'

    def get_success_url(self):
        return reverse_lazy('adverts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.kwargs['ad_slug']:
        adverts = Advert.objects.all().select_related('username')
        if self.request.user == adverts.get(slug=self.kwargs['ad_slug']).username:
            c_def = self.get_user_context(title='Edit')
        else:
            c_def = self.get_user_context(title='Edit', message="Oops... You don't have permission to this page")

        return dict(list(context.items()) + list(c_def.items()))


class EditProfile(LoginRequiredMixin, DataMixin, generic.UpdateView):
    model = Users
    fields = ['username', 'email', 'information', 'language', 'gender', 'photo']
    template_name_suffix = '_update_form'
    slug_url_kwarg = 'user_slug'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.slug == self.kwargs['user_slug']:
            c_def = self.get_user_context(title='Edit')
        else:
            c_def = self.get_user_context(title='Edit', message="Oops... You don't have permission to this page")
        return dict(list(context.items()) + list(c_def.items()))




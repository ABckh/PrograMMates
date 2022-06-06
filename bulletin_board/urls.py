from django.urls import path
from . import views
urlpatterns = [
    path('', views.StartPageView.as_view(), name='index'),
    path('add_ad/', views.AddingView.as_view(), name='adding'),
    path('profile/<slug:user_slug>/', views.UserProfileView.as_view(), name='profile'),
    path('service/', views.ContactService.as_view(), name='service'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('logout/', views.logout_user, name='logout'),
    path('my_adverts/', views.UserAdverts.as_view(), name='adverts'),
    # path('<slug:ad_slug>/', views.DetailView.as_view(), name='details'),
    path('about_user/<slug:user_slug>/', views.AboutUserView.as_view(), name='about_user'),
    path('delete/<slug:ad_slug>/', views.DeleteAdvert.as_view(), name='delete_advert'),
    path('edit/<slug:ad_slug>/', views.EditAdvert.as_view(), name='edit_advert'),
    path('edit_user/<slug:user_slug>/', views.EditProfile.as_view(), name='edit_profile'),
]

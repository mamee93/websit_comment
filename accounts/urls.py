from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [

    path('profile',views.profile,name='profile'),
    path('signup',views.signup,name='signup'),
    path('<str:slug>/edit', views.edit_profile, name='edit_profile'),
]
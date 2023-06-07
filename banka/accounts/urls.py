from django.urls import path
from .views import *
from . import views

app_name = 'accounts'

urlpatterns = [
    #path(url ismi, çalışacak view'ın ismi)
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
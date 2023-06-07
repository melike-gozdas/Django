from django.urls import path
from .views import *
from . import views

app_name = 'data'

urlpatterns = [
    #path(url ismi, çalışacak view'ın ismi)
    path('index/', data_index, name='index'),
    #path('detail/', data_detail),
    path('<int:CustomerId>/', data_detail, name='detail'),
    path('create/', data_create, name='create'),
    path('<int:CustomerId>/update/', data_update, name='update'),
    path('<int:CustomerId>/delete/', data_delete, name='delete'),
]


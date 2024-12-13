from django.urls import path
from app.views import *

app_name='front'
urlpatterns=[
    path('front/',front,name='front'),
]
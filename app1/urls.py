from django.urls import path
from app1.views import *

app_name='back'
urlpatterns=[
    path('back/',back,name='back'),
]

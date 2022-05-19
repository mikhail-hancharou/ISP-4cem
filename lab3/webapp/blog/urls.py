from django.urls import path
from .views import *  # import all our views


urlpatterns = [  # set urls to our views here
    path('', blog),
]

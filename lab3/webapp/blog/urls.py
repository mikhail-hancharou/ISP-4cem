from django.urls import path
from .views import *  # import all our views


urlpatterns = [  # set urls to our views here
    path('', blog, name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('', blog, name='post_new'),
    path('', blog, name='signup'),
    path('', blog, name='login'),
]

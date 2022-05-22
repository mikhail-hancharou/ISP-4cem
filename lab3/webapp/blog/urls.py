from django.urls import path
from .views import *  # import all our views


urlpatterns = [  # set urls to our views here
    path('', BlogListView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('new-post/', BlogCreateView.as_view(), name='post_new'),
    path('', blog, name='login'),
    path('', blog, name='logout'),
    path('category/<str:category>/', CategoryPostList.as_view(), name='posts_by_category'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
]

from django.urls import path
from .views import *  # import all our views


urlpatterns = [  # set urls to our views here
    path('', BlogListView.as_view(), name='home'),
    path('new-post/', BlogCreateView.as_view(), name='post_new'),
    path('category/<str:category>/', CategoryPostList.as_view(), name='posts_by_category'),
    path('home/', MyPostsList.as_view(), name='my_posts'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
]

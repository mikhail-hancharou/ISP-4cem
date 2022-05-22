from django.urls import path
from .views import SignUpView, logout_user

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
]

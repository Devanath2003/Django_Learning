from django.urls import path
from .views import create_user,get_users, get_user

urlpatterns = [
    path("users", create_user),
    path("users/all", get_users),
    path("users/<int:user_id>", get_user)
]

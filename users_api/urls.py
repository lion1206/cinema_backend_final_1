from django.urls import path
from .views import user_list, user_register, admin_register

urlpatterns = [
    path('users/', user_list),
    path('users/register/', user_register),
    path('users/register_admin/', admin_register),
]

from django.urls import path
from .views import login_user, logout_user

# app_name="members"

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
]

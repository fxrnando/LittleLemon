from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api_token_auth/', obtain_auth_token),
]

from django.contrib import admin
from django.urls import path, include

from .views import user_view, user_register_view

urlpatterns = [
    path('register/', user_register_view),
    path('operations/', user_view),
]


from django.contrib import admin
from django.urls import path, include

from .views import user_view
urlpatterns = [
    path('operations/',user_view ),
]

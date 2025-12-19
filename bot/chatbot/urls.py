from django.urls import path
from .views import chat_api, index

urlpatterns = [
    path("", index),
    path("chat/", chat_api),
    ]
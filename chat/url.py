from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_page, name="chat-page"),
    path("send/", views.send_message, name="send-message"),
    path("get/", views.get_messages, name="get-messages"),
]

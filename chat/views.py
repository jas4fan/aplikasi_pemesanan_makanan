from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chat_page(request):
    return render(request, "chat/chat.html")

def send_message(request):
    username = request.POST.get("username")
    text = request.POST.get("text")
    Message.objects.create(username=username, text=text)
    return JsonResponse({"status": "success"})

def get_messages(request):
    messages = Message.objects.order_by("-timestamp")[:20]
    data = [
        {
            "username": msg.username,
            "text": msg.text,
            "timestamp": msg.timestamp.strftime("%H:%M")
        }
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

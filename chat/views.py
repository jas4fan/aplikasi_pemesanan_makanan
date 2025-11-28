from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chat_page(request):
    # template ada di chat/templates/chat.html -> render "chat.html"
    return render(request, "chat.html")

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

# alias supaya urls.py tetap pakai views.index
def index(request):
    return chat_page(request)

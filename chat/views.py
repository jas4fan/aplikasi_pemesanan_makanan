from django.shortcuts import render
from .chat_oop import ChatUser, ChatSystem

# Buat sistem chat
chat_sys = ChatSystem()

# Buat user
customer = ChatUser("Budi", "Customer")
driver = ChatUser("Andi", "Driver")
restaurant = ChatUser("Restoran Maju", "Restaurant")
admin = ChatUser("Admin Pusat", "Admin")

# Tambah user ke sistem
for u in [customer, driver, restaurant, admin]:
    chat_sys.add_user(u)


def chat_view(request):
    if request.method == "POST":
        sender_name = request.POST.get("sender")
        receiver_name = request.POST.get("receiver")
        message = request.POST.get("message")

        sender = chat_sys.get_user(sender_name)
        receiver = chat_sys.get_user(receiver_name)

        if sender and receiver:
            sender.send(receiver, message)

    context = {
        "users": chat_sys.users
    }
    return render(request, "chat/chat.html", context)

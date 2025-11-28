from chat_user import User
from message import Message
from chat_service import ChatService

# Membuat user sesuai subsistem GoFood
customer = User(1, "Budi", "Customer")
restaurant = User(2, "Restoran Maju", "Restaurant")
driver = User(3, "Andi", "Driver")
admin = User(4, "Admin Pusat", "Admin")

# Membuat layanan chat
chat = ChatService()

# Contoh chat
m1 = Message(customer, restaurant, "Halo, apakah pesanan saya sudah diproses?")
chat.send_message(m1)

m2 = Message(restaurant, customer, "Sudah ya kak, dalam tahap persiapan.")
chat.send_message(m2)

m3 = Message(customer, driver, "Bang, sudah sampai mana?")
chat.send_message(m3)

m4 = Message(driver, customer, "OTW kak!")
chat.send_message(m4)

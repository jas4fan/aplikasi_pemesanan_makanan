🍽️ Aplikasi Pemesanan Makanan (Food Ordering Application)
Aplikasi ini merupakan sistem pemesanan makanan online yang menghubungkan Pelanggan (Customer), Restoran (Restaurant), Pengemudi (Driver), dan memiliki panel Admin.

✨ Fitur Utama (Core Features)
Aplikasi ini memiliki lima komponen utama yang diakses melalui modul/folder yang berbeda:
1. adminpanel (Oleh Iqbal): Panel kontrol untuk mengelola data master dan memantau operasional aplikasi secara keseluruhan.

2. customer (Oleh Amel): Antarmuka yang digunakan Pelanggan untuk menjelajah, memesan, dan melacak pesanan.

3. driver (Oleh Afiq): Antarmuka yang digunakan Pengemudi untuk menerima, melihat detail, dan mengonfirmasi pengiriman pesanan.

4. restaurant (Oleh Zaky): Antarmuka yang digunakan Restoran untuk mengelola menu, menerima pesanan, dan mengelola profil restoran.

5. chat (Oleh Marcellino): Fitur komunikasi real-time antara pihak-pihak terkait (misalnya, Pelanggan - Restoran, Pelanggan - Pengemudi).

💾 Struktur Data dan Entitas (CRUD & Attributes)
Berikut adalah daftar entitas utama yang perlu diimplementasikan, lengkap dengan operasi CRUD (Create, Read, Update, Delete) yang diperlukan dan atribut kuncinya.
1. Entitas Pengguna (Users)
 <img width="931" height="399" alt="image" src="https://github.com/user-attachments/assets/be5ae3c0-4080-4e86-a887-82d268edbcb8" />

2. Entitas Restoran dan Makanan (Restaurant & Food)
 <img width="892" height="335" alt="image" src="https://github.com/user-attachments/assets/067ed0b4-0cb2-44f7-86c6-94980fcec9cf" />

3. Entitas Transaksi (Transaction)
 <img width="888" height="362" alt="image" src="https://github.com/user-attachments/assets/ebec4785-a657-4041-a0d7-caf39bf4db29" />

🧑‍💻 Pembagian Tugas dan Struktur Repositori
Setiap anggota tim bertanggung jawab penuh atas folder/modul dan branch yang telah ditentukan:

 <img width="903" height="563" alt="image" src="https://github.com/user-attachments/assets/377d6502-ec7a-44d1-a61a-bcbe549ab9c2" />

File Utama Lainnya yang Harus Ada
- README.md (Anda sedang membacanya): Dokumentasi proyek.
- manage.py: Berkas utama untuk menjalankan proyek Django.
- requirements.txt: Berkas yang mencantumkan semua dependensi Python yang dibutuhkan proyek (misalnya, Django, Pillow, dll.).
- urls.py: Berkas konfigurasi routing URL utama untuk proyek.
- .gitignore: Berkas untuk mengabaikan file dan folder yang tidak perlu diunggah ke Git (misalnya, virtual environment, cache, database lokal).
- foodsystem (Root folder proyek/settings): Berkas konfigurasi utama (settings.py, urls.py utama, wsgi.py, asgi.py).

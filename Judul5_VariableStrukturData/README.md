<img width="1224" height="791" alt="Screenshot 2026-05-25 222753" src="https://github.com/user-attachments/assets/4e1fe284-b8fb-4375-9d84-08cdc8eebacb" />
<img width="1225" height="772" alt="Screenshot 2026-05-25 222813" src="https://github.com/user-attachments/assets/08a5a50f-948c-4118-a3e2-d85f33426d5d" />
<img width="1223" height="440" alt="Screenshot 2026-05-25 222836" src="https://github.com/user-attachments/assets/0a94fc66-13be-4df2-ba87-5ac48aea64a4" />
<img width="1219" height="859" alt="Screenshot 2026-05-25 222903" src="https://github.com/user-attachments/assets/143eed78-8a79-413c-8b2f-1941e2f59bc8" />

Program ini adalah sebuah aplikasi simulasi Sistem Validasi Tiket Konser berbasis teks (CLI) yang menggunakan struktur data Binary Search Tree (BST). Tujuan utama dari sistem ini adalah untuk mengelola penyimpanan data nomor seri tiket resmi (Insert) dan melakukan verifikasi instan apakah tiket yang dibawa oleh penonton asli atau palsu (Search).

Struktur utama pencarian biner yang memiliki aturan: nomor seri tiket di sebelah kiri selalu lebih kecil dari induknya, dan di sebelah kanan selalu lebih besar. Hal ini membuat proses pencarian tiket berjalan sangat cepat karena sistem tidak perlu mengecek seluruh data satu per satu, melainkan langsung membelah jalur pencarian menjadi dua (divide and conquer).

**Penjelasan Alur Main Menu Program**
1. Register ID Baru (Pilihan 1): Memasukkan nomor seri tiket resmi yang baru terjual ke dalam database BST.
2. Validasi Tiket (Pilihan 2): Mengecek nomor tiket penonton di pintu masuk. Jika ditemukan di dalam pohon BST, tiket dinyatakan Valid (Asli). Jika tidak ditemukan, dinyatakan Palsu atau Belum Terdaftar.
3. Cetak Urut (Pilihan 3): Menggunakan metode Inorder Traversal untuk menampilkan semua nomor tiket yang terdaftar dari angka terkecil hingga terbesar secara otomatis.
4. Preorder & Postorder (Pilihan 4 & 5): Menampilkan struktur pemetaan data tiket di dalam memori berdasarkan urutan Root-Kiri-Kanan dan Kiri-Kanan-Root.
5. Lihat Nomor Seri Terkecil & Terbesar (Pilihan 6 & 7): Menemukan nomor seri tiket paling ujung (paling kiri untuk nilai minimum, paling kanan untuk nilai maksimum).
6. Hitung Total Tiket Terjual (Pilihan 8): Menghitung berapa banyak tiket resmi yang sudah terdaftar di dalam sistem secara real-time.
7. Total Nilai (Pilihan 9): Menjumlahkan seluruh angka nomor seri tiket (biasanya digunakan untuk keperluan validasi total kecocokan data internal).
8. Keluar (Pilihan 10): Menghentikan perulangan while loop dan menutup aplikasi keamanan tiket.

Video Youtube: https://youtu.be/cxzow2opr58

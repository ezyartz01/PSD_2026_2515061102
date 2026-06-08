Nama Program: Sistem Rak Perpustakaan.

<img width="1213" height="829" alt="Screenshot 2026-06-08 225703" src="https://github.com/user-attachments/assets/c7eaadc2-b6b7-48f5-a0bb-339b1012dd8a" />
<img width="1228" height="690" alt="Screenshot 2026-06-08 225733" src="https://github.com/user-attachments/assets/772bdd7a-1418-4dcd-8b70-1137f7112a24" />
<img width="1232" height="333" alt="Screenshot 2026-06-08 225747" src="https://github.com/user-attachments/assets/05ded52a-0733-4b0c-9a58-399f977ac1ab" />

implementasi sederhana struktur data Hash Table menggunakan metode penanganan tabrakan (collision handling) Separate Chaining berbasis Linked List. Untuk memudahkan pemahaman, proyek ini menggunakan analogi dunia nyata berupa Sistem Penataan Buku di Rak Perpustakaan menggunakan bahasa pemrograman Python.

ANALOGI SISTEM
1. Hash Table (HashMapSeparateChaining): Wadah utama yang memiliki rak terbatas (pada kode ini diset sebanyak 5 rak, yaitu Rak 0 sampai Rak 4).
2. Fungsi Hash (hash_function): Aturan matematika (kode_buku % total_rak) untuk menentukan secara instan di rak nomor berapa sebuah buku harus diletakkan.
3. Node (Node): Merepresentasikan satu buku fisik yang menyimpan informasi kunci (kode_buku), nilai (judul_buku), dan tali pengikat (next) untuk menunjuk ke buku setelahnya jika terjadi penumpukan di rak yang sama.

FITUR UTAMA PROGRAM
1. insert(kode_buku, judul_buku): Memasukkan buku ke rak yang sesuai berdasarkan hasil kalkulasi fungsi hash. Jika kode buku sudah ada, sistem akan memperbarui judulnya. Jika terjadi collision (nomor rak sama), buku baru akan dirantai di posisi paling depan pada rak tersebut.
2. search(kode_buku): Mencari lokasi buku secara efisien dengan langsung melompat ke rak yang dituju, kemudian menyisir rantai buku di rak tersebut dari depan ke belakang.
3. ambil_buku(kode_buku): Menghapus data buku dari rak tanpa memutus rantai keterhubungan antara buku sebelum (prev) dan sesudahnya (current.next).
4. tampilkan_kondisi_rak(): Memvisualisasikan struktur tumpukan dan rantai buku pada setiap rak perpustakaan ke layar terminal.

<img width="1215" height="371" alt="Screenshot 2026-06-08 225759" src="https://github.com/user-attachments/assets/bf9df2c9-6cf2-4fbb-ae40-c7d69678c3bc" />

PENJELASAN OUTPUT PROGRAM
1. Kondisi Awal Rak (Proses Penempatan & Collision). Program memasukkan buku dengan kode 5, 10, 15, dan 7 ke dalam 5 rak yang tersedia.
- Buku kode 7 akan masuk ke Rak Nomor 2 karena 7 % 5 = sisa 2.
- Buku kode 5, 10, dan 15 semuanya menghasilkan sisa bagi 0 ketika di-modulo 5 (5%5=0, 10%5=0, 15%5=0). Hal ini memicu terjadinya Collision (tabrakan) di Rak Nomor 0.
- Karena menggunakan Separate Chaining, ketiga buku tersebut tidak saling menimpa, melainkan saling merantai dari depan ke belakang dengan urutan: [15 : Matematika Diskrit] -> [10 : Rekayasa Perangkat Lunak] -> [5 : Struktur Data] -> Selesai. Buku yang masuk terakhir akan selalu berada di posisi paling depan rantai rak.
2. Proses Pencarian Buku (Search). Ketika program melakukan pencarian untuk Kode Buku 10, fungsi hash langsung mengarahkan program ke Rak Nomor 0. Program kemudian menyisir rantai di rak tersebut. Karena kode 10 ditemukan di dalam rantai, program berhasil mengambil dan menampilkan judul bukunya, yaitu 'Rekayasa Perangkat Lunak'.
3. Kondisi Akhir Rak (Proses Pengambilan Buku / Penghapusan di Tengah Rantai). Program melakukan simulasi pengambilan buku dengan kode 10. Buku kode 10 berada di posisi tengah rantai Rak Nomor 0 (di antara buku kode 15 dan buku kode 5). Fungsi ambil_buku akan memutuskan tali pengikat yang menuju ke buku kode 10, lalu menyambungkan tali dari buku kode 15 langsung ke buku kode 5 (logika prev.next = current.next).

Hasil visualisasi akhir akan menunjukkan bahwa Rak Nomor 0 sekarang hanya berisi: [15 : Matematika Diskrit] -> [5 : Struktur Data] -> Selesai. Rantai data tetap tersambung dengan benar dan tidak rusak meskipun data di tengahnya telah dihapus.

Link Youtube: https://youtu.be/-7CbqtyJASE

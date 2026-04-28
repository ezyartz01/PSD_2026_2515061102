Judul Program:
Program List 1D, Sistem Nilai mahasiswa

Deskripsi Singkat:
Program Sistem Nilai Mahasiswa merupakan program berbasis Python yang digunakan untuk mengelola data nilai mahasiswa secara sederhana menggunakan struktur data array (list).
Program ini memungkinkan pengguna untuk memasukkan nilai, menampilkan seluruh data nilai, mengecek nilai mahasiswa pada urutan tertentu, serta melihat address memori dari array dan setiap elemennya.
Melalui sistem menu interaktif, pengguna dapat berinteraksi langsung dengan data sehingga program dapat digunakan sebagai simulasi pengolahan data mahasiswa dalam skala kecil.

Source Code:

<img width="459" height="155" alt="image" src="https://github.com/user-attachments/assets/2d32bb61-a44d-4f4a-af0a-b521245a0f81" />

def menu():

#Baris ini digunakan untuk mendefinisikan fungsi bernama menu.
Fungsi ini nantinya dipanggil setiap kali menu ingin ditampilkan.

print("\n ----SISTEM NILAI MAHASISWA----- ")

#Menampilkan judul program.
\n berfungsi memberi baris kosong sebelum teks ditampilkan.

print("1. Input nilai mahasiswa") 
print("2. Tampilkan semua nilai") 
print("3. Cek nilai mahasiswa tertentu") 
print("4. Tampilkan address array") 
print("5. Keluar")

#Kelima baris ini hanya berfungsi menampilkan pilihan menu kepada pengguna.

<img width="423" height="235" alt="image" src="https://github.com/user-attachments/assets/688fdb68-7bc7-4918-9164-34e6f0081dd3" />

def main():

#Mendefinisikan fungsi utama program.
Semua proses utama dijalankan di dalam fungsi ini.

nilai = buatkan deskripsi singkat[0] * 5

#Membuat list atau array bernama nilai.
[0] : satu elemen bernilai 0
* 5 : digandakan menjadi 5 elemen

running = True

#Membuat variabel kontrol perulangan.
Jika running = True, program tetap berjalan.

while running:

#Perulangan utama program.
menu akan terus muncul selama running masih True.

menu()

#Memanggil fungsi menu() agar pilihan menu tampil di layar.

try:

#Memulai blok exception handling untuk menangani error input.

pilihan = int(input("Pilih menu: "))

#Penjelasan:
input() : menerima input dari user
int() : mengubah input menjadi angka
disimpan ke variabel pilihan

except ValueError:

#Jika user memasukkan huruf atau simbol, Python menghasilkan error ValueError.

print("Input harus angka!")
continue

#Program menampilkan pesan error lalu kembali ke awal perulangan menu.

if pilihan == 1:

#Percabangan kondisi jika user memilih menu nomor 1.

print("\nMasukkan nilai 5 mahasiswa")

#Perulangan sebanyak panjang array.
len(nilai) bernilai 5, jadi loop berjalan 5 kali.

while True:

#Digunakan agar input diulang jika terjadi kesalahan.

nilai[i] = int(input(f"Nilai Mahasiswa ke-{i+1}: "))
#Penjelasan:

meminta input nilai
{i+1} agar nomor mahasiswa dimulai dari 1
nilai disimpan pada index array tertentu

break

#Keluar dari loop while jika input berhasil.

except ValueError: 
print("Harus berupa angka")

#Jika input bukan angka, program meminta input ulang.


https://youtu.be/NI6EImYEA_o

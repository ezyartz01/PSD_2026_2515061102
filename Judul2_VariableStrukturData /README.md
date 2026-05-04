Judul: Program mengurutkan ranking player terbaik dalam sebuah game berdasarkan score tertinggi


<img width="672" height="76" alt="image" src="https://github.com/user-attachments/assets/199573b9-549d-4f2d-9104-642a9cc6aa15" />

- def tukar(arr, i ,j): --> Membuat fungsi bernama tukar 
- temp = arr[i] --> Memasukkan nilai dalam index i ke dalam variabel temp untuk sementara
- arr[i] = arr[j] --> Memasukkan nilai dari index j ke index i
- arr[j] = temp --> Memasukkan nilai temp ke dalam index j

<img width="676" height="157" alt="image" src="https://github.com/user-attachments/assets/f3b1ebeb-d7dc-477c-8e5e-0ed501f78383" />

- def selection_sort(arr, n,): --> Membuat fungsi selection_sort
- for i in range(n - 1): --> Loop untuk menandai batas bagian yang sudah terurut
- pos_terbesar = i --> Anngap nilai i adalah nilai terbesar saat ini
- for j in range(i + 1, n): --> Loop untuk mengecek nilai yang belum terurut
- if arr[j] < arr[pos_terbesar]: --> Jika ada nilai yang lebih besar dari pos_terbesar
- pos_terbesar = j --> Update posisi telai terbesar yang baru
- if pos_terbesar != i: --> Jika pos terbesar bukan di index i
- tukar(arr, i, pos_terbesar) --> Tukar posisi elemen i dengan elemen terbesar tersebut

<img width="673" height="404" alt="image" src="https://github.com/user-attachments/assets/22719932-7713-4f16-8aef-748968d983ad" />

- def main() --> Membuat fungsi utama (main)
- try: --> Mulai mencoba
- n = int(input("Masukkan jumlah pemain: ")) --> Membuat inputan untuk user dan harus interger
- except ValueError: --> Error Handling
- print("Input tidak valid!") --> Menampilkan "input tidak valid" karena inputan tidak sesuai
- return --> Menghentikan fungsi
- arr = [] --> menyiapkan wadah kosong untuk menampung score
- print("Masukkan score pemain:") --> Menampilkan "Masukkan score"
- for i in range(n): --> Memulai loop sebanyak jumlah n (banyak inputan user)
- while True: --> Selagi masih true (looping)
- try: --> Mulai Mencoba
- nilai = int(input(f"Score pemain ke-{i+1}: ")) --> Membuat variabel nilai lalu membuat inputan untuk user: membuat score untuk pemain
- arr.append(nilai) --> Menambahkan nilai yang baru di inputkan ke dalam array
- break --> Untuk menghentikan looping
- except ValueError: --> Error Handling
- print("Input tidak valid, silakan masukkan angka!") --> Menampilkan "Input tidak valid, silakan masukkan angka!"
- print(f"Array sebelum diurutkan: {arr}") --> Menampilkan Array sebelum diurutkan
- selection_sort(arr, n) --> Memanggil fungsi Selection_sort
- print("Array setelah diurutkan (Selection Sort - Descending):", end="\n") --> Menampilkan array setelah diurutkan
- for i in range(n): --> Memulai loop sebanyak jumlah n (banyak inputan user)
- print(f"{i+1}. {arr[i]} Points") Menampilkan Nomor urutan dari 1, dan menampilkan Score inputan dari user yang tadi dimasukkan ke dalam array

<img width="682" height="43" alt="image" src="https://github.com/user-attachments/assets/0521e43f-fedd-4bf8-8001-634a39f466e7" />

if __name__ == "__main__":
    main() --> Memulai fungsi utama (main)

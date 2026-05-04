Judul: Program mengurutkan ranking player terbaik dalam sebuah game berdasarkan score tertinggi


<img width="672" height="76" alt="image" src="https://github.com/user-attachments/assets/199573b9-549d-4f2d-9104-642a9cc6aa15" />

- def tukar(arr, i ,j): --> Membuat fungsi bernama tukar 
- temp = arr[i] --> Memasukkan nilai dalam index i ke dalam variabel temp untuk sementara
- arr[i] = arr[j] --> Memasukkan nilai dari index j ke index i
- arr[j] = temp --> Memasukkan nilai temp ke dalam index j

<img width="676" height="162" alt="image" src="https://github.com/user-attachments/assets/603700f5-be4c-4c63-83fa-a75c8ad23b0a" />

- def selection_sort(arr, n,): --> Membuat fungsi selection_sort
- for i in range(n - 1): --> Loop untuk menandai batas bagian yang sudah terurut
- pos_terbesar = i --> Anngap nilai i adalah nilai terbesar saat ini
- for j in range(i + 1, n): --> Loop untuk mengecek nilai yang belum terurut
- if arr[j] < arr[pos_terbesar]: --> Jika ada nilai yang lebih besar dari pos_terbesar
- pos_terbesar = j --> Update posisi telai terbesar yang baru
- if pos_terbesar != i: --> Jika pos terbesar bukan di index i
- tukar(arr, i, pos_terbesar) --> Tukar posisi elemen i dengan elemen terbesar tersebut

<img width="673" height="404" alt="image" src="https://github.com/user-attachments/assets/22719932-7713-4f16-8aef-748968d983ad" />

- def main()
- try:
- n = int(input("Masukkan jumlah pemain: "))
- except ValueError:
- print("Input tidak valid!")
- return
- arr = []
- print("Masukkan score pemain:")
- for i in range(n):
- while True:
- try:
- nilai = int(input(f"Score pemain ke-{i+1}: "))
- arr.append(nilai)
- break
- except ValueError:
- print("Input tidak valid, silakan masukkan angka!")
- print(f"Array sebelum diurutkan: {arr}")
- selection_sort(arr, n)
- print("Array setelah diurutkan (Selection Sort - Descending):", end="\n")
- for i in range(n):
- print(f"{i+1}. {arr[i]} Points")

<img width="682" height="43" alt="image" src="https://github.com/user-attachments/assets/0521e43f-fedd-4bf8-8001-634a39f466e7" />

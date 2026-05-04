def tukar(arr, i ,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr, n,):
    for i in range(n - 1):
        pos_terbesar = i 
        for j in range(i + 1, n):
            if arr[j] > arr[pos_terbesar]:
                pos_terbesar = j
        if pos_terbesar != i:
                tukar(arr, i, pos_terbesar)

def main():
    try:
        n = int(input("Masukkan jumlah pemain: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan score pemain:")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Score pemain ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Array sebelum diurutkan: {arr}")
    selection_sort(arr, n)
    print("Array setelah diurutkan (Selection Sort - Descending):", end="\n")
    for i in range(n):
        print(f"{i+1}. {arr[i]} Points")

if __name__ == "__main__":
    main()


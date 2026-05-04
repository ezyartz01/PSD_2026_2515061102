def menu():
    print("\n ----SISTEM NILAI MAHASISWA----  ")
    print("1. Input nilai mahasiswa")
    print("2. Tampilkan semua nilai")
    print("3. Cek nilai mahasiswa tertentu")
    print("4. Tampilkan address array")
    print("5. Keluar")

def main():
    nilai = [0] * 5
    running = True

    while running:
        menu()

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka...")
            continue

        #Input Nilai
        if pilihan == 1:
            print("\nMasukkan nilai 5 mahasiswa")
            for i in range(len(nilai)):
                while True:
                    try:
                        nilai[i] = int(input(f"Nilai Mahasiswa ke-{i+1}: "))
                        break
                    except ValueError:
                        print("Harus berupa angka...")

        #Menampilkan Nilai
        elif pilihan == 2:
            print("\nDaftar Nilai Mahasiswa:")
            for i in range(len(nilai)):
                print(f"Mahasiswa {i+1} = {nilai[i]}")

        #Cek Nilai
        elif pilihan == 3:
            try:
                index = int(input("Cek mahasiswa nomor (1-5): ")) - 1
                if 0 <= index < len(nilai):
                    print(f"Nilai Mahasiswa {index+1} = {nilai[index]}")
                else:
                    print("Nomor mahasiswa tidak ada!")
            except ValueError:
                print("Input harus angka...")

        # ADDRESS ARRAY
        elif pilihan == 4:
            print(f"Address array nilai: ")
            for i in range(len(nilai)):
                print(f"Address nilai[{i}] = {id(nilai[i])}")

        # KELUAR
        elif pilihan == 5:
            running = False
            print("Program selesai.")

        else:
            print("Menu tidak tersedia...")

if __name__ == "__main__":
    main()
def binary_search_player(player_ids, n, target_id):
    l = 0
    r = n - 1
    pos = -1

    while l <= r:
        m = l + (r - l) // 2
        print(f"Mengecek Player ID: {player_ids[m]}")

        if player_ids[m] == target_id:
            pos = m
            break
        elif player_ids[m] < target_id:
            print("Mencari player dengan ID lebih besar:")
            l = m + 1
        else:
            print("Mencari player dengan ID lebih kecil:")
            r = m - 1
    return pos


def main():
    player_ids = list(range(1001, 1021))
    n = len(player_ids)

    friend_list = []

    print("SISTEM ADD FRIEND GAME")

    while True:
        print("\nFriend List Saat Ini:")
        if friend_list:
            print(friend_list)
        else:
            print("Belum memiliki teman.")

        pilihan = input("\nTambah teman baru? (y/n): ")

        if pilihan.lower() == "n":
            print("Program selesai.")
            break

        elif pilihan.lower() == "y":
            print("\nDaftar Player Online:")
            print(player_ids)

            try:
                target_id = int(input("\nMasukkan ID Player: "))

                pos = binary_search_player(player_ids, n, target_id)

                if pos != -1:
                    print(f"\nPlayer ID {target_id} ditemukan!")

                    if target_id in friend_list:
                        print("Player sudah ada di friend list.")
                        continue

                    konfirmasi = input("Tambah sebagai teman? (y/n): ")

                    if konfirmasi.lower() == "y":
                        if target_id not in friend_list:
                            friend_list.append(target_id)
                            print("Teman berhasil ditambahkan!")
                    else:
                        print("Batal menambahkan teman.")

                else:
                    print("Player tidak ditemukan.")

            except ValueError:
                print("Input harus berupa angka!")

        else:
            print("Pilihan tidak valid!")

    print("\nFRIEND LIST AKHIR:")
    print(friend_list)


if __name__ == "__main__":
    main()
class Node:
    def __init__(self, kode_buku, judul_buku):
        self.kode_buku = kode_buku
        self.judul_buku = judul_buku
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, total_rak=5):
        self.TOTAL_RAK = total_rak
        self.daftar_rak = [None] * self.TOTAL_RAK

    def hash_function(self, kode_buku):
        return (kode_buku % self.TOTAL_RAK + self.TOTAL_RAK) % self.TOTAL_RAK

    def insert(self, kode_buku, judul_buku):
        nomor_rak = self.hash_function(kode_buku)
        current = self.daftar_rak[nomor_rak]
        
        while current is not None:
            if current.kode_buku == kode_buku:
                current.judul_buku = judul_buku
                return
            current = current.next
            
        buku_baru = Node(kode_buku, judul_buku)
        buku_baru.next = self.daftar_rak[nomor_rak]
        self.daftar_rak[nomor_rak] = buku_baru

    def search(self, kode_buku):
        nomor_rak = self.hash_function(kode_buku)
        current = self.daftar_rak[nomor_rak]
        
        while current is not None:
            if current.kode_buku == kode_buku:
                return current
            current = current.next
        return None

    def ambil_buku(self, kode_buku):
        nomor_rak = self.hash_function(kode_buku)
        current = self.daftar_rak[nomor_rak]
        prev = None
        
        while current is not None:
            if current.kode_buku == kode_buku:
                if prev is None:
                    self.daftar_rak[nomor_rak] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def tampilkan_kondisi_rak(self):
        print("\n ==KONDISI RAK PERPUSTAKAAN (Separate Chaining)== ")
        for i in range(self.TOTAL_RAK):
            print(f"Rak Nomor {i}: ", end="")
            current = self.daftar_rak[i]
            if current is None:
                print("[Kosong]")
                continue
                
            while current is not None:
                print(f"[{current.kode_buku} : {current.judul_buku}] -> ", end="")
                current = current.next
            print("Selesai")


def main():
    perpustakaan = HashMapSeparateChaining(total_rak=5)
    
    perpustakaan.insert(5, "Struktur Data")
    perpustakaan.insert(10, "Rekayasa Perangkat Lunak")
    perpustakaan.insert(15, "Matematika Diskrit")
    perpustakaan.insert(7, "Aljabar Matriks")
    
    perpustakaan.tampilkan_kondisi_rak()

    kode_dicari = 10
    print(f"\n[Mencari Buku dengan Kode {kode_dicari}...]")
    buku_ditemukan = perpustakaan.search(kode_dicari)
    if buku_ditemukan is not None:
        print(f"Buku ditemukan! Judulnya adalah '{buku_ditemukan.judul_buku}'")
    else:
        print("kode buku tersebut tidak ada di rak mana pun.")

    print(f"\n[Mengambil Buku dengan Kode {kode_dicari} dari rak...]")
    perpustakaan.ambil_buku(kode_dicari)
    
    perpustakaan.tampilkan_kondisi_rak()


if __name__ == "__main__":
    main()
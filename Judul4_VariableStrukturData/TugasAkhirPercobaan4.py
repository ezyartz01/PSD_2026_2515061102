#Queue linked list

class Node:
    def __init__(self, nomor_antrian):
        self.nomor_antrian = nomor_antrian
        self.next = None

class CloudQueue:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.nomor_urut_counter = 1

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self):
        nomor_pemain = self.nomor_urut_counter
        self.nomor_urut_counter += 1 

        new_node = Node(nomor_pemain)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"Pemain nomor {nomor_pemain} masuk antrian cloud server.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong.")
            return
        
        temp = self.front_ptr
        pemain_masuk_game = temp.nomor_antrian
        self.front_ptr = self.front_ptr.next

        print(f"Pemain nomor {pemain_masuk_game} dialokasikan ke PC Cloud untuk bermain.")

        if self.front_ptr is None:
            self.rear_ptr = None
            
    def peek(self):
        if self.is_empty():
            print("Antrian kosong.")
            return
        print(f"Giliran berikutnya: Pemain nomor {self.front_ptr.nomor_antrian}")

    def display(self):
        if self.is_empty():
            print("\n DASHBOARD ANTRIAN CLOUD GAMING: ")
            print("Status: Kosong")
            return

        print("\n DASHBOARD ANTRIAN CLOUD GAMING: ")
        print("Urutan Antrian (Depan -> Belakang): ", end="")
        current = self.front_ptr
        
        while current is not None:
            print(current.nomor_antrian, end=" ")
            current = current.next

def main():
    queue = CloudQueue()
    pilih = 0

    while pilih != 5:
        print("\n SYSTEM CLOUD GAMING QUEUE MENU ")
        print("1. (Enqueue)")
        print("2. (Dequeue)")
        print("3. (Peek)")
        print("4. (Dashboard)")
        print("5. (Matikan Sistem)")
        
        try:
            pilih = int(input("Aksi menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            queue.enqueue()
            
        elif pilih == 2:
            queue.dequeue()
            
        elif pilih == 3:
            queue.peek()
            
        elif pilih == 4:
            queue.display()
            
        elif pilih == 5:
            print("\nMembersihkan sisa antrian...")
            while not queue.is_empty():
                    queue.dequeue()
            print("Sistem cloud gaming dimatikan.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
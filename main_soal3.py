from soal_3 import RestaurantQueue

def main():
    rq = RestaurantQueue()

    while True:
        print("\nMenu:")
        print("1. Tambah pesanan (enqueue)")
        print("2. Hapus pesanan (dequeue)")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        pilihan = input("Pilih operasi (1/2/3/4): ")

        if pilihan == "1":
            order = input("Masukkan pesanan: ")
            rq.enqueue(order)
        elif pilihan == "2":
            rq.dequeue()
        elif pilihan == "3":
            rq.display_queue()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()

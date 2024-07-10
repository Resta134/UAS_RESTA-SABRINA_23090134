mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    mahasiswa.append({"NIM": nim, "Nama": nama})

    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
    if tambah_lagi != 'ya':
        break

print("\nData Mahasiswa:")
for idx, mhs in enumerate(mahasiswa, 1):
    print(f"{idx}. NIM: {mhs['NIM']}, Nama: {mhs['Nama']}")

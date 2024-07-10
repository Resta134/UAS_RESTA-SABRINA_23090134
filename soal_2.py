import pandas as pd

nilai_mahasiswa = [
    [90, 80],
    [50, 60],
    [65, 70]
]

df = pd.DataFrame(nilai_mahasiswa, index=['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
                  columns=['Algoritma dan Struktur Data 2', 'Matematika Numerik'])

print("Data Nilai Mahasiswa:")
print(df)

rata_rata_mata_kuliah = df.mean()
df['Rata-rata'] = df.mean(axis=1)


print("\nRata-rata Nilai Setiap Mata Kuliah:")
print(rata_rata_mata_kuliah)

print("\nData Nilai Mahasiswa dengan Rata-rata:")
print(df)

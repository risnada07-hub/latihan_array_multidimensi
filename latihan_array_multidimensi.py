# ============================================================
#   LATIHAN ARRAY MULTIDIMENSI PYTHON
#   Materi: 2D Array, 3D Array, Operasi, dan Studi Kasus
# ============================================================

import random

# ─────────────────────────────────────────────
# BAGIAN 1: ARRAY 2 DIMENSI (MATRIKS)
# ─────────────────────────────────────────────

print("=" * 55)
print("  BAGIAN 1: ARRAY 2 DIMENSI (MATRIKS)")
print("=" * 55)

# 1.1 Membuat array 2D secara manual
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n[1.1] Matriks 3x3 :")
for baris in matriks:
    print(" ", baris)

# 1.2 Akses elemen
print(f"\n[1.2] Akses elemen baris ke-1, kolom ke-2 : {matriks[1][2]}")
print(f"      Akses elemen baris ke-0, kolom ke-0 : {matriks[0][0]}")

# 1.3 Mengubah nilai elemen
matriks[2][2] = 99
print(f"\n[1.3] Setelah matriks[2][2] diubah menjadi 99 :")
for baris in matriks:
    print(" ", baris)

# 1.4 Iterasi seluruh elemen
print("\n[1.4] Semua elemen matriks :")
for i, baris in enumerate(matriks):
    for j, nilai in enumerate(baris):
        print(f"      matriks[{i}][{j}] = {nilai}")

# 1.5 Membuat matriks dengan list comprehension
print("\n[1.5] Matriks 4x4 dengan list comprehension (baris * kolom) :")
matriks_lc = [[i * j for j in range(1, 5)] for i in range(1, 5)]
for baris in matriks_lc:
    print(" ", baris)


# ─────────────────────────────────────────────
# BAGIAN 2: OPERASI PADA MATRIKS
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("  BAGIAN 2: OPERASI PADA MATRIKS")
print("=" * 55)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# 2.1 Penjumlahan matriks
print("\n[2.1] Penjumlahan Matriks A + B :")
hasil_tambah = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("  A =", A)
print("  B =", B)
print("  Hasil =", hasil_tambah)

# 2.2 Perkalian skalar
skalar = 3
print(f"\n[2.2] Perkalian Matriks A dengan skalar {skalar} :")
hasil_skalar = [[A[i][j] * skalar for j in range(len(A[0]))] for i in range(len(A))]
print("  Hasil =", hasil_skalar)

# 2.3 Transpose matriks
print("\n[2.3] Transpose Matriks A :")
transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("  A         =", A)
print("  Transpose =", transpose)

# 2.4 Perkalian matriks (dot product)
print("\n[2.4] Perkalian Matriks A x B :")
baris_A, kolom_A = len(A), len(A[0])
kolom_B = len(B[0])
hasil_kali = [[sum(A[i][k] * B[k][j] for k in range(kolom_A)) for j in range(kolom_B)] for i in range(baris_A)]
print("  A x B =", hasil_kali)

# 2.5 Mencari nilai maksimum dan minimum
print("\n[2.5] Nilai maksimum dan minimum pada matriks A :")
semua_nilai = [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]
print(f"  Semua nilai : {semua_nilai}")
print(f"  Maksimum    : {max(semua_nilai)}")
print(f"  Minimum     : {min(semua_nilai)}")


# ─────────────────────────────────────────────
# BAGIAN 3: ARRAY 3 DIMENSI
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("  BAGIAN 3: ARRAY 3 DIMENSI")
print("=" * 55)

# 3.1 Membuat array 3D
array_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

print("\n[3.1] Array 3D (3 lapisan, 2 baris, 2 kolom) :")
for i, lapisan in enumerate(array_3d):
    print(f"  Lapisan {i} :")
    for baris in lapisan:
        print(f"    {baris}")

# 3.2 Akses elemen 3D
print(f"\n[3.2] Akses elemen array_3d[1][0][1] = {array_3d[1][0][1]}")
print(f"      Akses elemen array_3d[2][1][0] = {array_3d[2][1][0]}")

# 3.3 List comprehension untuk 3D
print("\n[3.3] Array 3D dengan list comprehension (2x3x4) diisi nilai 0 :")
array_3d_lc = [[[0 for _ in range(4)] for _ in range(3)] for _ in range(2)]
for i, lapisan in enumerate(array_3d_lc):
    print(f"  Lapisan {i} : {lapisan}")


# ─────────────────────────────────────────────
# BAGIAN 4: STUDI KASUS – NILAI SISWA
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("  BAGIAN 4: STUDI KASUS – NILAI SISWA")
print("=" * 55)

# Data: [nama, [Matematika, IPA, Bahasa Indonesia]]
siswa = [
    ["Andi",  [85, 90, 78]],
    ["Budi",  [70, 65, 88]],
    ["Citra", [92, 88, 95]],
    ["Devi",  [60, 75, 80]],
    ["Eko",   [78, 82, 73]],
]
mata_pelajaran = ["Matematika", "IPA", "Bahasa Indonesia"]

print("\n[4.1] Daftar Nilai Siswa :")
print(f"  {'Nama':<10}", end="")
for mp in mata_pelajaran:
    print(f"{mp:>18}", end="")
print(f"{'Rata-rata':>12}")
print("  " + "-" * 70)

for nama, nilai in siswa:
    rata = sum(nilai) / len(nilai)
    print(f"  {nama:<10}", end="")
    for n in nilai:
        print(f"{n:>18}", end="")
    print(f"{rata:>12.1f}")

# Nilai tertinggi per mata pelajaran
print("\n[4.2] Nilai Tertinggi per Mata Pelajaran :")
for idx, mp in enumerate(mata_pelajaran):
    nilai_mp = [(siswa[i][0], siswa[i][1][idx]) for i in range(len(siswa))]
    terbaik = max(nilai_mp, key=lambda x: x[1])
    print(f"  {mp:<20}: {terbaik[0]} ({terbaik[1]})")

# Siswa dengan rata-rata tertinggi
print("\n[4.3] Peringkat Siswa Berdasarkan Rata-rata :")
peringkat = sorted(siswa, key=lambda s: sum(s[1]) / len(s[1]), reverse=True)
for rank, (nama, nilai) in enumerate(peringkat, 1):
    rata = sum(nilai) / len(nilai)
    print(f"  {rank}. {nama:<10} - Rata-rata: {rata:.1f}")


# ─────────────────────────────────────────────
# BAGIAN 5: STUDI KASUS – PETA GRID (MAZE)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("  BAGIAN 5: STUDI KASUS – PETA GRID (MAZE)")
print("=" * 55)

# Keterangan: 0 = jalan, 1 = dinding, S = start, E = end
peta = [
    ['S', 0, 1, 1, 1],
    [1,   0, 0, 1, 1],
    [1,   1, 0, 1, 1],
    [1,   1, 0, 0, 0],
    [1,   1, 1, 1, 'E'],
]

print("\n[5.1] Peta Grid 5x5 :")
print("  Keterangan : S=Start, E=End, 0=Jalan, 1=Dinding")
print()
for baris in peta:
    print("  ", end="")
    for sel in baris:
        print(f"{str(sel):^4}", end="")
    print()

print("\n[5.2] Mencari posisi Start dan End :")
for i in range(len(peta)):
    for j in range(len(peta[i])):
        if peta[i][j] == 'S':
            print(f"  Start berada di : baris {i}, kolom {j}")
        if peta[i][j] == 'E':
            print(f"  End   berada di : baris {i}, kolom {j}")


# ─────────────────────────────────────────────
# BAGIAN 6: LATIHAN MANDIRI (SOAL)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("  BAGIAN 6: LATIHAN MANDIRI")
print("=" * 55)

print("""
  Kerjakan soal-soal berikut ini:

  Soal 1 ──────────────────────────────────────
  Buat matriks 5x5 yang berisi bilangan acak 1–100,
  kemudian tampilkan:
    a) Semua elemen pada diagonal utama
    b) Jumlah seluruh elemen
    c) Nilai terbesar dan letaknya (baris, kolom)

  Soal 2 ──────────────────────────────────────
  Buat array 2D untuk menyimpan jadwal pelajaran
  (5 hari x 3 sesi). Isi dengan nama mata pelajaran,
  lalu tampilkan jadwal hari Rabu.

  Soal 3 ──────────────────────────────────────
  Buat fungsi `jumlah_matriks(A, B)` yang menerima
  dua matriks berukuran sama dan mengembalikan
  matriks hasil penjumlahannya.

  Soal 4 ──────────────────────────────────────
  Gunakan list comprehension untuk membuat matriks
  identitas (diagonal bernilai 1, sisanya 0)
  berukuran NxN (N diinput pengguna).

  Soal 5 ──────────────────────────────────────
  Buat array 3D berukuran 3x3x3 berisi angka 1–27
  secara berurutan, kemudian tampilkan setiap lapisan
  dalam bentuk tabel rapi.
""")

# ─── Contoh Solusi Soal 1 ───
print("  [Contoh Solusi Soal 1]")
random.seed(42)
matriks_acak = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

print("\n  Matriks 5x5 acak :")
for baris in matriks_acak:
    print("  ", baris)

diagonal = [matriks_acak[i][i] for i in range(5)]
print(f"\n  Diagonal utama : {diagonal}")
print(f"  Jumlah semua   : {sum(matriks_acak[i][j] for i in range(5) for j in range(5))}")

maks = matriks_acak[0][0]
pos = (0, 0)
for i in range(5):
    for j in range(5):
        if matriks_acak[i][j] > maks:
            maks = matriks_acak[i][j]
            pos = (i, j)
print(f"  Nilai terbesar : {maks} pada baris {pos[0]}, kolom {pos[1]}")

print("\n" + "=" * 55)
print("=" * 55)
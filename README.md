#   LATIHAN ARRAY MULTIDIMENSI PYTHON
#   Materi : 2D Array, 3D Array, Operasi, dan Studi Kasus
#   Library: Tidak ada (built-in only)

#   DAFTAR ISI
#   ──────────────────────────────────────────────────────────
#   Bagian 1 │ Array 2 Dimensi (Matriks)
#   Bagian 2 │ Operasi pada Matriks
#   Bagian 3 │ Array 3 Dimensi
#   Bagian 4 │ Studi Kasus – Nilai Siswa
#   Bagian 5 │ Studi Kasus – Peta Grid (Maze)
#   Bagian 6 │ Latihan Mandiri (Soal + Solusi Soal 1)
#   ──────────────────────────────────────────────────────────
#
#   Cara menjalankan:
#     python latihan_array_multidimensi.py
#
#   Di VS Code:
#     Ctrl+F5  →  Run Without Debugging
#     tombol di pojok kanan atas
#
 
import random
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 1: ARRAY 2 DIMENSI (MATRIKS)
# ─────────────────────────────────────────────────────────────
#
#   Cara kerja indeks:
#
#   matriks[baris][kolom]
#            │       │
#            │       └── kolom ke-? (dari kiri, mulai 0)
#            └────────── baris ke-? (dari atas, mulai 0)
#
#   matriks = [[1, 2, 3],   ← baris 0
#              [4, 5, 6],   ← baris 1
#              [7, 8, 9]]   ← baris 2
#                 ↑  ↑  ↑
#              kol0 kol1 kol2
#
#   matriks[1][2]  →  6  ✓
# ─────────────────────────────────────────────────────────────
 
print("=" * 55)
print("  BAGIAN 1: ARRAY 2 DIMENSI (MATRIKS)")
print("=" * 55)
 
# 1.1 – Membuat array 2D secara manual
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
print("\n[1.1] Matriks 3x3 :")
for baris in matriks:
    print(" ", baris)
 
# 1.2 – Mengakses elemen → matriks[baris][kolom]
print(f"\n[1.2] Akses elemen baris ke-1, kolom ke-2 : {matriks[1][2]}")
print(f"      Akses elemen baris ke-0, kolom ke-0 : {matriks[0][0]}")
 
# 1.3 – Mengubah nilai elemen
matriks[2][2] = 99
print(f"\n[1.3] Setelah matriks[2][2] diubah menjadi 99 :")
for baris in matriks:
    print(" ", baris)
 
# 1.4 – Iterasi seluruh elemen dengan index
print("\n[1.4] Semua elemen matriks :")
for i, baris in enumerate(matriks):
    for j, nilai in enumerate(baris):
        print(f"      matriks[{i}][{j}] = {nilai}")
 
# 1.5 – List comprehension untuk membuat matriks 4x4
#        Pola: [[i * j for j in range(1,5)] for i in range(1,5)]
print("\n[1.5] Matriks 4x4 dengan list comprehension (baris * kolom) :")
matriks_lc = [[i * j for j in range(1, 5)] for i in range(1, 5)]
for baris in matriks_lc:
    print(" ", baris)
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 2: OPERASI PADA MATRIKS
# ─────────────────────────────────────────────────────────────
#
#   Operasi yang dipelajari:
#     2.1 → Penjumlahan   : hasil[i][j] = A[i][j] + B[i][j]
#     2.2 → Skalar        : hasil[i][j] = A[i][j] * k
#     2.3 → Transpose     : hasil[i][j] = A[j][i]
#     2.4 → Dot product   : hasil[i][j] = sum(A[i][k] * B[k][j])
#     2.5 → Max & Min     : max/min dari seluruh elemen
# ─────────────────────────────────────────────────────────────
 
print("\n" + "=" * 55)
print("  BAGIAN 2: OPERASI PADA MATRIKS")
print("=" * 55)
 
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
 
# 2.1 – Penjumlahan matriks A + B
print("\n[2.1] Penjumlahan Matriks A + B :")
hasil_tambah = [[A[i][j] + B[i][j]
                 for j in range(len(A[0]))]
                 for i in range(len(A))]
print("  A      =", A)
print("  B      =", B)
print("  Hasil  =", hasil_tambah)   # [[6,8],[10,12]]
 
# 2.2 – Perkalian skalar
skalar = 3
print(f"\n[2.2] Perkalian Matriks A dengan skalar {skalar} :")
hasil_skalar = [[A[i][j] * skalar
                 for j in range(len(A[0]))]
                 for i in range(len(A))]
print("  Hasil =", hasil_skalar)    # [[3,6],[9,12]]
 
# 2.3 – Transpose matriks (baris ↔ kolom)
print("\n[2.3] Transpose Matriks A :")
transpose = [[A[j][i]
              for j in range(len(A))]
              for i in range(len(A[0]))]
print("  A         =", A)
print("  Transpose =", transpose)   # [[1,3],[2,4]]
 
# 2.4 – Perkalian matriks / dot product
#        hasil[i][j] = Σ A[i][k] × B[k][j]
print("\n[2.4] Perkalian Matriks A x B :")
baris_A, kolom_A = len(A), len(A[0])
kolom_B = len(B[0])
hasil_kali = [[sum(A[i][k] * B[k][j] for k in range(kolom_A))
               for j in range(kolom_B)]
               for i in range(baris_A)]
print("  A x B =", hasil_kali)      # [[19,22],[43,50]]
 
# 2.5 – Nilai maksimum dan minimum dari seluruh elemen
print("\n[2.5] Nilai maksimum dan minimum pada matriks A :")
semua_nilai = [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]
print(f"  Semua nilai : {semua_nilai}")
print(f"  Maksimum    : {max(semua_nilai)}")
print(f"  Minimum     : {min(semua_nilai)}")
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 3: ARRAY 3 DIMENSI
# ─────────────────────────────────────────────────────────────
#
#   Struktur akses:
#     array_3d[lapisan][baris][kolom]
#
#   List comprehension 3D:
#     array = [[[0 for _ in range(N)]
#                  for _ in range(M)]
#                  for _ in range(L)]
#              └─────────────────────── L lapisan
#                   └──────────────── M baris per lapisan
#                        └─────────── N kolom per baris
# ─────────────────────────────────────────────────────────────
 
print("\n" + "=" * 55)
print("  BAGIAN 3: ARRAY 3 DIMENSI")
print("=" * 55)
 
# 3.1 – Membuat array 3D secara manual (3 lapisan × 2 baris × 2 kolom)
array_3d = [
    [[1,  2],  [3,  4]],   # lapisan 0
    [[5,  6],  [7,  8]],   # lapisan 1
    [[9, 10], [11, 12]],   # lapisan 2
]
 
print("\n[3.1] Array 3D (3 lapisan, 2 baris, 2 kolom) :")
for i, lapisan in enumerate(array_3d):
    print(f"  Lapisan {i} :")
    for baris in lapisan:
        print(f"    {baris}")
 
# 3.2 – Mengakses elemen dengan 3 indeks
print(f"\n[3.2] Akses elemen array_3d[1][0][1] = {array_3d[1][0][1]}")
print(f"      Akses elemen array_3d[2][1][0] = {array_3d[2][1][0]}")
 
# 3.3 – Array 3D kosong via list comprehension (2 × 3 × 4)
print("\n[3.3] Array 3D dengan list comprehension (2x3x4) diisi nilai 0 :")
array_3d_lc = [[[0 for _ in range(4)]
                   for _ in range(3)]
                   for _ in range(2)]
for i, lapisan in enumerate(array_3d_lc):
    print(f"  Lapisan {i} : {lapisan}")
 
# Tips debugging ukuran array 3D:
print(f"\n  Tips debugging :")
print(f"    len(array_3d)       = {len(array_3d)}  (jumlah lapisan)")
print(f"    len(array_3d[0])    = {len(array_3d[0])}  (baris per lapisan)")
print(f"    len(array_3d[0][0]) = {len(array_3d[0][0])}  (kolom per baris)")
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 4: STUDI KASUS – NILAI SISWA
# ─────────────────────────────────────────────────────────────
#
#   Struktur data:
#     siswa = [
#         [nama_string, [nilai_mapel1, nilai_mapel2, nilai_mapel3]],
#         ...
#     ]
#
#   Indeks akses:
#     siswa[i][0]    → nama siswa ke-i
#     siswa[i][1]    → list nilai siswa ke-i
#     siswa[i][1][j] → nilai siswa ke-i pada mapel ke-j
# ─────────────────────────────────────────────────────────────
 
print("\n" + "=" * 55)
print("  BAGIAN 4: STUDI KASUS – NILAI SISWA")
print("=" * 55)
 
siswa = [
    ["Andi",  [85, 90, 78]],
    ["Budi",  [70, 65, 88]],
    ["Citra", [92, 88, 95]],
    ["Devi",  [60, 75, 80]],
    ["Eko",   [78, 82, 73]],
]
mata_pelajaran = ["Matematika", "IPA", "Bahasa Indonesia"]
 
# 4.1 – Tampilkan tabel nilai + rata-rata
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
 
# 4.2 – Nilai tertinggi per mata pelajaran
print("\n[4.2] Nilai Tertinggi per Mata Pelajaran :")
for idx, mp in enumerate(mata_pelajaran):
    nilai_mp = [(siswa[i][0], siswa[i][1][idx]) for i in range(len(siswa))]
    terbaik  = max(nilai_mp, key=lambda x: x[1])
    print(f"  {mp:<20}: {terbaik[0]} ({terbaik[1]})")
 
# 4.3 – Peringkat berdasarkan rata-rata (descending)
print("\n[4.3] Peringkat Siswa Berdasarkan Rata-rata :")
peringkat = sorted(siswa, key=lambda s: sum(s[1]) / len(s[1]), reverse=True)
for rank, (nama, nilai) in enumerate(peringkat, 1):
    rata = sum(nilai) / len(nilai)
    print(f"  {rank}. {nama:<10} - Rata-rata: {rata:.1f}")
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 5: STUDI KASUS – PETA GRID (MAZE)
# ─────────────────────────────────────────────────────────────
#
#   Representasi maze sebagai array 2D:
#     'S' = Start (titik awal)
#     'E' = End   (titik akhir)
#      0  = Jalan (bisa dilalui)
#      1  = Dinding (tidak bisa dilalui)
#
#   Akses sel : peta[baris][kolom]
# ─────────────────────────────────────────────────────────────
 
print("\n" + "=" * 55)
print("  BAGIAN 5: STUDI KASUS – PETA GRID (MAZE)")
print("=" * 55)
 
peta = [
    ['S', 0, 1, 1, 1],
    [ 1,  0, 0, 1, 1],
    [ 1,  1, 0, 1, 1],
    [ 1,  1, 0, 0, 0],
    [ 1,  1, 1, 1,'E'],
]
 
# 5.1 – Tampilkan peta grid
print("\n[5.1] Peta Grid 5x5 :")
print("  Keterangan : S=Start, E=End, 0=Jalan, 1=Dinding")
print()
for baris in peta:
    print("  ", end="")
    for sel in baris:
        print(f"{str(sel):^4}", end="")
    print()
 
# 5.2 – Cari posisi Start dan End secara otomatis
print("\n[5.2] Mencari posisi Start dan End :")
for i in range(len(peta)):
    for j in range(len(peta[i])):
        if peta[i][j] == 'S':
            print(f"  Start berada di : baris {i}, kolom {j}")
        if peta[i][j] == 'E':
            print(f"  End   berada di : baris {i}, kolom {j}")
 
 
# ─────────────────────────────────────────────────────────────
# BAGIAN 6: LATIHAN MANDIRI
# ─────────────────────────────────────────────────────────────
#
#   soal_latihan = {
#       1: ("Matriks 5x5 acak – diagonal, jumlah, terbesar", "⭐ Mudah"),
#       2: ("Jadwal pelajaran (5 hari × 3 sesi)",            "⭐ Mudah"),
#       3: ("Fungsi jumlah_matriks(A, B)",                   "⭐⭐ Menengah"),
#       4: ("Matriks identitas NxN via list comprehension",  "⭐⭐ Menengah"),
#       5: ("Array 3D 3×3×3 berisi 1–27, tabel rapi",       "⭐⭐⭐ Menantang"),
#   }
# ─────────────────────────────────────────────────────────────
 
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
  Buat fungsi jumlah_matriks(A, B) yang menerima
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
 
# ── Contoh Solusi Soal 1 ─────────────────────────────────────
print("  [Contoh Solusi Soal 1]")
 
random.seed(42)
matriks_acak = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
 
print("\n  Matriks 5x5 acak :")
for baris in matriks_acak:
    print("  ", baris)
 
# a) Diagonal utama → elemen di mana baris == kolom
diagonal = [matriks_acak[i][i] for i in range(5)]
print(f"\n  a) Diagonal utama : {diagonal}")
 
# b) Jumlah seluruh elemen
total = sum(matriks_acak[i][j] for i in range(5) for j in range(5))
print(f"  b) Jumlah semua   : {total}")
 
# c) Nilai terbesar beserta posisinya
maks = matriks_acak[0][0]
pos  = (0, 0)
for i in range(5):
    for j in range(5):
        if matriks_acak[i][j] > maks:
            maks = matriks_acak[i][j]
            pos  = (i, j)
print(f"  c) Nilai terbesar : {maks} pada baris {pos[0]}, kolom {pos[1]}")
 
# ── Contoh Solusi Soal 3 (Bonus) ─────────────────────────────
print("\n  [Contoh Solusi Soal 3 – Fungsi jumlah_matriks]")
 
def jumlah_matriks(A, B):
    """Menjumlahkan dua matriks berukuran sama."""
    return [[A[i][j] + B[i][j]
             for j in range(len(A[0]))]
             for i in range(len(A))]
 
X = [[1, 2, 3], [4, 5, 6]]
Y = [[7, 8, 9], [1, 2, 3]]
print(f"  X           = {X}")
print(f"  Y           = {Y}")
print(f"  X + Y       = {jumlah_matriks(X, Y)}")
 
# ── Contoh Solusi Soal 4 (Bonus) ─────────────────────────────
print("\n  [Contoh Solusi Soal 4 – Matriks Identitas]")
 
N = 4
identitas = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
print(f"  Matriks identitas {N}x{N} :")
for baris in identitas:
    print("  ", baris)
 
# ── Contoh Solusi Soal 5 (Bonus) ─────────────────────────────
print("\n  [Contoh Solusi Soal 5 – Array 3D 3×3×3 berisi 1–27]")
 
angka   = 1
kubus   = [[[angka + i * 9 + j * 3 + k for k in range(3)]
                                         for j in range(3)]
                                         for i in range(3)]
for i, lapisan in enumerate(kubus):
    print(f"\n  Lapisan {i} :")
    for baris in lapisan:
        print("   ", baris)
 
# ── Selesai ──────────────────────────────────────────────────

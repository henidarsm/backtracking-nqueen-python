"""
===========================================
  Algoritma Backtracking - N-Queens Problem
  Mata Kuliah: Algoritma & Pemrograman
===========================================
  Deskripsi:
  Menempatkan N ratu pada papan N x N
  sehingga tidak ada ratu yang saling menyerang.
  (tidak boleh sebaris, sekolom, atau satu diagonal)
"""

import time

# ==============================
# KONFIGURASI
# ==============================
N = 4  # Ubah nilai N di sini (coba: 4, 5, 6)

board = [["." for _ in range(N)] for _ in range(N)]


# ==============================
# FUNGSI: Tampilkan Papan
# ==============================
def print_board():
    """Cetak kondisi papan saat ini ke layar"""
    print("  " + " ".join(str(i) for i in range(N)))   # header kolom
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()


# ==============================
# FUNGSI: Cek Posisi Aman
# ==============================
def is_safe(row, col):
    """
    Cek apakah posisi (row, col) aman untuk menaruh ratu.
    Cek 3 arah: kolom atas, diagonal kiri atas, diagonal kanan atas.
    """

    # Cek kolom — ada ratu di atas kolom ini?
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Cek diagonal kiri atas ( \ )
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Cek diagonal kanan atas ( / )
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True  # Aman!


# ==============================
# FUNGSI: Backtracking (INTI)
# ==============================
def solve(row):
    """
    Fungsi rekursif utama.
    Coba tempatkan ratu di setiap kolom pada baris 'row'.
    Jika gagal di semua kolom → return False (backtrack).
    """

    # BASE CASE: semua baris sudah diisi → solusi ditemukan
    if row == N:
        print("=" * 30)
        print("  SOLUSI DITEMUKAN!")
        print("=" * 30)
        print_board()
        return True

    # Coba setiap kolom di baris ini
    for col in range(N):

        print(f"  Mencoba ratu di baris {row}, kolom {col} ...")
        time.sleep(0.4)  # delay agar visualisasi terlihat

        if is_safe(row, col):

            # Taruh ratu
            board[row][col] = "Q"
            print(f"  >> Ratu ditempatkan di ({row}, {col})")
            print_board()
            time.sleep(0.4)

            # Rekursi: lanjut ke baris berikutnya
            if solve(row + 1):
                return True

            # Sampai sini = tidak ada solusi lanjutan → BACKTRACK
            board[row][col] = "."
            print(f"  << Backtracking dari ({row}, {col})")
            print_board()
            time.sleep(0.3)

        else:
            print(f"  XX Konflik di ({row}, {col}) — dilewati\n")

    # Semua kolom dicoba, tidak ada yang cocok
    return False


# ==============================
# PROGRAM UTAMA
# ==============================
if __name__ == "__main__":
    print()
    print("=" * 30)
    print(f"  N-Queens Problem  (N = {N})")
    print("=" * 30)
    print()
    print("  Papan awal:")
    print_board()
    time.sleep(0.5)

    hasil = solve(0)

    if not hasil:
        print(f"  Tidak ada solusi untuk N = {N}")

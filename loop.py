import time


database_musik = {
    "Mrs Green Apple": ["Inferno", "Soranji", "Attitude"],
    "Sheila On 7": ["Dan", "Film Favorit", "Seberapa Pantas"],
    "Yorushika": ["Sunny", "Paddle", "Parade"]}

print("=" * 40)
print("SELAMAT DATANG DI RADIO 010")
print("=" * 40)
time.sleep(1)

print("\nDaftar Band Musik:")
for band in database_musik:
    print(f" - {band}")

while True:
    pilihan_band = input("\nApa band yang ingin Anda pilih? ").title()
    if pilihan_band in database_musik:
        break
    print("Maaf, band tidak ada di daftar. Silakan ketik ulang.")

print("\nPilihan yang sempurna!")
time.sleep(1)

print(f"\nBerikut adalah daftar lagu dari {pilihan_band}:")
for lagu in database_musik[pilihan_band]:
    print(f" - {lagu}")

while True:
    pilihan_lagu = input("\nSilakan ketik judul lagu yang ingin diputar: ").title()
    if pilihan_lagu in database_musik[pilihan_band]:
        break
    print("Maaf, lagu tersebut tidak tersedia. Silakan ketik ulang.")

print("\nPilihan yang sangat tepat! Selamat mendengarkan.")
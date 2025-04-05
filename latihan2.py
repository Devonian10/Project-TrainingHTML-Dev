import math
x = int(5)
y = int(math.sqrt(25))
z = 'C'
print(f'Umur ku adalah', x)

# name = input("Tulis namamu : ")
# hp = int(input("Tulis HP kamu : "))
# atk = int(input("Tulis Atk kamu : "))
# em = int(input("Tulis EM kamu : "))
# spd = int(input("Tulis SPD kamu : "))

# print(f"Daftar kateogri sebagai berikut:")
# print(f"")
# choose = input("Pilih Kategori senjata (Polearm/Sword): ").strip()
# if (choose == 'Polearm'):
#     polearm = atk =- 100
#     res=print("LOL")
# elif(choose == 'Sword'):
#     sword = atk =- 100
#     res=sword

# monster = input("Pilih kategori monster (Slime/Hillicurl): ").strip()
# def calculate_damage(monster, atk, em):
#     if (monster == 'Slime'):
#         slime = 1000 - (atk - em)  # HP Slime dikurangi ATK dan ditambah EM
#         res1 = slime
#     elif (monster == 'Hillicurl'):
#         if (em != 0):
#             hillicurl = 1000 - (atk // em)  # Pembagian integer jika EM tidak nol
#         else:
#             hillicurl = 1000 - atk  # Jika EM nol, hanya dikurangi ATK
#         res1 = hillicurl
#     else: 
#         res1 = 1000  # Jika monster tidak dikenali, HP tetap 1000
#     return res1  
# hp_sisa = calculate_damage(monster, atk, em)
# print(f"HP {monster} setelah terkena serangan: {hp_sisa}")
# print(f'hasil atk adalah {res}', f' dan monster adalah {monster}')


menu = {
    'Nasi Goreng': 16000, 'Ayam Kampung': 20000, 'Ayam Goreng Lalapan': 22000, 
    'Capcay': 20000, 'Ikan Goreng Tepung': 25000, 'Cumi-cumi Goreng': 30000, 
    "Jus Alpukat": 15000, 'Jus Jeruk': 7000, 'Jus Apel': 10000, 'Jus Kelp': 30000, 'Ice Lemon Tea': 10000, 'Red Velvet':15000
}

money = int(input("Silahkan isi uangmu: "))

while True:
    print(f"\nMenu tersedia: {', '.join(menu.keys())}")
    pesanan = input("Pilih menu (atau ketik 'selesai' untuk mengakhiri): ").strip()
    
    if pesanan.lower() == 'selesai':
        break  # Keluar dari loop
    
    if pesanan not in menu:
        print("Menu tidak tersedia.")
        continue

    if money >= menu[pesanan]:
        money -= menu[pesanan]
        print(f"{pesanan} berhasil dipesan! Sisa uangmu: {money}")
    else:
        print("Uang tidak cukup.")

print(f"\nTransaksi selesai. Kembalian uang anda: {money}")

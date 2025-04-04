import math
x = int(5)
y = int(math.sqrt(25))
z = 'C'
print(f'Umur ku adalah', x)

name = input("Tulis namamu : ")
hp = int(input("Tulis HP kamu : "))
atk = int(input("Tulis Atk kamu : "))
em = int(input("Tulis EM kamu : "))
spd = int(input("Tulis SPD kamu : "))

print(f"Daftar kateogri sebagai berikut:")
print(f"")
choose = input("Pilih Kategori senjata (Polearm/Sword): ").strip()
if (choose == 'Polearm'):
    polearm = atk =- 100
    res=print("LOL")
elif(choose == 'Sword'):
    sword = atk =- 100
    res=sword

monster = input("Pilih kategori monster (Slime/Hillicurl): ").strip()
def calculate_damage(monster, atk, em):
    if (monster == 'Slime'):
        slime = 1000 - (atk - em)  # HP Slime dikurangi ATK dan ditambah EM
        res1 = slime
    elif (monster == 'Hillicurl'):
        if (em != 0):
            hillicurl = 1000 - (atk // em)  # Pembagian integer jika EM tidak nol
        else:
            hillicurl = 1000 - atk  # Jika EM nol, hanya dikurangi ATK
        res1 = hillicurl
    else: 
        res1 = 1000  # Jika monster tidak dikenali, HP tetap 1000
    return res1  
hp_sisa = calculate_damage(monster, atk, em)
print(f"HP {monster} setelah terkena serangan: {hp_sisa}")
print(f'hasil atk adalah {res}', f' dan monster adalah {monster}')




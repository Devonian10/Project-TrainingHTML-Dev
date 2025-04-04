name = "Devonian 10"

x = 1
y = 4
z = (x + y) + x / 2
print(z)

# print(x == 5 ^ x == 5)
x **= 4
print(x)

y %= 1
print(y)

for x in range (x, 21, 2):
    if x == 0:
        continue

print(x)

class Person :
    def __init__(self, name,age,score,nim):
        self.name = name
        self.age = age
        self.nim = nim
        self.score = score

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Nim: {self.nim}, Score: {self.score} "
p1 = Person("Devon", 24, 100, "H071191048")

print(p1.name)
print(p1.age)
print(p1.score)

hasil = [i for i in range(0,13,3) ]
print(hasil)

name2 = ('Devon', 'age', 24)

name3 = "Devonian"

print(f'{name3}')

money = int(input("Silahkan isi uangmu : "))
food = ['Nasi Goreng', 'Ayam Kampung', 'Ayam Goreng Lalapan', 'Capcay', 'Ikan Goreng Tepung', 'Cumi-cumi Goreng', 'Cumi-cumi Hitam', 'Ikan Bolu', 'Ikan Bakar']
price_food=(16000, 20000, 22000,20000,25000,30000, )
drink = ["Jus Alpukat", 'Jus Jeruk', 'Jus Apel', 'Jus Kelp']
price_drink = (15000, 7000, 10000, 30000)
res1 = []
menu = input("Silahkan pilih menu (food/drink) : ").strip()
#Ini untuk makanan
menu1 = input('Pilih Pemesanan anda : ').strip()
if (menu == 'food'): 
    if (menu1 == 'Nasi Goreng'):
        money -= price_food[0]
        res1 = money
    elif (menu1 == 'Ayam Kampung'):
        money -= price_food[1]
        res1 = money

    elif (menu1 == 'Ayam Goreng Lalapan'):
        money -=price_food[2]
        res1 = money

    elif (menu1 == 'Capcay'):
        money -= price_food[3]
        res1 = money
#Ini Untuk Minuman
elif (menu == 'drink'):
    if (menu1 == 'Jus Alpukat'):
        money -= price_drink[0]
        res1 = money
    elif (menu1 == 'Jus Apel'):
        money -= price_drink[1]
        res1 = money
    elif (menu1 == 'Jus Kelp'):
        money -= price_drink[2]
        res1 = money
else:
    print('Tidak ada kategori ')
print(f'Kembalian uang anda adalah {res1}')

import math
a = float(input('Masukkan angka a : '))
b = float(input('masukkan angka b : '))
c = float(input("Masukkan angka c : "))

r1 = math.pow(a, 2)
r2 = math.pow(b, 2)
r3 = math.pow(c, 2)

r4 = math.pow(a , 3)
r5 = math.pow(b , 3)
r6 = math.pow(c , 3)

luas_lingkaran = 3.14 * r1
volume_tabung = 3.14 * r4 
layang2 = (a * b) / c
print(f'{c}')
print(f'{layang2}')
print(luas_lingkaran)
print(volume_tabung)

print((a >= b and a <= c))


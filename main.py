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

for x in range(6):
    print("Angka")

for i in range(1, 20, 2):
    if i == 19:
        break
    print(i)

for i in range(3, 50, 3):
    if i == 21:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Hasil abis bagi 2 adalah ", i)

for i in range (2,22,3):
    if i % 2 != 0:
        break
    print(i)

x = 1
while x < 6:
  x += 1
  if x == 3:
    break
  print(x)

print("Hello World")

pi = 22/7
def calculateCircleArea(radius):
    area = pi * radius * radius
    return area

r = input("circle radius: ")
circleArea = calculateCircleArea(float(r))

print (f'circle area : {circleArea}' )

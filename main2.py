import math


x = float(input("Masukkan nilai X : "))
y = float(input("Masukkan Nilai Y : "))

name = str(input("Nama kamu : "))

def myFunct():
    print("Nama saya :", name)

def menghitung(x,y):
   
    return x ** y
    
myFunct()
hasil = menghitung(x,y)
print("Hasil nilai kamu adalah : " + str(hasil))

# Operator 
# operator = str(input('Pilih Operator : "Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", atau "Perpangkatan": '))

# number1 = float(input("masukkan nilai 1 : "))
# number2 = float(input("masukkan nilai 2 : "))

# if operator == 'Penjumlahan':
#     res = number1 + number2
# elif operator == 'Pengurangan':
#     res = number1 - number2
# elif operator == 'Perkalian' :
#     res = number1 * number2 
# elif operator == 'Pembagian' :
#     res = number1//number2
# elif operator == 'Perpangkatan' :
#     res = number1 ** number2

    
# print(f'{operator} dari {number1} dan {number2} adalah {res}')


#Bangun datar project sederhana hampir sama dengan diatas algoritma
dimentional = str(input('Pilih Luas bangun datar : "Persegi","Persegi Panjang", "Belah Ketupat", "Jajar Genjang", "Segitiga": '))
number3 = float(input("Masukkan nilai : "))
number4 = float(input("Masukkan nilai : "))
if dimentional == 'Persegi':
    res = math.pow(number3,2)
elif dimentional == 'Persegi Panjang':
    res = number3 * number4
elif dimentional == 'Belah Ketupat' :
    res =( number3 * number4 )/2
elif dimentional == 'Jajar Genjang' :
    res = number3 * number4
elif dimentional == 'Segitiga' :
    res = (number3*number4)/2

print(f'Luas {dimentional} pada bangun datar nilai 1: {number3} dan nilai 2: {number4} adalah {res} ')



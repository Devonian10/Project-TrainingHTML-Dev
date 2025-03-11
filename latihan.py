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


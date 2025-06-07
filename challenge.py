lower = 1
upper = 250
primes = []

for number in range (lower,upper+1):
    if number > 1:
        for i in range (2,number):
            if number % i == 0:
                #print(f'{number} bukan prima, karena {number} habis dibagi sama {i}')
                break
        else:   
         #no break occured _> number is prime 
         primes.append(str(number))

with open('result.txt', 'a') as f:

    f.write('\n'.join(primes))
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes=[]
for a in numbers:
    a = a - 1
    i = 0
    is_prime = False
    for b in numbers:
        b = b - 1
        if numbers[a] > 1 and numbers[b] > 1 and numbers[a] % numbers[b] == 0:
            is_prime = True
            i = i + 1
        if a == b or numbers[a] == 1:
            break
    if is_prime == True and numbers[a]!= 1 and i == 1:
        primes.append(numbers[a])
    elif numbers[a]!= 1:
        not_primes.append(numbers[a])
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
# Декораторы
def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        d = 2
        while total % d != 0:
            d += 1
        if (d == total) == True:
            print('Простое')
        else:
            print('Составное')
        return total
    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total

result = sum_three(2, 3, 6)
print(result)
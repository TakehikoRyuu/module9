# Декораторы
def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        d = 2
        for d in range(2, int(total**0.5) + 1):
            d += 1
        if (d == total) == True:
            print('Простое')
        else:
            print('Составное')
        return total
    return wrapper


@is_prime
def sum_three(*args):
    total = sum(args)
    return total

result = sum_three(2, 3, 6)
print(result)

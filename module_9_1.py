# Введение в функциональное программирование

def apply_all_func(int_list, *functions):
    result = {}
    for fun in functions:
        operation = (fun(int_list))
        result[fun.__name__] = operation
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
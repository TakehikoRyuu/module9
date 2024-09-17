# Генераторные сборки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = [len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s)]
print(first_result)
second_result = [len(first[f]) == len(second[f]) for f in range(len(first))]
print(second_result)
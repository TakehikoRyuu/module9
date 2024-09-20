# Генераторы
def all_variants(text):
    for r in range(len(text)):
        yield text[r]
    for r in range(len(text) - 1):
        result = text[r]
        r = r + 1
        result += text[r]
        yield result
    yield text


a = all_variants("abc")
for i in a:
    print(i)
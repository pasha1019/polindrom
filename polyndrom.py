# Определение полиндрома через кортеж
print('Введите слово')
text = input()
polyndrom = bool(text.find(text[::-1]) + 1)
if polyndrom is True:
    print('Введенное слово полиндром')
else:
    print('Введенное слово не полиндром')

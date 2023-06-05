# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 19

text = set('''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''.lower().strip('.?,!\n').replace('.', ' ').split())

# text = set(text)
print(text)
print(f'Количество расличных слов в тексте = {len(text)}')

# Метод string lower() преобразует все символы верхнего регистра в строке в символы нижнего регистра и возвращает их
# Метод strip() возвращает копию строки, удаляя как начальные, так и конечные символы
# (в зависимости от переданного строкового аргумента)
# Метод replace() возвращает копию строки, в которой заменены все вхождения указанной строки указанным значением
# Функция split() сканирует всю строку и разделяет ее в случае нахождения разделителя
# (пробел - разделитель по умолчанию)

# Другой способ в одну строку:
print(len(set(input('Enter text: ').lower().split())))
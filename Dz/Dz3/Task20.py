#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

dict_en = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 
           'FHVWY': 4, 'K': 5 , 'JX': 8, 'QZ': 10}
dict_ru = {'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 
           'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

en = 'QWERTYUIOPASDFGHJKLZXCVBNM'
ru = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
result = 0
word = input('Enter word: ').upper()

if word[0] in en:
    for i in word:
        for k, v in dict_en.items():
            if i in k:
                result += v
    print(f'Word {word} worth {result} points')

if word[0] in ru:
    for i in word:
        for k, v in dict_ru.items():
            if i in k:
                result += v
    print(f'Слово {word} стоит {result} очков')

# Сложность первым способом = O(n^2), 
# поэтому лучше решить эту задачу через конструкцию re.sub() (сложность O(n)):

# import re

# dict_eng = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3', 
#            '[FHVWY]': '4', '[K]': '5' , '[JX]': '8', '[QZ]': '10'}
# dict_rus = {'[АВЕИНОРСТ]': '1', '[ДКЛМПУ]': '2', '[БГЁЬЯ]': '3', 
#            '[ЙЫ]': '4', '[ЖЗХЦЧ]': '5', '[ШЭЮ]': '8', '[ФЩЪ]': '10'}

# word = input('Enter word: ').upper()

# if word[0] in en:
#     for i in dict_eng:
#         word = re.sub(i, dict_eng[i], word)
#     print(sum(map(int, word)))

# if word[0] in ru:
#     for i in dict_rus:
#         word = re.sub(i, dict_rus[i], word)
#     print(sum(map(int, word)))
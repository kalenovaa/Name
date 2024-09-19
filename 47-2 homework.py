# from itertools import count
#     latiniza = 'qwertyuiopasdfghjkllzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     kirilica = 'йцукенгшщзхъёфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
#     galsnie = 'eyuoaiEIYUOAуеёыаоэяиюЕУЫАОЭЯИЮ'
# a = input('введите любое слово: ')
# count = 0
# while True:
#     for letter in latiniza:
#         if letter in latiniza:
#             count += 1


glasnie = "аеёиоуыэюяaeiou"
vsebukvy = "бвгджзклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

while True:
    slovo = input("введите слово, для выхода напишите выход: ").strip()
    if slovo.lower() == 'выход':
        break

    vsegoslov = len(slovo)
    vowels_count = sum(1 for char in slovo if char.lower() in glasnie)
    consonants_count = sum(1 for char in slovo if char.lower() in vsebukvy)

    print(f"количество букв: {vsegoslov}")
    print(f"гласные: {vowels_count}")
    print(f"согласные: {consonants_count}")

    if vsegoslov > 0:
        vowels_percentage = (vowels_count / vsegoslov) * 100
        consonants_percentage = (consonants_count / vsegoslov) * 100
        print(f"гласные/согласные: {vowels_percentage:.2f}% /{consonants_percentage:.2f}%")
    else:
        print("слово не содержит букв.")


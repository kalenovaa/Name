#операторы: принадлежности, назначения, циклы
#
#
# '''операторы назначения'''
# number = 5
# number += 5
# number **= 2
# number //= 4
# number -= 15
# print(number)
#
# '''операторы: принадлежности'''
#
# word = 'geeks'
# print('o' in word)
# print('e' in word)
# print('t' not in word)
# print('s' not in word)

#
# """циклы"""
# counter = 0
# while counter <= 50:
#     if counter == 40:
#         print('stop')
#         break
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print('geeks', counter)
#

#
# rounds = int(input("how many do you want? "))
#
# while rounds > 0:
#     time = input(f'enter time: ({rounds})').lower()
#     if time in 'exit stop':
#         break
#     if time == 'утро' or time == 'morning':
#         print('good morning')
#     elif time == 'день' or time == 'day':
#         print('good day')
#     elif time == 'вечер' or time == 'evening':
#         print('good evening')
#     else:
#         print('idk the time')
#     rounds -= 1

word = 'ilublusvoegokota'

for letter in word:
    if letter == 'v':
        break
    if letter in 'kota':
        continue
    print(letter)


    












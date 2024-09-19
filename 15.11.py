# def countGrades(g1, g2, g3):
#   avg = (g1 + g2 +g3) / 3
#   result = ''
#   if avg > 95:
#       result = 'A+'
#   elif 85 < avg < 95:
#       result = 'A'
#   elif 65 < avg < 85:
#       result = 'B'
#   else:
#       result = 'C'
#   return result
#
# print(countGrades(67, 45, 89))

# def longSentence(txt):
#     words = txt.split()
#     maks = 0
#     for i, v in enumerate(words):
#         if len(v) > len(words[maks]):
#             maks = i
#     return words[maks]
# print(longSentence('hello everybody i hope i will go home soon'))

# def reverseSent(txt):
#     words = txt.split()
#     res = ''
#     for i, v in enumerate(words):
#         res += ''.join(reversed(list(v))) + ' '
#     return res
#     # sent = 'hello everybody i hope i will go home soon'
#     # print(revs)
# print(reverseSent('hello everybody i hope i will go home soon'))
def add_student(student_list, groups):
    name = input('write your name: ')
    surname = input('write your surname: ')
    age = int(input('write your age: '))
    for i,v in enumerate(groups):
        print(f'{i + 1}: ', v)
    group_index = int(input('choose your group '))
    student_list.append({'name':name,'surname': surname,'age': age, 'group': groups})
    return name, surname, age, groups


def main():
    groups = ['sca23', 'csc23', 'aco23', 'mar23']
    students = [
        {'name': 'John','surname': 'Smith','age': 19, 'group': 'sca23'
        }]
    print(students)
    add_student(students, groups)
    print(students)

if __name__ == '__main__':
    main()
# def dublicate_letters(word):
#     res = ''
#     for i, v in enumerate(word):
#         res += v * (i + 1)
#     print(res)
# dublicate_letters('hello')

# def maxWord(arr):
#     maxx = arr[0]
#     for n in arr:
#         if n > maxx:
#             maxx = n
#             return maxx
#         print(maxWord([34, 5, 456,7 ,6, 5,]))














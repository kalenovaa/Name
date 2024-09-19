# import random
# def main():
#     secret_number = random.randint(0,100)
#     counter = 0
#     while True:
#         guess = int(input('write number:'))
#         if guess > secret_number:
#             print('your number is too big')
#         else:
#             print('your number is too small')
#         if guess == secret_number:
#             print('you won')
#         else:
#             print('try again')
#             counter += 1
#         if counter >= 10:
#             break
#
# def isDone():
#     answer = input('do you want to continue (y/n)')
#     return True if answer == 'yes' else False
#
# if __name__ == '__main__':
#     main()
#
# import random
#
# import random
# def main():
#     while True:
#         secret_number = random.randint(1, 10)
#         counter = 0
#         while True:
#             try:
#                 guess = int(input('write number:'))
#                 counter += 1
#                 if guess == secret_number:
#                     print(f"Congratulations! You guessed the number {secret_number} in {counter} attempts")
#                     break
#                 elif guess < secret_number:
#                     print('your number is too big')
#                 else:
#                     print('your number is too small')
#             except ValueError:
#                 print('Please enter an integer.')
#
#         play_again = input('do you want to continue (y/n):')
#         if play_again.lower() != 'no':
#             break
#
# if __name__ == "__main__":
#     main()
#
# def main():
#     balance = 1000
#     login = 'rebellion'
#     password = 'qwerty'
#     database = {'login': 'rebellion', 'password': 'qwerty', 'balance': '1000'}
#     while True:
#         if input('enter login') == database['login'] and input('enter password') == database['password']:
#             act = input('choose action 1 - show balance, 2 - withdraw, 3 - deposit, 4 - exit')
#             if act == '1':
#                 show_balance(balance)
#             elif act == "2":
#                 money = int(input('how much do u want to draw'))
#                 balance = balance - money
#                 show_balance(balance)
#             elif act == "3":
#                 cash = int(input('how much do u want to put on deposit'))
#                 deposit = balance + cash
#                 show_balance(deposit)
#             elif act == '4':
#                  break
#             else:
#                 print('read correctly')
#         else:
#             print('login or password wrong')
#
#
# def show_balance(balance):
#     print(f'your balance is {balance}')
#
# if __name__ == '__main__':
#      main()
#

#
# def randomPicker(word_list):
#     return random.choice(word_list)
#
# def displayBoard(secret_word):
#     n = '_' * len(secret_word)
#     print(n)
# import random
#
# num_count = 3
#
#
# def main():
#     num_string = '123456789'
#     number_list = list(num_string)
#     random.shuffle(number_list)
#     number = ''
#     # number = number_list[0] + number_list[1] + number_list[2]
#     for i in range(3):
#         number += number_list[i]
#         guess = int(input('guess the number: '))
#         clues = []
#         for i, v in enumerate(guess):
#             if v == number[i]:
#                 clues.append('fermi')
#             elif v in number:
#                 clues.append('bagles')
#
#         if guess == int(number):
#             print('you guess correct')
#         else:
#             print('you guess wrong')
#         print(number)
#
#
# if __name__ == '__main__':
#     main()

# for i in num_string(3):
#     num_string.append(int(i))
#     print(num_string)
#     guess = 0
#     if num_string == guess:
#         print('you guess correct')
#     else:
#         print('you did it wrong')

# number_list = ['1', '2', '3', '4']
# int_num_list = []
# for i in number_list:
#     int_num_list.append(int(i))
#     print(int_num_list)

# l = ['mehmed', 'ali', 'aisa', 'berk', 'amina', 'akich', 'spezz']
# secret_word = randomPicker(l)
# displayBoard(secret_word)
# error_count = 0
# attempts = 0
# while True:
#     guess = input('try to guess a letter: ')
#     if guess in secret_word:
#         attempts += 1
#     else:
#         error_count += 1

# if 'a' in l:
#     print('he is here')
#
#
# def randomWord(name_list):
# word_list = sentence.split(' ')
# # word_index = random.randint(0, len(word_list) -1)
# print(word_list[word_index])
#     return random.choice(name_list)
#
# def main():
#     secret_word = randomWord(l)
#     n = len(secret_word)
#     print(secret_word)
#     print('_' * n)
#     for i in range(5):
#         guess = input('guess letter: ')
#         if guess in secret_word:
#             print('letter exist')
#         else:
#             print('there is no letter')
#
# if __name__ == '__main__':
#     main()

# for i in range(5):
#     print(randomWord(n))

# import random
# a = []
# for i in range(10):
#     a.append(random.randint(0, 100))
# print(a)
# l = [12, 23, 30, 45, 5, 10, 67, 6]
# p = []
# b = []
#
#
# for a in l:
#     if a % 5 == 0:
#         p.append(a)
#     else:
#         b.append(a)
# print(p)
# print(b)

# yes = True
# count = 0
# def isCoun():
#     ans = input('do u want to add a num?')
#     if ans == 'yes':
#         return True
#     else:
#         return False
# while yes:
#     a,b = int(input('write num')),int(input('write second num'))
#     if a % b == 0:
#             print('its ok')
#     else:
#             print('its not ok')
#     yes = isCoun()

# isDone = True
# for i in range(2):
#     a, b = int(input('write first num: ')), int(input('write second num: '))
# if a % b == 0:
#     print('its ok')
# else:
#     print('its not ok')

# def isCont():
#     ans = input('do u want to add a num?')
#     if ans == 'yes':
#         return True
#     else:
#         return False

# def calc(op):
#     b = int(input('write first'))
#     c = int(input('write second'))
#     if op == "+":
#         return c + b
#     elif op == '_':
#         return b - c

# def main():
#     while True:
#         op = input('choose op or q')
#         result = calc(op)
#         if result == 'quit':
#             break
#         print(result)
#
# if __name__ == "__main__":
#     main()
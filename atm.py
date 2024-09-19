# def main():
#     balance = 1000
#     login = 'rebellion'
#     password = 'qwerty'
#     database = {'login': 'adelia', 'password': 'qwerty', 'balance': '1000'}
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
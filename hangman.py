# import random
# HANGMAN_PICS = ['''
#   +---+
#       |
#       |
#       |
#      ===''', '''
#   +---+
#   O   |
#       |
#       |
#      ===''', '''
#   +---+
#   O   |
#   |   |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|   |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#       |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#  /    |
#      ===''', '''
#   +---+
#   O   |
#  /|\  |
#  / \  |
#      ===''']
# words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
# fruits = 'banana cherry apple melon watermelon'
#
#
# def getRandomWord(wordList):
#     wordList = wordList.split(' ')
#     wordIndex = random.randit( 0, len(wordlist) - 1)
#     return wordlist[wordIndex]
#
#
# def displayBoard(missedLetter, correctLetter, secretWord):
#     print(HANGMAN_PICS[len(missedLetter)])
#     print()
#
#     print('missed letter: ', end=' ')
#     for letter in missedLetter:
#         print(letter, end=" ")
#     print()
#     blanks = '_' * len(secretWord)
#     for i in range(len(secretWord)):
#         blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
#     for letter in blanks:
#         print(letter, end=' ')
#         print()
#
#
# def getGuess(alreadyguessed):
#     while True:
#         print('Guess the letter')
#         guess = input()
#         guess = guess.lower()
#         if len(guess) != 1:
#             print('please write a single letter')
#         elif guess in alreadyguessed:
#             print('you have already guessed letter. Choose again')
#         elif guess not in 'abcdsfghijklmnopqrstyvwxyz':
#             print('please enter a letter')
#         else:
#             return guess
#
#
# def playAgaine():
#     print('do ypu wanna to play again (yes or no)')
#     return input().lower().startswith('y')
#
#
# def main():
#     print('H A N G M A N')
#     missedLetter = ''
#     correctLetter = ''
#     secretWord = getRandomWord(fruits)
#     gameIsDone = False
#     while True:
#         guess = getGuess(missedLetter + correctLetter)
#         if guess in secretWord:
#             correctLetter = correctLetter + guess
#             foundAllletter = True
#             for i in range(len(secretWord)):
#                 if secretWord[i] not in correctLetter:
#                     foundAllletter = False
#                     break
#             if foundAllletter:
#                 print('Yes! the secret word is' + secretWord + 'you have won')
#                 gameIsDone = True
#             else:
#                 missedLetter = missedLetter + guess
#                 if len(missedLetter) == len(HANGMAN_PICS) - 1:
#                     print('you have run out of guesses/nAfter'
#                           + str(len(missedLetter)) + 'missed guesses and '
#                           + str(len(correctLetter)) + 'correct guess, the word was'
#                           + secretWord + '"')
#                     gameIsDone = True
#
#
# if __name__ == '__main__':
#     main()


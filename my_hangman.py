from copy import copy
import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_random_word(word_list):
    word = word_list[random.randint(0, len(words) - 1)]
    print(word)
    return word

def show_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    # print("HANGMAN")
    # print("Missed letters", end=' ')
    # print('_ ' * len(secret_word))
    # print(HANGMANPICS[0])

    blanks_shown = '_' * len(secret_word)
    hangmanpics = copy(HANGMANPICS)
    #pic_index = 0
    print(' '.join(list(blanks_shown)))

    while hangmanpics:
    #while len(hangmanpics) != pic_index:
        guess = input("Guess the letter: ")
        if guess in secret_word:
            correct_letters += guess
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    blanks_shown = blanks_shown[:i] + secret_word[i] + blanks_shown[i+1:]
            print(' '.join(list(blanks_shown)))
        else:
            missed_letters += guess
            print (hangmanpics.pop(0))
            #print (hangmanpics[pic_index])
            #pic_index += 1
            print('Missed letters:' + ', '.join(list(missed_letters)))
        if '_' not in blanks_shown:
            print('You have won! The secret word is ' + secret_word)
            # We won exit from while
            break

    if playAgain():
        start_game()


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def start_game():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''

    secret_word = get_random_word(words)
    show_board(HANGMANPICS, missed_letters, correct_letters, secret_word)


start_game()



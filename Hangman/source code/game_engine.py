"""
2024/12/01
David Hamilton, Owen Dunken, James Jang

This file contains the GameRound class.
The GameRound is a custom object type for a single round of hangman.
"""

from random_word_generator import *

class GameRound:
    def __init__(self, theme):
        self._theme = theme
        self._word = game_choice(self._theme)
        self._word_list = list(self._word)
        self._word_length = len(self._word)
        self._user_word = "_" * self._word_length
        self._user_word_list = list(self._user_word)
        self._num_of_misses = 0
        self._alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self._hangman_default = ("  ____  \n"
                                 " |    | \n"
                                 " |      \n"
                                 " |      \n"
                                 " |      \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss1 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |      \n"
                                 " |      \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss2 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |    | \n"
                                 " |      \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss3 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |   /| \n"
                                 " |      \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss4 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |   /|\\\n"
                                 " |      \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss5 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |   /|\\\n"
                                 " |   /  \n"
                                 " |      \n"
                                 "_|_     ")
        self._hangman_miss6 = ("  ____  \n"
                                 " |    | \n"
                                 " |    O \n"
                                 " |   /|\\\n"
                                 " |   / \\\n"
                                 " |      \n"
                                 "_|_     ")

    def take_guess(self, guess):
        user_input = guess
        if len(user_input) == 1:
            if user_input.upper() not in self._alphabet_list:
                pass
            else:
                for index, character in enumerate(self._alphabet_list):
                    if character == user_input.upper():
                        self._alphabet_list[index] = " "
            if user_input.lower() in self._word:
                for position, character in enumerate(self._word_list):
                    if user_input.lower() == character:
                        self._user_word_list[position] = character
                        self._user_word = ''.join(self._user_word_list)
                if "_" not in self._user_word_list:
                    return "WIN"
            else:
                self._num_of_misses += 1
                if self._num_of_misses == 6:
                    return "GAME OVER"
        elif len(user_input) > 1:
            if user_input.lower() == self._word:
                print('Correct!')
                return "WIN"
            else:
                print('Incorrect')
                self._num_of_misses += 1

    def get_num_of_misses(self):
        return self._num_of_misses
    
    def get_user_word(self):
        user_word = ' '.join(self._user_word_list)
        return user_word
    
    def get_hangman_drawing(self):
        if self._num_of_misses == 0:
            return self._hangman_default
        elif self._num_of_misses == 1:
            return self._hangman_miss1
        elif self._num_of_misses == 2:
            return self._hangman_miss2
        elif self._num_of_misses == 3:
            return self._hangman_miss3
        elif self._num_of_misses == 4:
            return self._hangman_miss4
        elif self._num_of_misses == 5:
            return self._hangman_miss5
        elif self._num_of_misses == 6:
            return self._hangman_miss6


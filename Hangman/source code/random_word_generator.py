"""
2024/12/01
David Hamilton, Owen Dunken, James Jang

This file contains functions for 
    1. reading an external csv file (a list of words in a single theme).
    2. returning a random word from the list.
"""

import csv
import random

#imports values from csv files
def import_file(file):
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        values = list(csv_reader)
        random_value = random.choice(values)[0]       
    return random_value

#allows user to choose which file list they want to play
def game_choice(choice):
    if choice == 'cities':
        #hangman_value = import_file('C:\\Users\\james\\Documents\\CIS121\\PythonPrograms\\CIS121 Hangman\\cities.csv')
        hangman_value = import_file('word_bank\\cities.csv')
    elif choice == 'colors':
        #hangman_value = import_file('C:\\Users\\james\\Documents\\CIS121\\PythonPrograms\\CIS121 Hangman\\colors.csv')
        hangman_value = import_file('word_bank\\colors.csv')
    elif choice == 'fruit':
        #hangman_value = import_file('C:\\Users\\james\\Documents\\CIS121\\PythonPrograms\\CIS121 Hangman\\fruit.csv')
        hangman_value = import_file('word_bank\\fruit.csv')
    elif choice == 'teams':
        #hangman_value = import_file('C:\\Users\\james\\Documents\\CIS121\\PythonPrograms\\CIS121 Hangman\\teams.csv')
        hangman_value = import_file('word_bank\\teams.csv')
    return hangman_value

if __name__ == "__main__":
    user_choise = input("Sections: cities, colors, fruits, teams\n")
    print(game_choice(user_choise))

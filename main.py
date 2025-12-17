
import pandas as pd
#student_data_frame = pd.DataFrame(student_dict)

nato_phonetic_code = pd.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_code.iterrows()}
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
user_input_letters = [phonetic_dict[letter] for letter in user_input.upper()]
print(user_input_letters)


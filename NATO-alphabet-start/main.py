import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


word = input("Enter a word: ").upper()
word_list = [nato_dict[letter] for letter in word]
print(word_list)

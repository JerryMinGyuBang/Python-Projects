import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(word_list)


generate_phonetic()
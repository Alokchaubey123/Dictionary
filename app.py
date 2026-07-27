import json
from difflib import get_close_matches

file = open("environmental_thesaurus_40k.json", "r", encoding="utf-8")
data = json.load(file)
file.close()


def search(word):
    word = word.lower().strip()

    if word in data:
        return data[word], word

    guess = get_close_matches(word, data.keys(), 1, 0.8)

    if len(guess) > 0:
        ans = input("Did you mean " + guess[0] + "? (Y/N): ")

        if ans.lower() == "y":
            return data[guess[0]], guess[0]

    return None, None


def display(info, word):

    if info == None:
        print("Word not found.")
        return

    print()
    print("Word:", word)

    if "definition" in info:
        print("Definition:", info["definition"])


print("Environmental Thesaurus")
print("Type exit to stop.")

while True:

    text = input("Enter a word: ")

    if text.lower() == "exit":
        break

    if text.strip() == "":
        continue

    result, found = search(text)

    if result:
        display(result, found)
    else:
        print("Word not found.\n")
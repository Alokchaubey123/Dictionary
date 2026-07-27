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


print("Environmental Thesaurus")
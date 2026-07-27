import json
from difflib import get_close_matches

with open("environmental_thesaurus_40k.json", "r", encoding="utf-8") as file:
    data = json.load(file)

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

    if "synonyms" in info:
        if len(info["synonyms"]) > 0:
            print("Synonyms:", ", ".join(info["synonyms"]))

    if "antonyms" in info:
        if len(info["antonyms"]) > 0:
            print("Antonyms:", ", ".join(info["antonyms"]))

    if "example_sentences" in info:
        if len(info["example_sentences"]) > 0:
            print("Examples:")
            for sentence in info["example_sentences"][:2]:
                print("-", sentence)

    if "related_terms" in info:
        if len(info["related_terms"]) > 0:
            print("Related Terms:", ", ".join(info["related_terms"][:5]))

    if "difficulty" in info:
        print("Difficulty:", info["difficulty"])

    if "category" in info:
        print("Category:", info["category"])

    print()

    


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
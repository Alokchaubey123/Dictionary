import json

file = open("environmental_thesaurus_40k.json", "r", encoding="utf-8")
data = json.load(file)
file.close()


def search(word):
    word = word.lower().strip()

    if word in data:
        return data[word], word

    return None, None


print("Environmental Thesaurus")
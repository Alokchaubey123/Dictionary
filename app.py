import json

file = open("environmental_thesaurus_40k.json", "r", encoding="utf-8")
data = json.load(file)
file.close()

print("Environmental Thesaurus")
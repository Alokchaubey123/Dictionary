# Environmental Thesaurus

## About
A simple Python command-line Environmental Thesaurus that lets users search for environmental terms and view their definition, synonyms, antonyms, examples, related terms, difficulty level, and category. The data is stored in a JSON file, making it easy to update. It also suggests the correct spelling for misspelled words using `difflib`.

## Features
- Search environmental terms
- View definitions, synonyms, antonyms, and examples
- Display related terms, difficulty, and category
- Spelling suggestions for incorrect words
- Runs until the user types `exit`

## Project Structure
```text
Dictinary/
├── app.py
├── environmental_thesaurus_40k.json
└── README.md
```

## Modules Used
- `json` – Reads data from the JSON file
- `difflib` – Suggests similar words

## How to Run
1. Make sure Python is installed.
2. Keep `app.py` and `environmental_thesaurus_40k.json` in the same folder.
3. Run:
   ```bash
   python app.py
   ```

## Example
```text
Enter a word: climate

Definition: The long-term pattern of weather in a particular area.
Synonyms: weather pattern, atmosphere
Category: Climate Science
```

## Future Improvements
- Search by category
- Save search history
- Add new words
- Build a GUI
- Support partial word search

## License
This project is for educational purposes.
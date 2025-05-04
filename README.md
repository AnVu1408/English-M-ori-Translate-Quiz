# English-Maori-Translate-Quiz
Here's a `README.md` file you can include in your GitHub repository to describe your Māori language quiz program using Python and VSCode:

---

# 🧠 Māori Language Quiz (Reo Māori Translator)

This is a simple command-line quiz program written in **Python** using **VSCode** that helps users practice translating English terms into **Te Reo Māori**.

The quiz works by reading a list of Māori words from a text file, prompting the user to provide the correct translation, and scoring their performance.

## 📂 Project Structure

```
.
├── main.py           
├── days.txt        
├── numbers.txt        
├── places.txt        
└── README.md        
```

## ▶️ How It Works

* When you run the program, you'll be asked:

  ```
  Please enter a filename:
  ```

* Provide the name of one of the word files, e.g., `words.txt`.

* If the file contains at least one term, the program will start the quiz:

  ```
  Kia ora, you have 3 terms to translate today :-)
  en: dance
  mi: 
  ```

* You'll enter your answer. If correct, you'll see:

  ```
  Ka pai
  ```

  Otherwise, it will show a masked hint using:

  ```
  A: *a***a**
  ```

* You will repeat until you translate all terms correctly.

* At the end, you'll receive the score:

  ```
  You translated all the terms!
  You scored 66.67%
  ```

If the file contains no terms, it will display:

```
We can't play, hōhā!
```

## 🧪 Testing & Development Notes

* Developed incrementally in **Python** using **Visual Studio Code**.
* Designed to be tested with different `.txt` word lists.
* The user should **not enter a translation longer than the target Māori word**—these won't be tested.

## 📝 Example Word Files

Four word files are included so users can experiment:

* `words.txt`
* `days.txt`
* `numbers.txt`
* `places.txt`

Each file contains Māori terms to be translated.

Example:

```
kunikuni
ingoa
kanikani
```

## 🛠 Requirements

* Python 3.x
* VSCode (or any editor of choice)

## 🚀 Run It

Run the script using:

```bash
python main.py
```

---



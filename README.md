# 🧠 Tokenizer Comparison Visualizer

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![Status](https://img.shields.io/badge/Project-Learning-orange)

A simple Python project that demonstrates how different NLP tokenizers split the same input text into tokens.

This script compares tokenizers used by modern language models such as **BERT, GPT-2, GPT-4 tokenizers, and T5**, and prints tokens in **color-coded blocks** in the terminal so token boundaries are easy to see.

---

## 📌 Why This Project Exists

When working with **LLMs, embeddings, or prompt engineering**, everything is measured in **tokens**.

Most developers never actually see how text is converted into tokens.
This project helps visualize that process.

It helps you understand:

* How tokenization works
* Why token counts differ between models
* Why prompt costs vary between APIs
* How casing, unicode, numbers, and symbols affect tokenization

---

## 🧩 Tokenizers Compared

This script compares the following tokenizers from HuggingFace Transformers:

| Model                  | Tokenization Type      |
| ---------------------- | ---------------------- |
| `bert-base-cased`      | WordPiece              |
| `bert-base-uncased`    | WordPiece (lowercased) |
| `gpt2`                 | Byte Pair Encoding     |
| `google/flan-t5-small` | SentencePiece          |
| `Xenova/gpt-4`         | GPT-style tokenizer    |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/tokenizer-visualizer.git
cd tokenizer-visualizer
```

Install required dependencies:

```bash
pip install transformers
```

(Optional but recommended)

```bash
pip install torch
```

---

## 🚀 Usage

Run the script:

```bash
python tokenizer_visualizer.py
```

The program will tokenize the input text using different tokenizers and display tokens in colored blocks in the terminal.

---

## ✏️ Example Input Text

The script tests tokenizers using a mixed input containing uppercase text, unicode characters, emojis, operators, numbers, and whitespace.

```
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
```

---

## 🖥 Example Output

```
Tokenizer: bert-base-cased
Vocab length: 28996

[CLS] English and CAPITALIZATION 🎵 鸟 show_tokens False None elif == >= else
```

Each token is printed with a different background color to make token boundaries visible.

---

## 🧪 How It Works

### Load Tokenizer

```python
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
```

### Convert Text to Token IDs

```python
token_ids = tokenizer(sentence).input_ids
```

### Decode Token IDs

```python
tokenizer.decode(token_id)
```

### Display Colored Tokens

The script prints tokens using ANSI terminal color codes so each token appears with a different background color.

---

## 📂 Project Structure

```
tokenizer-visualizer
│
├── tokenizer_visualizer.py
└── README.md
```

---

## 💡 Why Tokenization Matters

Understanding tokenization is important because it affects:

* LLM API costs (tokens = cost)
* Prompt length limits
* Model performance
* Embedding quality

Different models tokenize the same text very differently.

---

## 🔮 Future Improvements

Possible enhancements include:

* Token count comparison table
* Web-based visualization UI
* Support for more models (LLaMA, Mistral, Claude)
* Token statistics and analysis
* Token cost estimation

---

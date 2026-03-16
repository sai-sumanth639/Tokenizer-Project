Tokenizer Comparison Visualizer

This project demonstrates how different NLP tokenizers break down the same input text into tokens. It helps visualize how models like BERT, GPT-2, T5, and GPT-4 tokenizers interpret text differently.

The script prints tokens in color-coded format in the terminal so you can easily observe token boundaries.

Project Overview

Natural Language Processing models do not understand raw text directly.
Instead, they convert text into tokens (smaller pieces of text) and then map them to token IDs.

Different models use different tokenization strategies such as:

WordPiece (BERT)

Byte Pair Encoding (GPT-2)

SentencePiece (T5)

Other modern tokenizers

This project compares these tokenizers using the same input text.

Features

Tokenizes text using multiple popular models

Displays token IDs

Decodes tokens back into readable text

Shows tokens in colored blocks for easy visualization

Compares tokenization across different models

Tokenizers Used

The script currently compares the following tokenizers:

bert-base-cased

bert-base-uncased

Xenova/gpt-4

gpt2

google/flan-t5-small

Installation

Clone the repository:

git clone https://github.com/your-username/tokenizer-visualizer.git
cd tokenizer-visualizer

Install dependencies:

pip install transformers

(Optional but recommended)

pip install torch
Usage

Run the script:

python tokenizer_visualizer.py

Example input text inside the script:

English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
Example Output
Tokenizer: bert-base-cased
Vocab length: 28996

[CLS] English and CAPITALIZATION 🎵 鸟 show _ tokens ...

Each token is displayed with a different background color in the terminal.

How It Works

Load tokenizer using HuggingFace Transformers

AutoTokenizer.from_pretrained("bert-base-cased")

Convert sentence into token IDs

token_ids = tokenizer(sentence).input_ids

Decode tokens back to text

tokenizer.decode(token_id)

Print tokens with ANSI colored backgrounds.

Project Structure
tokenizer-visualizer
│
├── tokenizer_visualizer.py
└── README.md
Why This Is Useful

Understanding tokenization helps with:

Prompt engineering

LLM cost estimation (tokens = cost)

Debugging NLP models

Learning how transformers process text

Example Learning Insight

The same sentence may produce very different token counts depending on the tokenizer.
This directly impacts model performance, latency, and API cost.

Future Improvements

Possible enhancements:

Token count comparison table

Visualization in a web UI

Token length statistics

Support for more models (LLaMA, Mistral, Claude)

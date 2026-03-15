# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer


# Sentence to tokenize
sentence = "Hello world!"


# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# Convert sentence into token IDs
token_ids = tokenizer(sentence).input_ids

print("Token IDs:", token_ids)



# Decode each token ID back to word/token
for token_id in token_ids:
    print(tokenizer.decode(token_id))

# Colors for tokens
colors = [
    '102;194;165', '252;141;98', '141;160;203',
    '231;138;195', '166;216;84', '255;217;47'
]


def show_tokens(sentence: str, tokenizer_name: str):
    """Show tokens in different colors"""

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    token_ids = tokenizer(sentence).input_ids

    print(f"\nTokenizer: {tokenizer_name}")
    print(f"Vocab length: {len(tokenizer)}\n")

    for idx, token_id in enumerate(token_ids):
        print(
            f'\x1b[0;30;48;2;{colors[idx % len(colors)]}m'
            + tokenizer.decode(token_id)
            + '\x1b[0m',
            end=' '
        )

    print("\n")

text = """
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
"""

show_tokens(text, "bert-base-cased")

show_tokens(text, "bert-base-uncased")

show_tokens(text, "Xenova/gpt-4")

show_tokens(text, "gpt2")

show_tokens(text, "google/flan-t5-small")
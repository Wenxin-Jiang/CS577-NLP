import re
from loguru import logger

import re
import torch
from transformers import DistilBertTokenizer, DistilBertModel


def remove_code_snippets(text):
    return re.sub(r'```.*?```', '', text, flags=re.DOTALL)


def remove_tables(text):
    def replace_table(match):
        header = re.findall(r'\|([^|\n]+)\|', match.group(0))
        values = re.findall(r'\|([^|\n]+)\|', match.group(0)[match.end(1):])
        return "\n".join(header + values)

    return re.sub(r'(\|.*\|\n\|:?-+:?\|.*\n)((\|.*\|(\n)?)+)', replace_table, text, flags=re.MULTILINE)


def remove_urls(text):
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)


def parse_readme(readme):
    main_text = re.sub(r"---\n.+?\n---", "", readme, flags=re.DOTALL).strip()
    main_text = remove_code_snippets(main_text)
    main_text = remove_tables(main_text)
    main_text = remove_urls(main_text)
    return main_text


def load_readme(readme_path):
    with open(readme_path, "r") as f:
        readme = f.read()
    main_text = parse_readme(readme)
    return main_text


def get_embeddings(text):
    # Load the pre-trained DistilBERT model and tokenizer
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertModel.from_pretrained('distilbert-base-uncased')

    # Tokenize the text
    inputs = tokenizer(main_text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Create embeddings
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state
    return embeddings


if __name__ == "__main__":
    dataset_path = "/scratch/gilbreth/jiang784/PTMTorrent/huggingface/PTM-Torrent/ptm_torrent/huggingface/data/huggingface/repos/"
    readme_path = dataset_path + "Intel/distilbert-base-uncased-distilled-squad-int8-static//README.md"
    main_text = load_readme(readme_path)
    logger.debug(main_text)
    embeddings = get_embeddings(main_text)
    logger.debug(embeddings.shape)

    

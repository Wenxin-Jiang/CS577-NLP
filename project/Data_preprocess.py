import os
from tqdm import tqdm
import openai

from loguru import logger

def read_readme_files(base_dir):
    readmes = {}
    for author_name in tqdm(os.listdir(base_dir)):
        for model_name in os.listdir(os.path.join(base_dir, author_name)):
            readme_path = os.path.join(base_dir, author_name, model_name, "README.md")
            # logger.debug(readme_path)
            if os.path.exists(readme_path):
                with open(readme_path, "r") as f:
                    readmes[model_name] = f.read()
        #     break
        # break
    return readmes


def extract_metadata_gpt35(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def truncate_text(text, max_tokens=2000):
    tokens = text.split()
    truncated_tokens = tokens[:max_tokens]
    truncated_text = ' '.join(truncated_tokens)
    return truncated_text

def extract_metadata_gpt(metadata, readme):
    truncated_documentation = truncate_text(readme)
    prompt = f"Extract metadata from the following model documentation: {readme}"
    metadata_text = extract_metadata_gpt35(prompt)
    logger.debug(metadata_text)
    metadata[model_name] = metadata_text

    with open("metadata.txt", "w") as file:
        for entry in metadata:
            for key, value in entry.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    return metadata

if __name__ == "__main__":
    base_dir = "/scratch/gilbreth/jiang784/PTMTorrent/huggingface/PTM-Torrent/ptm_torrent/huggingface/data/huggingface/repos"
    readmes = read_readme_files(base_dir)
    # logger.debug(readmes.keys())

    # extract metadata from readme using GPT APIs
    openai.api_key = "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"
    
    metadata = {}
    for model_name, readme in readmes.items():
        extract_metadata_gpt(metadata, readme)
        logger.info(f"Extracted metadata for {model_name}")
        # Assuming 'metadata' variable contains the extracted metadata
        break
    logger.debug(metadata)


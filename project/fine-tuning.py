import torch
import pandas as pd
from transformers import BertTokenizer, BertForTokenClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("my_dataset.csv")

# Split the dataset_names column into a list of strings
df["dataset_names"] = df["dataset_names"].str.split(",")

def chunk_text(text, max_length=512, overlap=50):
    """
    Chunk a long string of text into smaller pieces.

    Args:
        text (str): The text to chunk.
        max_length (int): The maximum length of each chunk.
        overlap (int): The number of characters to overlap between chunks.

    Returns:
        A list of strings containing the chunked text.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_length, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_length - overlap
    return chunks


max_length = 512  # Maximum length of each chunk
overlap = 50  # Number of characters to overlap between chunks

# Create a new column to hold the chunked text
df["readme_chunks"] = df["readme"].apply(lambda x: chunk_text(x, max_length, overlap))


from transformers import BertTokenizer
import torch
from torch.utils.data import Dataset, DataLoader

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

import torch
from torch.utils.data import Dataset

class DatasetNameDataset(Dataset):
    def __init__(self, data, tokenizer, max_length):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.texts = data['text']
        self.labels = data['label']

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        label = self.labels[index]

        # Encode text using the tokenizer
        inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        # Return the input IDs, attention mask, and label as PyTorch tensors
        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'label': torch.tensor(label, dtype=torch.long)
        }


def token_classification_dataset(encodings, labels):
    class TokenClassificationDataset(torch.utils.data.Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = self.labels[idx]

# Load the dataset (README + dataset names)
with open('dataset.txt', 'r') as f:
    dataset_text = f.read()

with open('readme.txt', 'r') as f:
    readme_text = f.read()

# Preprocess the data and chunk it
max_length = 512  # Maximum number of tokens per chunk
stride = 256  # Number of tokens to overlap between chunks
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
readme_tokens = tokenizer.tokenize(readme_text)
dataset_tokens = tokenizer.tokenize(dataset_text)

chunked_readme_tokens = []
chunked_dataset_tokens = []

start = 0
while start < len(readme_tokens):
    end = min(start + max_length, len(readme_tokens))
    chunked_readme_tokens.append(readme_tokens[start:end])
    start += max_length - stride

start = 0
while start < len(dataset_tokens):
    end = min(start + max_length, len(dataset_tokens))
    chunked_dataset_tokens.append(dataset_tokens[start:end])
    start += max_length - stride

# Create the labels
labels = []
for chunk in chunked_readme_tokens:
    label = [0] * len(chunk)
    for i, token in enumerate(chunk):
        if token in chunked_dataset_tokens:
            label[i] = 1
    labels.append(label)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(chunked_readme_tokens, labels, test_size=0.2, random_state=42)

# Convert the data to PyTorch tensors
train_encodings = tokenizer(X_train, is_split_into_words=True, padding=True, truncation=True)
val_encodings = tokenizer(X_val, is_split_into_words=True, padding=True, truncation=True)

train_labels = torch.tensor(y_train)
val_labels = torch.tensor(y_val)

# Fine-tune the pre-trained model
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=2)

training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    learning_rate=2e-5,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model='f1',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=token_classification_dataset(train_encodings, train_labels),
    eval_dataset=token_classification_dataset(val_encodings, val_labels),
    data_collator=lambda data: {'input_ids': torch.stack([f[0] for f in data]),
                                'attention_mask': torch.stack([f[1] for f in data]),
                                'labels': torch.stack([f[2] for f in data])},
    compute_metrics=compute_metrics,
)

trainer.train()

---
language: si
tags:
- SinBERTo
- Sinhala
- roberta
---

### Overview

SinBerto is a small language model trained on a small news corpus. SinBerto is trained on Sinhala Language which is a low resource language compared to other languages.

### Model Specifications.
model : [Roberta](https://arxiv.org/abs/1907.11692) 

vocab_size=52_000,
max_position_embeddings=514,
num_attention_heads=12,
num_hidden_layers=6,
type_vocab_size=1


### How to use from the Transformers Library

from transformers import AutoTokenizer, AutoModelForMaskedLM
  
tokenizer = AutoTokenizer.from_pretrained("Kalindu/SinBerto")

model = AutoModelForMaskedLM.from_pretrained("Kalindu/SinBerto")


### OR Clone the model repo

git lfs install

git clone https://huggingface.co/Kalindu/SinBerto
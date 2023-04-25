---
language: 
- ru
tags:
- text-classification
license: apache-2.0

---

# RuBERTConv Toxic Classifier

## Model description

Based on [rubert-base-cased-conversational](https://huggingface.co/DeepPavlov/rubert-base-cased-conversational) model

## Intended uses & limitations

#### How to use

Colab: [link](https://colab.research.google.com/drive/1veKO9hke7myxKigZtZho_F-UM2fD9kp8)

```python
from transformers import pipeline

model_name = "IlyaGusev/rubertconv_toxic_clf"
pipe = pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt") 

text = "Ты придурок из интернета"
pipe([text])
```

## Training data

Datasets:
- [2ch]( https://www.kaggle.com/blackmoon/russian-language-toxic-comments)
- [Odnoklassniki](https://www.kaggle.com/alexandersemiletov/toxic-russian-comments)
- [Toloka Persona Chat Rus](https://toloka.ai/ru/datasets)
- [Koziev's Conversations](https://github.com/Koziev/NLP_Datasets/blob/master/Conversations/Data) with [toxic words vocabulary](https://www.dropbox.com/s/ou6lx03b10yhrfl/bad_vocab.txt.tar.gz)

Augmentations:
- ё -> е
- Remove or add "?" or "!"
- Fix CAPS
- Concatenate toxic and non-toxic texts
- Concatenate two non-toxic texts
- Add toxic words from vocabulary
- Add typos
- Mask toxic words with "*", "@", "$"


## Training procedure

TBA
---
language: 
- ru
tags:
- token-classification
license: apache-2.0
widget:
 - text: Ёпта, меня зовут придурок и я живу в жопе

---

# RuBERTConv Toxic Editor

## Model description

Tagging model for detoxification based on [rubert-base-cased-conversational](https://huggingface.co/DeepPavlov/rubert-base-cased-conversational).

4 possible classes:
- Equal = save tokens
- Replace = replace tokens with mask
- Delete = remove tokens
- Insert = insert mask before tokens

Use in pair with [mask filler](https://huggingface.co/IlyaGusev/sber_rut5_filler).

## Intended uses & limitations

#### How to use

Colab: [link](https://colab.research.google.com/drive/1NUSO1QGlDgD-IWXa2SpeND089eVxrCJW)

```python
import torch
from transformers import AutoTokenizer, pipeline

tagger_model_name = "IlyaGusev/rubertconv_toxic_editor"

device = "cuda" if torch.cuda.is_available() else "cpu"
device_num = 0 if device == "cuda" else -1
tagger_pipe = pipeline(
    "token-classification",
    model=tagger_model_name,
    tokenizer=tagger_model_name,
    framework="pt",
    device=device_num,
    aggregation_strategy="max"
)

text = "..."
tagger_predictions = tagger_pipe([text], batch_size=1)
sample_predictions = tagger_predictions[0]
print(sample_predictions)
```

## Training data

- Dataset: [russe_detox_2022](https://github.com/skoltech-nlp/russe_detox_2022/tree/main/data)

## Training procedure

- Parallel corpus convertion: [compute_tags.py](https://github.com/IlyaGusev/rudetox/blob/main/rudetox/marker/compute_tags.py)
- Training script: [train.py](https://github.com/IlyaGusev/rudetox/blob/main/rudetox/marker/train.py)
- Pipeline step: [dvc.yaml, train_marker](https://github.com/IlyaGusev/rudetox/blob/main/dvc.yaml#L367)

## Eval results

TBA
---
tags:
- generated_from_trainer
model-index:
- name: CORD19_BERT
  results: []
---

# CORD19-BERT

## How to use

```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('CovRelex-SE/CORD19-BERT')
model = BertModel.from_pretrained("CovRelex-SE/CORD19-BERT")
text = "The virus can spread from an infected person’s mouth or nose."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

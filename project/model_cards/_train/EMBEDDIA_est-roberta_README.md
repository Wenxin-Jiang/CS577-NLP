---
language: 
- et

license: cc-by-sa-4.0
---
# Usage
Load in transformers library with:
```
from transformers import AutoTokenizer, AutoModelForMaskedLM
  
  tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/est-roberta")
  model = AutoModelForMaskedLM.from_pretrained("EMBEDDIA/est-roberta")
```

# Est-RoBERTa
Est-RoBERTa model is a monolingual Estonian BERT-like model. It is closely related to French Camembert model https://camembert-model.fr/. The Estonian corpora used for training the model have 2.51 billion tokens in total. The subword vocabulary contains 40,000 tokens.

Est-RoBERTa was trained for 40 epochs.


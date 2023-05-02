---
language: 
  - pt
---

This model was distilled from [BERTimbau](https://huggingface.co/neuralmind/bert-base-portuguese-cased)

## Usage

```python
from transformers import AutoTokenizer  # Or BertTokenizer
from transformers import AutoModelForPreTraining  # Or BertForPreTraining for loading pretraining heads
from transformers import AutoModel  # or BertModel, for BERT without pretraining heads
model = AutoModelForPreTraining.from_pretrained('adalbertojunior/distilbert-portuguese-cased')
tokenizer = AutoTokenizer.from_pretrained('adalbertojunior/distilbert-portuguese-cased', do_lower_case=False)
```
You should fine tune it on your own data.

It can achieve accuracy up to 99% relative to the original BERTimbau in some tasks.
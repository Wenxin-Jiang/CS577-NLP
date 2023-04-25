---
tags:
- summarization
language:
- it
metrics:
- rouge
model-index:
- name: summarization_ilpost
  results: []
datasets:
- ARTeLab/ilpost
---

# summarization_ilpost

This model is a fine-tuned version of [gsarti/it5-base](https://huggingface.co/gsarti/it5-base) on IlPost dataset for Abstractive Summarization.

It achieves the following results:
- Loss: 1.6020
- Rouge1: 33.7802
- Rouge2: 16.2953
- Rougel: 27.4797
- Rougelsum: 30.2273
- Gen Len: 45.3175

## Usage 

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("ARTeLab/it5-summarization-ilpost")
model = T5ForConditionalGeneration.from_pretrained("ARTeLab/it5-summarization-ilpost")
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Framework versions
- Transformers 4.12.0.dev0
- Pytorch 1.9.1+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
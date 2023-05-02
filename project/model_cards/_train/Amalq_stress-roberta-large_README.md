---
language: en
tags:
- Transformers
license: apache-2.0
datasets:
- Dreaddit
---

# StressRoberta model

is a model initialized with roberta-large (https://huggingface.co/roberta-large )and trained with 
[Dreaddit: A Reddit Dataset for Stress Analysis in Social Media] ( http://www.cs.columbia.edu/eturcan/data/dreaddit.zip ). 
We follow the standard pretraining protocols of RoBERTa with [Huggingface’s Transformers library](https://github.com/huggingface/transformers).    

## Usage Load the model via [Huggingface’s Transformers library](https://github.com/huggingface/transformers):   

```python
from transformers import AutoTokenizer,    
AutoModel tokenizer = AutoTokenizer.from_pretrained("amalq/stress-roberta-large")    
model = AutoModel.from_pretrained("amalq/stress-roberta-large")   
```

Perplexity of this model is: 3.28
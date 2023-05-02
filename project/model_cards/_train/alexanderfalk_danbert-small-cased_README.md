---
language:
- da
- en
thumbnail:
tags:
- named entity recognition
- token criticality
license: apache-2.0
datasets:
- custom danish dataset
inference: false
metrics:
- array of metric identifiers
---

# DanBERT

## Model description

DanBERT is a danish pre-trained model based on BERT-Base. The pre-trained model has been trained on more than 2 million sentences and 40 millions, danish words. The training has been conducted as part of a thesis.  
The model can be found at:

* [danbert-da](https://huggingface.co/alexanderfalk/danbert-small-cased)

## Intended uses & limitations

#### How to use

```python
from transformers import AutoTokenizer, AutoModel  
tokenizer = AutoTokenizer.from_pretrained("alexanderfalk/danbert-small-cased")  
model = AutoModel.from_pretrained("alexanderfalk/danbert-small-cased") 
```

### BibTeX entry and citation info

```bibtex
@inproceedings{...,
  year={2020},
  title={Anonymization of Danish, Real-Time Data, and Personalized Modelling},
  author={Alexander Falk},
}
```
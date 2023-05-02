---
language: fr
license: mit
datasets:
- oscar
---

## Model description

CamemBERT is a state-of-the-art language model for French based on the RoBERTa model. It is now available on Hugging Face in 6 different versions with varying number of parameters, amount of pretraining data and pretraining data source domains.

## Evaluation

The model developers evaluated CamemBERT using four different downstream tasks for French: part-of-speech (POS) tagging, dependency parsing, named entity recognition (NER) and natural language inference (NLI).

## Limitations and bias

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

This model was pretrinaed on a subcorpus of OSCAR multilingual corpus. Some of the limitations and risks associated with the OSCAR dataset, which are further detailed in the [OSCAR dataset card](https://huggingface.co/datasets/oscar), include the following: 

> The quality of some OSCAR sub-corpora might be lower than expected, specifically for the lowest-resource languages.

> Constructed from Common Crawl, Personal and sensitive information might be present.

## Training data

OSCAR or Open Super-large Crawled Aggregated coRpus is a multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the Ungoliant architecture.

## How to use

-**Filling masks using pipeline**

```python
>>> from transformers import pipeline
>>> camembert_fill_mask = pipeline("fill-mask", model="camembert-base")
>>> results = camembert_fill_mask("Le camembert est <mask> :)")

>>> result
[{'score': 0.49091097712516785,
  'token': 7200,
  'token_str': 'délicieux',
  'sequence': 'Le camembert est délicieux :)'},
 {'score': 0.1055697426199913,
  'token': 2183,
  'token_str': 'excellent',
  'sequence': 'Le camembert est excellent :)'},
 {'score': 0.03453319892287254,
  'token': 26202,
  'token_str': 'succulent',
  'sequence': 'Le camembert est succulent :)'},
 {'score': 0.03303128108382225,
  'token': 528,
  'token_str': 'meilleur',
  'sequence': 'Le camembert est meilleur :)'},
 {'score': 0.030076386407017708,
  'token': 1654,
  'token_str': 'parfait',
  'sequence': 'Le camembert est parfait :)'}]
```

-**Extract contextual embedding features from Camembert output**

```python
import torch

>>> tokenized_sentence = tokenizer.tokenize("J'aime le camembert !")
>>> encoded_sentence = tokenizer.encode(tokenized_sentence)
# Can be done in one step : tokenize.encode("J'aime le camembert !")

>>> tokenized_sentence 
['▁J', "'", 'aime', '▁le', '▁ca', 'member', 't', '▁!']
>>> encoded_sentence
[5, 121, 11, 660, 16, 730, 25543, 110, 83, 6] 
```

![128791.gif](https://s3.amazonaws.com/moonup/production/uploads/1666329291279-634fe2e8cfefce6e57795f69.gif)
[more about](https://youtu.be/dMTy6C4UiQ4)
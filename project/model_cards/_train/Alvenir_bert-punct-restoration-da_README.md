---
language: da
tags:
- bert
- punctuation restoration
license: apache-2.0
datasets:
- custom

---

# Bert Punctuation Restoration Danish
This model performs the punctuation restoration task in Danish. The method used is sequence classification similar to how NER models
are trained.

## Model description
TODO

### How to use
The model requires some additional inference code, hence we created an awesome little pip package for inference. 
The inference code is based on the `TokenClassificationPipeline` pipeline from huggingface. 

First, install the little package by running 

```
pip install punctfix
```
Then restoration is as simple as the following snippet:

```python
>>> from punctfix import PunctFixer
>>> fixer = PunctFixer(language="da")

>>> example_text = "mit navn det er rasmus og jeg kommer fra firmaet alvenir det er mig som har trænet denne lækre model"
>>> print(fixer.punctuate(example_text))
'Mit navn det er Rasmus og jeg kommer fra firmaet Alvenir. Det er mig som har trænet denne lækre model.'

>>> example_text = "en dag bliver vi sku glade for at vi nu kan sætte punktummer og kommaer i en sætning det fungerer da meget godt ikke"
>>> print(fixer.punctuate(example_text)) 
'En dag bliver vi sku glade for, at vi nu kan sætte punktummer og kommaer i en sætning. Det fungerer da meget godt, ikke?'
```

## Training data
To Do
 
## Training procedure
To Do

### Preprocessing

TODO

## Evaluation results
TODO

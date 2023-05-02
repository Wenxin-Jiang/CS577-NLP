---
language: es
tags:
- zero-shot-classification
- nli
- pytorch
datasets:
- xnli
license: mit
pipeline_tag: zero-shot-classification
widget:
- text: "El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo"
  candidate_labels: "cultura, sociedad, economia, salud, deportes"
---

# bert-base-spanish-wwm-cased-xnli

**UPDATE, 15.10.2021: Check out our new zero-shot classifiers, much more lightweight and even outperforming this one: [zero-shot SELECTRA small](https://huggingface.co/Recognai/zeroshot_selectra_small) and [zero-shot SELECTRA medium](https://huggingface.co/Recognai/zeroshot_selectra_medium).**

## Model description

This model is a fine-tuned version of the [spanish BERT model](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) with the Spanish portion of the XNLI dataset. You can have a look at the [training script](https://huggingface.co/Recognai/bert-base-spanish-wwm-cased-xnli/blob/main/zeroshot_training_script.py) for details of the training.

### How to use

You can use this model with Hugging Face's [zero-shot-classification pipeline](https://discuss.huggingface.co/t/new-pipeline-for-zero-shot-text-classification/681):
```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification", 
                       model="Recognai/bert-base-spanish-wwm-cased-xnli")

classifier(
    "El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo",
    candidate_labels=["cultura", "sociedad", "economia", "salud", "deportes"],
    hypothesis_template="Este ejemplo es {}."
)
"""output
{'sequence': 'El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo',
 'labels': ['cultura', 'sociedad', 'economia', 'salud', 'deportes'],
 'scores': [0.38897448778152466,
  0.22997373342514038,
  0.1658431738615036,
  0.1205764189362526,
  0.09463217109441757]}
"""
```
## Eval results


Accuracy for the test set:

|                             | XNLI-es |
|-----------------------------|---------|
|bert-base-spanish-wwm-cased-xnli | 79.9% |
---
tags:
- bert
- adapterhub:dp/ud_ewt
- adapter-transformers
datasets:
- universal_dependencies
language:
- en
---

# Adapter `AdapterHub/bert-base-uncased-pf-ud_en_ewt` for bert-base-uncased

An [adapter](https://adapterhub.ml) for the `bert-base-uncased` model that was trained on the [dp/ud_ewt](https://adapterhub.ml/explore/dp/ud_ewt/) dataset and includes a prediction head for dependency parsing.

This adapter was created for usage with the **[adapter-transformers](https://github.com/Adapter-Hub/adapter-transformers)** library.

## Usage

First, install `adapter-transformers`:

```
pip install -U adapter-transformers
```
_Note: adapter-transformers is a fork of transformers that acts as a drop-in replacement with adapter support. [More](https://docs.adapterhub.ml/installation.html)_

Now, the adapter can be loaded and activated like this:

```python
from transformers import AutoModelWithHeads

model = AutoModelWithHeads.from_pretrained("bert-base-uncased")
adapter_name = model.load_adapter("AdapterHub/bert-base-uncased-pf-ud_en_ewt", source="hf", set_active=True)
```

## Architecture & Training

This adapter was trained using adapter-transformer's example script for dependency parsing.
See https://github.com/Adapter-Hub/adapter-transformers/tree/master/examples/dependency-parsing.


## Evaluation results

Scores achieved by dependency parsing adapters on the test set of UD English EWT after training:

| Model | UAS | LAS |
| --- | --- | --- |
| `bert-base-uncased` | 91.74 | 89.15 |
| `roberta-base` | 91.43 | 88.43 |


## Citation

<!-- Add some description here -->
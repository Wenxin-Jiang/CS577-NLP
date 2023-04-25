---
tags:
- adapterhub:qa/bioasq
- adapter-transformers
- bart
---

# Adapter `AdapterHub/bioASQyesno` for facebook/bart-base

An [adapter](https://adapterhub.ml) for the `facebook/bart-base` model that was trained on the [qa/bioasq](https://adapterhub.ml/explore/qa/bioasq/) dataset.

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

model = AutoModelWithHeads.from_pretrained("facebook/bart-base")
adapter_name = model.load_adapter("AdapterHub/bioASQyesno", source="hf", set_active=True)
```

## Architecture & Training

Trained for 15 epochs with early stopping, a learning rate of 1e-4, and a batch size of 4 on the yes-no questions of the bioASQ 8b dataset.

## Evaluation results

Achieved 75% accuracy on the test dataset of bioASQ 8b dataset.

## Citation

<!-- Add some description here -->
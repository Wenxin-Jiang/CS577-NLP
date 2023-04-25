---
tags:
- adapterhub:qa/narrativeqa
- adapter-transformers
- bart
datasets:
- narrativeqa
---

# Adapter `hSterz/narrativeqa` for facebook/bart-base

An [adapter](https://adapterhub.ml) for the `facebook/bart-base` model that was trained on the [qa/narrativeqa](https://adapterhub.ml/explore/qa/narrativeqa/) dataset.

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
adapter_name = model.load_adapter("hSterz/narrativeqa", source="hf", set_active=True)
```

## Architecture & Training

<!-- Add some description here -->

## Evaluation results

<!-- Add some description here -->

## Citation

<!-- Add some description here -->
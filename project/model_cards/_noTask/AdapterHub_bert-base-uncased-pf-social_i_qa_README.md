---
tags:
- bert
- adapter-transformers
datasets:
- social_i_qa
language:
- en
---

# Adapter `AdapterHub/bert-base-uncased-pf-social_i_qa` for bert-base-uncased

An [adapter](https://adapterhub.ml) for the `bert-base-uncased` model that was trained on the [social_i_qa](https://huggingface.co/datasets/social_i_qa/) dataset and includes a prediction head for multiple choice.

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
adapter_name = model.load_adapter("AdapterHub/bert-base-uncased-pf-social_i_qa", source="hf")
model.active_adapters = adapter_name
```

## Architecture & Training

The training code for this adapter is available at https://github.com/adapter-hub/efficient-task-transfer.
In particular, training configurations for all tasks can be found [here](https://github.com/adapter-hub/efficient-task-transfer/tree/master/run_configs).


## Evaluation results

Refer to [the paper](https://arxiv.org/pdf/2104.08247) for more information on results.

## Citation

If you use this adapter, please cite our paper ["What to Pre-Train on? Efficient Intermediate Task Selection"](https://arxiv.org/pdf/2104.08247):

```bibtex
@inproceedings{poth-etal-2021-what-to-pre-train-on,
    title={What to Pre-Train on? Efficient Intermediate Task Selection},
    author={Clifton Poth and Jonas Pfeiffer and Andreas Rücklé and Iryna Gurevych},
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2104.08247",
    pages = "to appear",
}
```
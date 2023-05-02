---
language: en
---

# Sparse BERT base model (uncased)

Pretrained model pruned to 70% sparsity.
The model is a pruned version of the [BERT base model](https://huggingface.co/bert-base-uncased).

## Intended Use

The model can be used for fine-tuning to downstream tasks with sparsity already embeded to the model.
To keep the sparsity a mask should be added to each sparse weight blocking the optimizer from updating the zeros.
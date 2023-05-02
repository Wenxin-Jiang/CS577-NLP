---
license: mit
---

# Sparse BERT mini model (uncased)

Finetuned model pruned to 1:4 structured sparsity.
The model is a pruned version of the [BERT mini model](https://huggingface.co/prajjwal1/bert-mini).

## Intended Use

The model can be used for inference with sparsity optimization.
For further details on the model and its usage will be soon available.

## Evaluation Results
We get the following results on the sst2 tasks development set:

| Task | SST-2 (Acc) |
|------|-------------|
|      |     87.2    |
Better than dense [bert mini](https://huggingface.co/M-FAC/bert-mini-finetuned-sst2) which is 84.74%.

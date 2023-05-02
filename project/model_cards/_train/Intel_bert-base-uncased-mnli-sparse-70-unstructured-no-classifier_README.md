---
language: en
---

# Sparse BERT base model fine tuned to MNLI without classifier layer (uncased)

Fine tuned sparse BERT base to MNLI (GLUE Benchmark) task from [bert-base-uncased-sparse-70-unstructured](https://huggingface.co/Intel/bert-base-uncased-sparse-70-unstructured).
<br>
This model doesn't have a classifier layer to enable easier loading of the model for training to other downstream tasks.
In all the other layers this model is similar to [bert-base-uncased-mnli-sparse-70-unstructured](https://huggingface.co/Intel/bert-base-uncased-mnli-sparse-70-unstructured).
<br><br>
Note: This model requires `transformers==2.10.0`

## Evaluation Results
    Matched: 82.5%
    Mismatched: 83.3%

This model can be further fine-tuned to other tasks and achieve the following evaluation results:

| Task | QQP (Acc/F1) | QNLI (Acc) | SST-2 (Acc) | STS-B (Pears/Spear) | SQuADv1.1 (Acc/F1) |
|------|--------------|------------|-------------|---------------------|--------------------|
|      |   90.2/86.7  |    90.3    |     91.5    |      88.9/88.6      |      80.5/88.2     |

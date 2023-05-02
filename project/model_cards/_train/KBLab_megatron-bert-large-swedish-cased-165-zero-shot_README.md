---
pipeline_tag: zero-shot-classification
tags:
  - zero-shot-classification
  - swedish
  - megatron-bert
language:
  - sv
datasets:
  - KBLab/overlim
widget:
  - example_title: Zero-shot
    text: Många skjuter upp sina tandläkarbesök
    candidate_labels: hälsa, politik, sport, religion
inference:
  parameters:
    hypothesis_template: Detta exempel handlar om {}.
---


# Megatron-BERT-large Swedish 165k for zero-shot classification


This model is based on Megatron-BERT-large-165k (https://huggingface.co/KBLab/megatron-bert-large-swedish-cased-165k). It was fine-tuned on the QNLI task and further fine-tuned on the MNLI task.
The model can be used with the Hugging Face zero-shot classification pipeline.



## Usage

```python
>>> from transformers import pipeline
>>> classifier = pipeline(
...     "zero-shot-classification",
...     model="KBlab/megatron-bert-large-swedish-cased-165-zero-shot"
... )
>>> classifier(
...     "Ruben Östlunds ”Triangle of sadness” nomineras till en Golden Globe i kategorin bästa musikal eller komedi.",
...     candidate_labels=["hälsa", "politik", "sport", "religion", "nöje"],
...     hypothesis_template="Detta exempel handlar om {}.",
... )
{'sequence': 'Ruben Östlunds ”Triangle of sadness” nomineras till en Golden Globe i kategorin bästa musikal eller komedi.',
 'labels': ['nöje', 'sport', 'religion', 'hälsa', 'politik'],
 'scores': [0.9274595379829407,
  0.025105971843004227,
  0.018440095707774162,
  0.017049923539161682,
  0.011944468133151531]}
```

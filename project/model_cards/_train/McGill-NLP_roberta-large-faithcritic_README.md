---
license: mit
datasets:
- McGill-NLP/FaithDial
widget:
- text: "A cardigan is a type of knitted garment (sweater) that has an open front. </s></s> The old version is the regular one, knitted garment that has open front and buttons!"
model-index:
- name: roberta-large-faithcritic
  results:
  - task:
      type: text-classification
      name: Faithfulness Critic
    dataset:
      name: 'FaithCritic'
      type: McGill-NLP/FaithDial
    metrics:
    - name: Accuracy
      type: accuracy
      value: 86.51
  - task:
      type: text-classification
      name: Faithfulness Critic
    dataset:
      name: 'MNLI'
      type: multi_nli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 74.720
  - task:
      type: text-classification
      name: Faithfulness Critic
    dataset:
      name: 'BEGIN'
      type: begin
    metrics:
    - name: Accuracy
      type: accuracy
      value: 71.56
---

## Overview

**Model Description:** roberta-large-faithcritic is the [RoBERTa large model](https://huggingface.co/roberta-large) fine-tuned on FaithCritic, a derivative of the [FaithDial](https://huggingface.co/datasets/McGill-NLP/FaithDial) dataset. The objective is to predict whether an utterance is faithful or not, given the source knowledge.

The hyperparameters are provided in [hparams.yml](https://huggingface.co/McGill-NLP/roberta-large-faithcritic/blob/main/hparams.yaml). To know more about how to train a critic model, visit [our repo](https://github.com/McGill-NLP/FaithDial).

## Usage

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("McGill-NLP/roberta-large-faithcritic")
model = AutoModel.from_pretrained("McGill-NLP/roberta-large-faithcritic")

knowledge = "A cardigan is a type of knitted garment (sweater) that has an open front."
response = "The old version is the regular one, knitted garment that has open front and buttons!"
input = tokenizer(knowledge, response)
output = model(**input)

```


## Citation Information

```bibtex
@article{dziri2022faithdial,
  title={FaithDial: A Faithful Benchmark for Information-Seeking Dialogue},
  author={Dziri, Nouha and Kamalloo, Ehsan and Milton, Sivan and Zaiane, Osmar and Yu, Mo and Ponti, Edoardo and Reddy, Siva},
  journal={arXiv preprint, arXiv:2204.10757},
  year={2022},
  url={https://arxiv.org/abs/2204.10757}
}
```

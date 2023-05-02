---
license: apache-2.0
tags:
- generated_from_trainer
language: en
widget:
- text: "My name is Scott and I live in Columbus."
- text: "My name is Scott and I am calling from Buffalo, NY. I would like to file a complain with United Airlines."
- text: "Apple was founded in 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne."
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-large-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9504719600222099
    - name: Recall
      type: recall
      value: 0.9574896520863632
    - name: F1
      type: f1
      value: 0.9539679001337494
    - name: Accuracy
      type: accuracy
      value: 0.9885618059637473
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-finetuned-ner

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0778
- Precision: 0.9505
- Recall: 0.9575
- F1: 0.9540
- Accuracy: 0.9886

## Model description

More information needed

#### Limitations and bias

This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. Furthermore, the model occassionally tags subword tokens as entities and post-processing of results may be necessary to handle those cases. 


#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("Jorgeutd/bert-large-uncased-finetuned-ner")
model = AutoModelForTokenClassification.from_pretrained("Jorgeutd/bert-large-uncased-finetuned-ner")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Scott and I live in Ohio"
ner_results = nlp(example)
print(ner_results)
```


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1997        | 1.0   | 878  | 0.0576          | 0.9316    | 0.9257 | 0.9286 | 0.9837   |
| 0.04          | 2.0   | 1756 | 0.0490          | 0.9400    | 0.9513 | 0.9456 | 0.9870   |
| 0.0199        | 3.0   | 2634 | 0.0557          | 0.9436    | 0.9540 | 0.9488 | 0.9879   |
| 0.0112        | 4.0   | 3512 | 0.0602          | 0.9443    | 0.9569 | 0.9506 | 0.9881   |
| 0.0068        | 5.0   | 4390 | 0.0631          | 0.9451    | 0.9589 | 0.9520 | 0.9882   |
| 0.0044        | 6.0   | 5268 | 0.0638          | 0.9510    | 0.9567 | 0.9538 | 0.9885   |
| 0.003         | 7.0   | 6146 | 0.0722          | 0.9495    | 0.9560 | 0.9527 | 0.9885   |
| 0.0016        | 8.0   | 7024 | 0.0762          | 0.9491    | 0.9595 | 0.9543 | 0.9887   |
| 0.0018        | 9.0   | 7902 | 0.0769          | 0.9496    | 0.9542 | 0.9519 | 0.9883   |
| 0.0009        | 10.0  | 8780 | 0.0778          | 0.9505    | 0.9575 | 0.9540 | 0.9886   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.8.1+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

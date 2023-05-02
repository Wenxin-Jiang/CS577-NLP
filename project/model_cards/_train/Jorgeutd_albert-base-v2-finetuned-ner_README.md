---
license: apache-2.0
tags:
- generated_from_trainer
language: en
widget:
- text: "My name is Scott and I live in Columbus."
- text: "Apple was founded in 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne."
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: albert-base-v2-finetuned-ner
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
      value: 0.9252213840603477
    - name: Recall
      type: recall
      value: 0.9329732113328189
    - name: F1
      type: f1
      value: 0.9290811285541773
    - name: Accuracy
      type: accuracy
      value: 0.9848205157332728
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-ner

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0626
- Precision: 0.9252
- Recall: 0.9330
- F1: 0.9291
- Accuracy: 0.9848

## Model description

More information needed

## limitations

#### Limitations and bias

This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. Furthermore, the model occassionally tags subword tokens as entities and post-processing of results may be necessary to handle those cases. 


#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("Jorgeutd/albert-base-v2-finetuned-ner")

model = AutoModelForTokenClassification.from_pretrained("Jorgeutd/albert-base-v2-finetuned-ner")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Scott and I live in Ohio"
ner_results = nlp(example)
print(ner_results)
```

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 220  | 0.0863          | 0.8827    | 0.8969 | 0.8898 | 0.9773   |
| No log        | 2.0   | 440  | 0.0652          | 0.8951    | 0.9199 | 0.9073 | 0.9809   |
| 0.1243        | 3.0   | 660  | 0.0626          | 0.9191    | 0.9208 | 0.9200 | 0.9827   |
| 0.1243        | 4.0   | 880  | 0.0585          | 0.9227    | 0.9281 | 0.9254 | 0.9843   |
| 0.0299        | 5.0   | 1100 | 0.0626          | 0.9252    | 0.9330 | 0.9291 | 0.9848   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.8.1+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

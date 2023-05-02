---
license: apache-2.0
tags:
- generated_from_trainer
language: en
widget:
- text: "The agent on the phone was very helpful and nice to me."
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-surveyclassification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-surveyclassification

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on a custom survey dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2818
- Accuracy: 0.9097
- F1: 0.9097

## Model description

More information needed

#### Limitations and bias

This model is limited by its training dataset of survey results for a particular customer service domain. This may not generalize well for all use cases in different domains.

#### How to use

You can use this model with Transformers *pipeline* for Text Classification.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
tokenizer = AutoTokenizer.from_pretrained("Jorgeutd/bert-base-uncased-finetuned-surveyclassification")
model = AutoModelForSequenceClassification.from_pretrained("Jorgeutd/bert-base-uncased-finetuned-surveyclassification")
text_classifier = pipeline("text-classification", model=model,tokenizer=tokenizer, device=0)
example = "The agent on the phone was very helpful and nice to me."
results = text_classifier(example)
print(results)
```

## Training and evaluation data

Custom survey dataset.

## Training procedure
SageMaker notebook instance.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.4136        | 1.0   | 902  | 0.2818          | 0.9097   | 0.9097 |
| 0.2213        | 2.0   | 1804 | 0.2990          | 0.9077   | 0.9077 |
| 0.1548        | 3.0   | 2706 | 0.3507          | 0.9026   | 0.9026 |
| 0.1034        | 4.0   | 3608 | 0.4692          | 0.9011   | 0.9011 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.8.1+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

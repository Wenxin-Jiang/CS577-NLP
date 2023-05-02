---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: farsi_lastname_classifier_bert
  results: []
---


# farsi_lastname_classifier_bert

This model is trained to classify Iranian last names. 
To use it, type a last name in the space provided on the right and then click on "compute". 
The model computes probability of the last name being Persian.
The compute takes a few seconds to load for the first try (because it needs to load the model first). Subsequent attempt should take only milliseconds.
In practice the model can compute the results for an entire batch of data (last names) in a fraction of a second. 

It achieves the following results on the evaluation set:
- Loss: 0.0863
- Accuracy: 0.976

## Model description

Model is based on Bert ("bert-base-cased")

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 128
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 12   | 0.6325          | 0.588    |
| No log        | 2.0   | 24   | 0.3414          | 0.952    |
| No log        | 3.0   | 36   | 0.2496          | 0.97     |
| No log        | 4.0   | 48   | 0.1674          | 0.976    |
| No log        | 5.0   | 60   | 0.1160          | 0.976    |
| No log        | 6.0   | 72   | 0.0917          | 0.972    |
| No log        | 7.0   | 84   | 0.0896          | 0.974    |
| No log        | 8.0   | 96   | 0.0874          | 0.974    |
| No log        | 9.0   | 108  | 0.0869          | 0.974    |
| No log        | 10.0  | 120  | 0.0863          | 0.976    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2

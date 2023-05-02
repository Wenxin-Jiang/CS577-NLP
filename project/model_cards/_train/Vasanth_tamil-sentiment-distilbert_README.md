---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tamilmixsentiment
metrics:
- accuracy
model_index:
- name: tamil-sentiment-distilbert
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tamilmixsentiment
      type: tamilmixsentiment
      args: default
    metric:
      name: Accuracy
      type: accuracy
      value: 0.665
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tamil-sentiment-distilbert

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the tamilmixsentiment dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0230
- Accuracy: 0.665

## Dataset Information
- text: Tamil-English code-mixed comment.
- label: list of the possible sentiments 
  - LABEL_0: "Positive", 
  - LABEL_1: "Negative", 
  - LABEL_2: "Mixed_feelings", 
  - LABEL_3: "unknown_state", 
  - LABEL_4: "not-Tamil"

## Intended uses & limitations

This model was just created for doing classification task on tamilmixsentiment dataset

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.0442        | 1.0   | 250  | 0.9883          | 0.674    |
| 0.9227        | 2.0   | 500  | 0.9782          | 0.673    |
| 0.7591        | 3.0   | 750  | 1.0230          | 0.665    |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3

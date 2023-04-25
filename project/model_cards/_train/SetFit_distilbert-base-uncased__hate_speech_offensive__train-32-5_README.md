---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1327
- Accuracy: 0.57

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.0972        | 1.0   | 19   | 1.0470          | 0.45     |
| 0.9738        | 2.0   | 38   | 0.9244          | 0.65     |
| 0.7722        | 3.0   | 57   | 0.8612          | 0.65     |
| 0.4929        | 4.0   | 76   | 0.6759          | 0.75     |
| 0.2435        | 5.0   | 95   | 0.7273          | 0.7      |
| 0.0929        | 6.0   | 114  | 0.6444          | 0.85     |
| 0.0357        | 7.0   | 133  | 0.7671          | 0.8      |
| 0.0173        | 8.0   | 152  | 0.7599          | 0.75     |
| 0.0121        | 9.0   | 171  | 0.8140          | 0.8      |
| 0.0081        | 10.0  | 190  | 0.7861          | 0.8      |
| 0.0066        | 11.0  | 209  | 0.8318          | 0.8      |
| 0.0057        | 12.0  | 228  | 0.8777          | 0.8      |
| 0.0053        | 13.0  | 247  | 0.8501          | 0.8      |
| 0.004         | 14.0  | 266  | 0.8603          | 0.8      |
| 0.004         | 15.0  | 285  | 0.8787          | 0.8      |
| 0.0034        | 16.0  | 304  | 0.8969          | 0.8      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

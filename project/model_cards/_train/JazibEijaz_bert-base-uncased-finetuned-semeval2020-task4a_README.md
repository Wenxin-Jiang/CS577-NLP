---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
  name: bert-base-uncased-finetuned-semeval2020-task4a-e2-b32-l5e5
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-semeval2020-task4a

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the ComVE dataset which was part of SemEval 2020 Task 4.
It achieves the following results on the test set:
- Loss: 0.2782
- Accuracy: 0.9040

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 344  | 0.2700          | 0.8940   |
| 0.349         | 2.0   | 688  | 0.2782          | 0.9040   |

### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.12.1
- Tokenizers 0.10.3

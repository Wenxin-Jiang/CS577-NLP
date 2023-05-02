---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
  name: bert-base-uncased-finetuned-semeval2020-task4b-append
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-semeval2020-task4b

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the ComVE dataset which was part of SemEval 2020 Task 4.
It achieves the following results on the test set:
- Loss: 0.6760
- Accuracy: 0.8760

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.5016        | 1.0   | 688  | 0.3502          | 0.8600   |
| 0.2528        | 2.0   | 1376 | 0.5769          | 0.8620   |
| 0.0598        | 3.0   | 2064 | 0.6720          | 0.8700   |
| 0.0197        | 4.0   | 2752 | 0.6760          | 0.8760   |

### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.12.1
- Tokenizers 0.10.3

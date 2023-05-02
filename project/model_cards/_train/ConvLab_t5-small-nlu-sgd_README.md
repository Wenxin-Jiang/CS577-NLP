---
language:
- en
license: apache-2.0
tags:
- t5-small
- text2text-generation
- natural language understanding
- conversational system
- task-oriented dialog
datasets:
- ConvLab/sgd
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-sgd
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/sgd
      name: SGD
      split: test
      revision: 6e8c79b888b21cc658cf9c0ce128d263241cf70f
    metrics:
      - type: Dialog acts Accuracy
        value: 45.0
        name: Accuracy
      - type: Dialog acts F1
        value: 58.6
        name: F1

widget:
- text: "user: Could you get me a reservation at P.f. Chang's in Corte Madera at afternoon 12?"
- text: "user: Sure, may I know if they have vegetarian options and how expensive is their food?"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-sgd

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Schema-Guided Dialog](https://huggingface.co/datasets/ConvLab/sgd).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 128
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 256
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

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
- ConvLab/tm1
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-tm1-context3
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/tm1
      name: Taskmaster-1
      split: test
      revision: 187bd9f5e786d80f64b3d372386e330ae36d8488
    metrics:
      - type: Dialog acts Accuracy
        value: 76.2
        name: Accuracy
      - type: Dialog acts F1
        value: 56.2
        name: F1

widget:
- text: "user: Hi there, could you please help me with an order of Pizza?\nsystem: Sure, where would you like to order you pizza from?\nuser: I would like to order a pizza from Domino's."
- text: "system: What kind of pizza are do you want to order?\nuser: I want to order a large pizza with chicken and pepperoni please.\nsystem: From which Domino's location would you like to order?\nuser: I would like to order from the Domino's closest to my house."

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-tm1-context3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-1](https://huggingface.co/datasets/ConvLab/tm1) with context window size == 3.

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

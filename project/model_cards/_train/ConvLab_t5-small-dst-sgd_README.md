---
language:
- en
license: apache-2.0
tags:
- t5-small
- text2text-generation
- dialog state tracking
- conversational system
- task-oriented dialog
datasets:
- ConvLab/sgd
metrics:
- Joint Goal Accuracy
- Slot F1

model-index:
- name: t5-small-dst-sgd
  results:
  - task:
      type: text2text-generation
      name: dialog state tracking
    dataset:
      type: ConvLab/sgd
      name: SGD
      split: test
      revision: 6e8c79b888b21cc658cf9c0ce128d263241cf70f
    metrics:
      - type: Joint Goal Accuracy
        value: 20.1
        name: JGA
      - type: Slot F1
        value: 58.5
        name: Slot F1

widget:
- text: "user: Hi, could you get me a restaurant booking on the 8th please?\nsystem: Any preference on the restaurant, location and time?\nuser: Could you get me a reservation at P.f. Chang's in Corte Madera at afternoon 12?"
- text: "user: I need to book a dinner reservation for a date. Help me reserve a table at a restaurant.\nsystem: What time and location do you have in mind?\nuser: Something around 8 in the night should be fine. Oh, and look in the San Jose area."

inference:
  parameters:
    max_length: 100

---

# t5-small-dst-sgd

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Schema-Guided Dialog](https://huggingface.co/datasets/ConvLab/sgd).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 128
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

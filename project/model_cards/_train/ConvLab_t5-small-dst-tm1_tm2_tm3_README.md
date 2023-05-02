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
- ConvLab/tm1
- ConvLab/tm2
- ConvLab/tm3
metrics:
- Joint Goal Accuracy
- Slot F1

model-index:
- name: t5-small-dst-tm1_tm2_tm3
  results:
  - task:
      type: text2text-generation
      name: dialog state tracking
    dataset:
      type: ConvLab/tm1, ConvLab/tm2, ConvLab/tm3
      name: TM1+TM2+TM3
      split: test
    metrics:
      - type: Joint Goal Accuracy
        value: 48.5
        name: JGA
      - type: Slot F1
        value: 81.1
        name: Slot F1

widget:
- text: "tm1: user: Hi there, could you please help me with an order of Pizza?\nsystem: Sure, where would you like to order you pizza from?\nuser: I would like to order a pizza from Domino's."
- text: "tm2: user: I need help finding a hotel in New Orleans.\nsystem: Okay.\nuser: I need something that's around $300 a night and it's a five star rating."
- text: "tm3: user: Hi, I'm hoping to see a movie tonight.\nsystem: Great, I can assist with that. What genre of film do you prefer.\nuser: I usually like comedies."

inference:
  parameters:
    max_length: 100

---

# t5-small-dst-tm1_tm2_tm3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-1](https://huggingface.co/datasets/ConvLab/tm1), [Taskmaster-2](https://huggingface.co/datasets/ConvLab/tm2), and [Taskmaster-3](https://huggingface.co/datasets/ConvLab/tm3).

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

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
- ConvLab/tm2
- ConvLab/tm3
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-tm1_tm2_tm3
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/tm1, ConvLab/tm2, ConvLab/tm3
      name: TM1+TM2+TM3
      split: test
    metrics:
      - type: Dialog acts Accuracy
        value: 81.8
        name: Accuracy
      - type: Dialog acts F1
        value: 73.0
        name: F1

widget:
- text: "tm1: user: I would like to order a pizza from Domino's."
- text: "tm2: user: I would like help getting a flight from LA to Amsterdam."
- text: "tm3: user: Well, I need a kids friendly movie. I was thinking about seeing Mulan."

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-tm1_tm2_tm3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-1](https://huggingface.co/datasets/ConvLab/tm1), [Taskmaster-2](https://huggingface.co/datasets/ConvLab/tm2), and [Taskmaster-3](https://huggingface.co/datasets/ConvLab/tm3).

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

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
- ConvLab/tm3
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-tm3-context3
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/tm3
      name: Taskmaster-3
      split: test
      revision: 910584e5451e2e439bb2a07b8544ecb42ff8835b
    metrics:
      - type: Dialog acts Accuracy
        value: 89.0
        name: Accuracy
      - type: Dialog acts F1
        value: 85.1
        name: F1

widget:
- text: "system: OK. And where will you be seeing the movie?\nuser: In Creek's End, Oregon\nsystem: Creek’s End, Oregon. Got it. Is there a particular movie you have in mind?\nuser: Mulan, please. We are taking the kids"
- text: "system: No problem. It looks like tonight’s remaining showtimes for Mulan at AMC Mercado 24 are 5:00pm, 7:10pm, and 9:45pm. Which is best for you?\nuser: I would like the earliest time, 5:00pm\nsystem: Great. And how many tickets?\nuser: three please"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-tm3-context3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-3](https://huggingface.co/datasets/ConvLab/tm3) with context window size == 3.

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

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
- ConvLab/tm2
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-tm2-context3
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/tm2
      name: Taskmaster-2
      split: test
      revision: cdc314b156e7f7ffa81a1e7398f1f8a2e86c0095
    metrics:
      - type: Dialog acts Accuracy
        value: 82.4
        name: Accuracy
      - type: Dialog acts F1
        value: 74.3
        name: F1

widget:
- text: "user: Hi, I'm looking for a flight. I need to visit a friend.\nsystem: Hello, how can I help you? Sure, I can help you with that. On what dates?\nuser: I'm looking to travel from March 20th to 22nd."
- text: "system: Anything else?\nuser: That should be everything.\nsystem: I found a flight for $424 on United Airlines.\nuser: Okay, is that for New York?"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-tm2-context3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-2](https://huggingface.co/datasets/ConvLab/tm2) with context window size == 3.

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

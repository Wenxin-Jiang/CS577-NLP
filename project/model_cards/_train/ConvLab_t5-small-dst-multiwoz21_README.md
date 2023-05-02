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
- ConvLab/multiwoz21
metrics:
- Joint Goal Accuracy
- Slot F1

model-index:
- name: t5-small-dst-multiwoz21
  results:
  - task:
      type: text2text-generation
      name: dialog state tracking
    dataset:
      type: ConvLab/multiwoz21
      name: MultiWOZ 2.1
      split: test
      revision: 5f55375edbfe0270c20bcf770751ad982c0e6614
    metrics:
      - type: Joint Goal Accuracy
        value: 52.6
        name: JGA
      - type: Slot F1
        value: 91.9
        name: Slot F1

widget:
- text: "user: I would like a taxi from Saint John's college to Pizza Hut Fen Ditton.\nsystem: What time do you want to leave and what time do you want to arrive by?\nuser: I want to leave after 17:15."
- text: "user: I want to find a moderately priced restaurant. \nsystem: I have many options available for you! Is there a certain area or cuisine that interests you?\nuser: Yes I would like the restaurant to be located in the center of the town."

inference:
  parameters:
    max_length: 100

---

# t5-small-dst-multiwoz21

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21).

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

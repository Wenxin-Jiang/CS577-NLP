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
- ConvLab/multiwoz21
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: t5-small-nlu-all-multiwoz21-context3
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/multiwoz21
      name: MultiWOZ 2.1
      split: test
      revision: 5f55375edbfe0270c20bcf770751ad982c0e6614
    metrics:
      - type: Dialog acts Accuracy
        value: 73.6
        name: Accuracy
      - type: Dialog acts F1
        value: 86.9
        name: F1

widget:
- text: "user: I would like a taxi from Saint John's college to Pizza Hut Fen Ditton.\nsystem: What time do you want to leave and what time do you want to arrive by?\nuser: I want to leave after 17:15."
- text: "user: I want to find a moderately priced restaurant. \nsystem: I have many options available for you! Is there a certain area or cuisine that interests you?\nuser: Yes I would like the restaurant to be located in the center of the attractions. \nsystem: There are 21 restaurants available in the centre of town. How about a specific type of cuisine?"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-all-multiwoz21-context3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21) both user and system utterances with context window size == 3.

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

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1

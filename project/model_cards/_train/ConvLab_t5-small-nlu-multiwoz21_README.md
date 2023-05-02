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
- name: t5-small-nlu-multiwoz21
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
        value: 77.8
        name: Accuracy
      - type: Dialog acts F1
        value: 86.5
        name: F1

widget:
- text: "user: I would like a taxi from Saint John's college to Pizza Hut Fen Ditton."
- text: "user: we are staying 6 people for 4 nights starting from Tuesday. i need the reference number"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlu-multiwoz21

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21).

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

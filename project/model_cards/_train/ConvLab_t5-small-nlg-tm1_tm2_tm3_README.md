---
language:
- en
license: apache-2.0
tags:
- t5-small
- text2text-generation
- natural language generation
- conversational system
- task-oriented dialog
datasets:
- ConvLab/tm1
- ConvLab/tm2
- ConvLab/tm3
metrics:
- Slot Error Rate
- sacrebleu

model-index:
- name: t5-small-nlg-tm1_tm2_tm3
  results:
  - task:
      type: text2text-generation
      name: natural language generation
    dataset:
      type: ConvLab/tm1, ConvLab/tm2, ConvLab/tm3
      name: TM1+TM2+TM3
      split: test
    metrics:
      - type: Slot Error Rate
        value: 2.1
        name: SER
      - type: sacrebleu
        value: 51.5
        name: BLEU

widget:
- text: "tm1: [inform][pizza_ordering]([name.store][Domino's])\n\nsystem: "
- text: "tm2: [inform][restaurant-search]([name.restaurant][Via 313, the Violet Crown Social Club],[price_range][$8 per slice])\n\nsystem: "
- text: "tm3: [inform][movie]([name.movie][Star Wars],[name.movie][The Grudge])\n\nsystem: "

inference:
  parameters:
    max_length: 100

---

# t5-small-nlg-tm1_tm2_tm3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Taskmaster-1](https://huggingface.co/datasets/ConvLab/tm1), [Taskmaster-2](https://huggingface.co/datasets/ConvLab/tm2), and [Taskmaster-3](https://huggingface.co/datasets/ConvLab/tm3).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 512
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

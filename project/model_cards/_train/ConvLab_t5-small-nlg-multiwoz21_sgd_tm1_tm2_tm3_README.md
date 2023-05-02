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
- ConvLab/sgd
- ConvLab/tm1
- ConvLab/tm2
- ConvLab/tm3
- ConvLab/multiwoz21
metrics:
- Slot Error Rate
- sacrebleu

model-index:
- name: t5-small-nlg-multiwoz21_sgd_tm1_tm2_tm3
  results:
  - task:
      type: text2text-generation
      name: natural language generation
    dataset:
      type: ConvLab/multiwoz21
      name: MultiWOZ 2.1
      split: test
      revision: 5f55375edbfe0270c20bcf770751ad982c0e6614
    metrics:
      - type: Slot Error Rate
        value: 3.2
        name: SER
      - type: sacrebleu
        value: 35.6
        name: BLEU
  - task:
      type: text2text-generation
      name: natural language generation
    dataset:
      type: ConvLab/sgd
      name: SGD
      split: test
      revision: 6e8c79b888b21cc658cf9c0ce128d263241cf70f
    metrics:
      - type: Slot Error Rate
        value: 8.3
        name: SER
      - type: sacrebleu
        value: 29.9
        name: BLEU
  - task:
      type: text2text-generation
      name: natural language generation
    dataset:
      type: ConvLab/tm1, ConvLab/tm2, ConvLab/tm3
      name: TM1+TM2+TM3
      split: test
    metrics:
      - type: Slot Error Rate
        value: 2.0
        name: SER
      - type: sacrebleu
        value: 51.3
        name: BLEU

widget:
- text: "[inform][restaurant]([area][centre],[food][Indian],[choice][nine]);[request][restaurant]([price range][])\n\nsystem: "
  example_title: "MultiWOZ 2.1"
- text: "sgd: [confirm][Restaurants_2]([number_of_seats][2],[restaurant_name][P.f. Chang's],[location][Corte Madera],[time][12 pm],[date][March 8th])\n\nsystem: "
  example_title: "Schema-Guided Dialog"
- text: "tm1: [inform][pizza_ordering]([name.store][Domino's])\n\nsystem: "
  example_title: "Taskmaster-1"
- text: "tm2: [inform][restaurant-search]([name.restaurant][Via 313, the Violet Crown Social Club],[price_range][$8 per slice])\n\nsystem: "
  example_title: "Taskmaster-2"
- text: "tm3: [inform][movie]([name.movie][Star Wars],[name.movie][The Grudge])\n\nsystem: "
  example_title: "Taskmaster-3"

inference:
  parameters:
    max_length: 100

---

# t5-small-nlg-multiwoz21_sgd_tm1_tm2_tm3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21), [Schema-Guided Dialog](https://huggingface.co/datasets/ConvLab/sgd), [Taskmaster-1](https://huggingface.co/datasets/ConvLab/tm1), [Taskmaster-2](https://huggingface.co/datasets/ConvLab/tm2), and [Taskmaster-3](https://huggingface.co/datasets/ConvLab/tm3).

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

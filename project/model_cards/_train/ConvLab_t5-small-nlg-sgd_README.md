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
metrics:
- Slot Error Rate
- sacrebleu

model-index:
- name: t5-small-nlg-sgd
  results:
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
        value: 11.9
        name: SER
      - type: sacrebleu
        value: 29.6
        name: BLEU

widget:
- text: "[request][Restaurants_2]([time][],[restaurant_name][],[location][])\n\nsystem: "
- text: "[confirm][Restaurants_2]([number_of_seats][2],[restaurant_name][P.f. Chang's],[location][Corte Madera],[time][12 pm],[date][March 8th])\n\nsystem: "

inference:
  parameters:
    max_length: 100

---

# t5-small-nlg-sgd

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [Schema-Guided Dialog](https://huggingface.co/datasets/ConvLab/sgd).

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

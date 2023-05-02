---
language:
- en
license: apache-2.0
tags:
- t5-small
- text2text-generation
- dialogue generation
- conversational system
- task-oriented dialog
datasets:
- ConvLab/multiwoz21
metrics:
- LM loss

model-index:
- name: t5-small-goal2dialogue-multiwoz21
  results:
  - task:
      type: text2text-generation
      name: dialogue generation
    dataset:
      type: ConvLab/multiwoz21
      name: MultiWOZ 2.1
      split: validation
      revision: 5f55375edbfe0270c20bcf770751ad982c0e6614
    metrics:
      - type: Language model loss
        value: 1.5253684520721436
        name: LM loss
  - task:
      type: text2text-generation
      name: dialogue generation
    dataset:
      type: ConvLab/multiwoz21
      name: MultiWOZ 2.1
      split: test
      revision: 5f55375edbfe0270c20bcf770751ad982c0e6614
    metrics:
      - type: Language model loss
        value: 1.515929937362671
        name: LM loss


widget:
- text: "You are traveling to Cambridge and looking forward to try local restaurants. You are looking for a particular attraction. Its name is called nusha. Make sure you get postcode and address. You are also looking for a place to dine. The restaurant should be in the expensive price range and should serve indian food. The restaurant should be in the centre. Make sure you get address"
- text: "You want to book a taxi. The taxi should go to pizza hut fen ditton and should depart from saint john's college. The taxi should leave after 17:15. Make sure you get car type and contact number"

inference:
  parameters:
    max_length: 1024

---

# t5-small-goal2dialogue-multiwoz21

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

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
- ConvLab/multiwoz21
metrics:
- Slot Error Rate
- sacrebleu

model-index:
- name: t5-small-nlg-multiwoz21
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
        value: 3.7
        name: SER
      - type: sacrebleu
        value: 35.8
        name: BLEU

widget:
- text: "[request][taxi]([leave at][],[arrive by][])\n\nsystem: "
- text: "[inform][restaurant]([area][centre],[food][Indian],[choice][nine]);[request][restaurant]([price range][])\n\nsystem: "

inference:
  parameters:
    max_length: 100

---

# t5-small-nlg-multiwoz21

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on [MultiWOZ 2.1](https://huggingface.co/datasets/ConvLab/multiwoz21).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 128
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 512
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

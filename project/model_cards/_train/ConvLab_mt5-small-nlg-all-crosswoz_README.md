---
language:
- zh
license: apache-2.0
tags:
- mt5-small
- text2text-generation
- natural language generation
- conversational system
- task-oriented dialog
datasets:
- ConvLab/crosswoz
metrics:
- Slot Error Rate
- sacrebleu

model-index:
- name: mt5-small-nlg-all-crosswoz
  results:
  - task:
      type: text2text-generation
      name: natural language generation
    dataset:
      type: ConvLab/crosswoz
      name: CrossWOZ
      split: test
      revision: 4a3e56082543ed9eecb9c76ef5eadc1aa0cc5ca0
    metrics:
      - type: Slot Error Rate
        value: 6.9
        name: SER
      - type: sacrebleu
        value: 21.0
        name: BLEU

widget:
- text: "[Inform][酒店]([价格][100-200元],[评分][5分]);[greet][General]([][]);[Request][酒店]([名称][])\n\nuser: "
- text: "[Recommend][酒店]([名称][北京京仪大酒店],[名称][北京贵都大酒店]);[Inform][酒店]([酒店设施-健身房-否][]);[NoOffer][酒店]([][])\n\nsystem: "

inference:
  parameters:
    max_length: 100

---

# mt5-small-nlg-all-crosswoz

This model is a fine-tuned version of [mt5-small](https://huggingface.co/mt5-small) on [CrossWOZ](https://huggingface.co/datasets/ConvLab/crosswoz) both user and system utterances.

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
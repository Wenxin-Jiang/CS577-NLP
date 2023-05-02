---
language:
- zh
license: apache-2.0
tags:
- mt5-small
- text2text-generation
- natural language understanding
- conversational system
- task-oriented dialog
datasets:
- ConvLab/crosswoz
metrics:
- Dialog acts Accuracy
- Dialog acts F1

model-index:
- name: mt5-small-nlu-all-crosswoz
  results:
  - task:
      type: text2text-generation
      name: natural language understanding
    dataset:
      type: ConvLab/crosswoz
      name: CrossWOZ
      split: test
      revision: 4a3e56082543ed9eecb9c76ef5eadc1aa0cc5ca0
    metrics:
      - type: Dialog acts Accuracy
        value: 84.0
        name: Accuracy
      - type: Dialog acts F1
        value: 90.1
        name: F1

widget:
- text: "user: 你好，给我推荐一个评分是5分，价格在100-200元的酒店。"
- text: "system: 抱歉，为您搜索了一些经济型酒店都没有健身房。其他类型的一些酒店行吗？比如北京贵都大酒店、北京京仪大酒店这些也是很好的，就是价格高了一些。"

inference:
  parameters:
    max_length: 100

---

# mt5-small-nlu-all-crosswoz

This model is a fine-tuned version of [mt5-small](https://huggingface.co/mt5-small) on [CrossWOZ](https://huggingface.co/datasets/ConvLab/crosswoz) both user and system utterances.

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 256
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
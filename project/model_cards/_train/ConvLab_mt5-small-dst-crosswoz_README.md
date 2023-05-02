---
language:
- zh
license: apache-2.0
tags:
- mt5-small
- text2text-generation
- dialog state tracking
- conversational system
- task-oriented dialog
datasets:
- ConvLab/crosswoz
metrics:
- Joint Goal Accuracy
- Slot F1

model-index:
- name: mt5-small-dst-crosswoz
  results:
  - task:
      type: text2text-generation
      name: dialog state tracking
    dataset:
      type: ConvLab/crosswoz
      name: CrossWOZ
      split: test
      revision: 4a3e56082543ed9eecb9c76ef5eadc1aa0cc5ca0
    metrics:
      - type: Joint Goal Accuracy
        value: 62.5
        name: JGA
      - type: Slot F1
        value: 90.4
        name: Slot F1

widget:
- text: "user: 你好，给我推荐一个评分是5分，价格在100-200元的酒店。\nsystem: 推荐您去北京布提克精品酒店。\nuser: 北京布提克精品酒店酒店是什么类型，有健身房吗？\nsystem: 北京布提克精品酒店评分是4.8分，是高档型酒店，没有健身房。\nuser: 给我推荐一个评分在4.5分以上，游玩时间在2小时 - 3小时的免费景点。"
- text: "user: 您好，请帮我推荐个4.5分以上的景点游玩呗，最好把周边有什么酒店告诉我一下。\nsystem: 那我推荐您故宫，周边的酒店有北京天伦王朝酒店, 北京首都宾馆, 北京贵都大酒店。\nuser: 那请在故宫周边的酒店里，帮我找个评分在4.5分以上的店。\nsystem: 北京贵都大酒店符合您的要求。\nuser: 请帮我呼叫一辆从故宫到北京贵都大酒店的出租车，告诉我车型和车牌号。"

inference:
  parameters:
    max_length: 100

---

# mt5-small-dst-crosswoz

This model is a fine-tuned version of [mt5-small](https://huggingface.co/mt5-small) on [CrossWOZ](https://huggingface.co/datasets/ConvLab/crosswoz).

Refer to [ConvLab-3](https://github.com/ConvLab/ConvLab-3) for model description and usage.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
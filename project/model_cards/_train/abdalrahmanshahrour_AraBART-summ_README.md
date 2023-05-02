---
license: apache-2.0
language:
  - ar
tags:
  - summarization
  - AraBERT
  - BERT
  - BERT2BERT
  - MSA
  - Arabic Text Summarization
  - Arabic News Title Generation
  - Arabic Paraphrasing
  - Summarization
  - generated_from_trainer
  - Transformers
  - PyTorch
widget:
  - text: >-
      شهدت مدينة طرابلس، مساء أمس الأربعاء، احتجاجات شعبية وأعمال شغب لليوم
      الثالث على التوالي، وذلك بسبب تردي الوضع المعيشي والاقتصادي. واندلعت
      مواجهات عنيفة وعمليات كر وفر ما بين الجيش اللبناني والمحتجين استمرت
      لساعات، إثر محاولة فتح الطرقات المقطوعة، ما أدى إلى إصابة العشرات من
      الطرفين.
datasets:
  - xlsum
model-index:
  - name: arabartsummarization
    results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AraBART-summ

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

## Validation Metrics

- Loss: 2.3417
- Rouge1: 2.353
- Rouge2: 1.103
- RougeL: 1.176
- RougeLsum: 1.521

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.7555        | 1.0   | 9380 | 2.3417          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

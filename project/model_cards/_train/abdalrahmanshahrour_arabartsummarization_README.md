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

# arabartsummarization


## Model description

The model can be used as follows:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from arabert.preprocess import ArabertPreprocessor

model_name="abdalrahmanshahrour/arabartsummarization"
preprocessor = ArabertPreprocessor(model_name="")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
pipeline = pipeline("text2text-generation",model=model,tokenizer=tokenizer)

text = "شهدت مدينة طرابلس، مساء أمس الأربعاء، احتجاجات شعبية وأعمال شغب لليوم الثالث على التوالي، وذلك بسبب تردي الوضع المعيشي والاقتصادي. واندلعت مواجهات عنيفة وعمليات كر وفر ما بين الجيش اللبناني والمحتجين استمرت لساعات، إثر محاولة فتح الطرقات المقطوعة، ما أدى إلى إصابة العشرات من الطرفين."
text = preprocessor.preprocess(text)

result = pipeline(text,
            pad_token_id=tokenizer.eos_token_id,
            num_beams=3,
            repetition_penalty=3.0,
            max_length=200,
            length_penalty=1.0,
            no_repeat_ngram_size = 3)[0]['generated_text']
result
>>> "تجددت الاشتباكات بين الجيش اللبناني ومحتجين في مدينة طرابلس شمالي لبنان."
```

## Validation Metrics

- Loss: 2.3394
- Rouge1: 1.142
- Rouge2: 0.227
- RougeL: 1.124
- RougeLsum: 1.234

## Intended uses & limitations

More information needed

## Training and evaluation data

42.21K row in total
  - Training : 37.52K rows
  - Evaluation : 4.69K rows

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.784         | 1.0   | 9380  | 2.3820          |
| 2.4954        | 2.0   | 18760 | 2.3418          |
| 2.2223        | 3.0   | 28140 | 2.3394          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

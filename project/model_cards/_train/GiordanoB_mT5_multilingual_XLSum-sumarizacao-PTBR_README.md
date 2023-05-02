---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-sumarizacao-PTBR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-sumarizacao-PTBR

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3870
- Rouge1: 42.0195
- Rouge2: 24.9493
- Rougel: 32.3653
- Rougelsum: 37.9982
- Gen Len: 77.0

## Let's see the model in action!
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

model_name = "GiordanoB/mT5_multilingual_XLSum-sumarizacao-PTBR"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    input_ids = tokenizer(
        [WHITESPACE_HANDLER(sumariosDuplos[i])],
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        max_length=200,
        min_length=75,
        no_repeat_ngram_size=2,
        num_beams=5
    )[0]

    summary = tokenizer.decode(
        output_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )

    sumariosFinal.append(summary)
    print(i,"\n",summary,"\n")
   ```
    
## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 15   | 1.5687          | 32.2316 | 18.9289 | 23.918  | 27.7216   | 51.5714 |
| No log        | 2.0   | 30   | 1.4530          | 41.2297 | 26.1883 | 30.8012 | 37.1727   | 69.5714 |
| No log        | 3.0   | 45   | 1.4043          | 40.8986 | 24.4993 | 31.349  | 36.8782   | 72.2143 |
| No log        | 4.0   | 60   | 1.3908          | 42.1019 | 25.5555 | 32.9018 | 38.0202   | 74.5    |
| No log        | 5.0   | 75   | 1.3870          | 42.0195 | 24.9493 | 32.3653 | 37.9982   | 77.0    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

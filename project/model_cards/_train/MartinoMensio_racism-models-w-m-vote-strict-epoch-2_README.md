---
language: es
license: mit

widget:
- text: "y porqué es lo que hay que hacer con los menas y con los adultos también!!!! NO a los inmigrantes ilegales!!!!"
---

### Description
This model is a fine-tuned version of [BETO (spanish bert)](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) that has been trained on the *Datathon Against Racism* dataset (2022)

We performed several experiments that will be described in the upcoming paper "Estimating Ground Truth in a Low-labelled Data Regime:A Study of Racism Detection in Spanish" (NEATClasS 2022)
We applied 6 different methods ground-truth estimations, and for each one we performed 4 epochs of fine-tuning. The result is made of 24 models:

| method	| epoch 1	| epoch 3	| epoch 3	| epoch 4	|
|---	|---	|---	|---	|---	|
| raw-label	| [raw-label-epoch-1](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-1)	| [raw-label-epoch-2](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-2)	| [raw-label-epoch-3](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-3)	| [raw-label-epoch-4](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-4)	|
| m-vote-strict	| [m-vote-strict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-1)	| [m-vote-strict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-2)	| [m-vote-strict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-3)	| [m-vote-strict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-4)	|
| m-vote-nonstrict	| [m-vote-nonstrict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-1)	| [m-vote-nonstrict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-2)	| [m-vote-nonstrict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-3)	| [m-vote-nonstrict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-4)	|
| regression-w-m-vote	| [regression-w-m-vote-epoch-1](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-1)	| [regression-w-m-vote-epoch-2](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-2)	| [regression-w-m-vote-epoch-3](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-3)	| [regression-w-m-vote-epoch-4](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-4)	|
| w-m-vote-strict	| [w-m-vote-strict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-1)	| [w-m-vote-strict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-2)	| [w-m-vote-strict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-3)	| [w-m-vote-strict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-4)	|
| w-m-vote-nonstrict	| [w-m-vote-nonstrict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-1)	| [w-m-vote-nonstrict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-2)	| [w-m-vote-nonstrict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-3)	| [w-m-vote-nonstrict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-4)	|


This model is `w-m-vote-strict-epoch-2`

### Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
  
model_name = 'w-m-vote-strict-epoch-2'
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
full_model_path = f'MartinoMensio/racism-models-{model_name}'
model = AutoModelForSequenceClassification.from_pretrained(full_model_path)

pipe = pipeline("text-classification", model = model, tokenizer = tokenizer)

texts = [
    'y porqué es lo que hay que hacer con los menas y con los adultos también!!!! NO a los inmigrantes ilegales!!!!',
    'Es que los judíos controlan el mundo'
]
print(pipe(texts))
# [{'label': 'racist', 'score': 0.8647435903549194}, {'label': 'non-racist', 'score': 0.9660486578941345}]
```

For more details, see https://github.com/preyero/neatclass22

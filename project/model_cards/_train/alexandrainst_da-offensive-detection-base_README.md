---
license: mit
widget:
- text: "Din store idiot"
---

# Danish Offensive Text Detection based on XLM-Roberta-Base

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on a dataset consisting of approximately 5 million Facebook comments on [DR](https://dr.dk/)'s public Facebook pages. The labels have been automatically generated using weak supervision, based on the [Snorkel](https://www.snorkel.org/) framework.

The model achieves SOTA on a test set consisting of 600 Facebook comments annotated using majority vote by three annotators, of which 35.8% were labelled as offensive:

| **Model** | **Precision** | **Recall** | **F1-score** | **F2-score** |
| :-------- | :------------ | :--------- | :----------- | :----------- |
| `alexandrainst/da-offensive-detection-base` (this) | 74.81% | **89.77%** | **81.61%** | **86.32%** |
| [`alexandrainst/da-offensive-detection-base`](https://huggingface.co/alexandrainst/da-offensive-detection-base) | 74.13% | 89.30% | 81.01% | 85.79% |
| [`A&ttack`](https://github.com/ogtal/A-ttack) | **97.32%** | 50.70% | 66.67% | 56.07% |
| [`alexandrainst/da-hatespeech-detection-small`](https://huggingface.co/alexandrainst/da-hatespeech-detection-small) | 86.43% | 56.28% | 68.17% | 60.50% |
| [`Guscode/DKbert-hatespeech-detection`](https://huggingface.co/Guscode/DKbert-hatespeech-detection) | 75.41% | 42.79% | 54.60% | 46.84% |

## Using the model

You can use the model simply by running the following:

```python
>>> from transformers import pipeline
>>> offensive_text_pipeline = pipeline(model="alexandrainst/da-offensive-detection-base")
>>> offensive_text_pipeline("Din store idiot")
[{'label': 'Offensive', 'score': 0.9997463822364807}]
```

Processing multiple documents at the same time can be done as follows:

```python
>>> offensive_text_pipeline(["Din store idiot", "ej hvor godt :)"])
[{'label': 'Offensive', 'score': 0.9997463822364807}, {'label': 'Not offensive', 'score': 0.9996451139450073}]
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- gradient_accumulation_steps: 1
- total_train_batch_size: 32
- seed: 4242
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- max_steps: 500000
- fp16: True
- eval_steps: 1000
- early_stopping_patience: 100


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
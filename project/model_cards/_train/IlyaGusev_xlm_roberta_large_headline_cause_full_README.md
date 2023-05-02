---
language: 
- ru
- en
tags:
- xlm-roberta-large
datasets:
- IlyaGusev/headline_cause
license: apache-2.0
widget:
- text: "Песков опроверг свой перевод на удаленку</s>Дмитрий Песков перешел на удаленку"
---

# XLM-RoBERTa HeadlineCause Full

## Model description

This model was trained to predict the presence of causal relations between two headlines. This model is for the Full task with 7 possible labels: titles are almost the same, A causes B, B causes A, A refutes B, B refutes A, A linked with B in another way, A is not linked to B. English and Russian languages are supported.

You can use hosted inference API to infer a label for a headline pair. To do this, you shoud seperate headlines with ```</s>``` token.
For example:
```
Песков опроверг свой перевод на удаленку</s>Дмитрий Песков перешел на удаленку
```

## Intended uses & limitations

#### How to use

```python
from tqdm.notebook import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def get_batch(data, batch_size):
    start_index = 0
    while start_index < len(data):
        end_index = start_index + batch_size
        batch = data[start_index:end_index]
        yield batch
        start_index = end_index


def pipe_predict(data, pipe, batch_size=64):
    raw_preds = []
    for batch in tqdm(get_batch(data, batch_size)):
        raw_preds += pipe(batch)
    return raw_preds

MODEL_NAME = TOKENIZER_NAME = "IlyaGusev/xlm_roberta_large_headline_cause_full"
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME, do_lower_case=False)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, framework="pt", return_all_scores=True)
texts = [
    (
        "Judge issues order to allow indoor worship in NC churches",
        "Some local churches resume indoor services after judge lifted NC governor’s restriction"
    ),
    (
        "Gov. Kevin Stitt defends $2 million purchase of malaria drug touted by Trump",
        "Oklahoma spent $2 million on malaria drug touted by Trump"
    ),
    (
        "Песков опроверг свой перевод на удаленку",
        "Дмитрий Песков перешел на удаленку"
    )
]
pipe_predict(texts, pipe)
```

#### Limitations and bias

The models are intended to be used on news headlines. No other limitations are known.

## Training data

* HuggingFace dataset: [IlyaGusev/headline_cause](https://huggingface.co/datasets/IlyaGusev/headline_cause)
* GitHub: [IlyaGusev/HeadlineCause](https://github.com/IlyaGusev/HeadlineCause)

## Training procedure

* Notebook: [HeadlineCause](https://colab.research.google.com/drive/1NAnD0OJ0TnYCJRsHpYUyYkjr_yi8ObcA)
* Stand-alone script: [train.py](https://github.com/IlyaGusev/HeadlineCause/blob/main/headline_cause/train.py)

## Eval results

Evaluation results can be found in the [arxiv paper](https://arxiv.org/pdf/2108.12626.pdf).

### BibTeX entry and citation info

```bibtex
@misc{gusev2021headlinecause,
      title={HeadlineCause: A Dataset of News Headlines for Detecting Causalities}, 
      author={Ilya Gusev and Alexey Tikhonov},
      year={2021},
      eprint={2108.12626},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

---
license: apache-2.0
language: ca
tags:
- "catalan"
datasets:
- catalonia_independence
metrics:
- accuracy
model-index:
- name: roberta-base-ca-finetuned-mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: catalonia_independence
      type: catalonia_independence
      args: catalan
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7611940298507462
widget:
 - text: "Puigdemont, a l'estat espanyol: Quatre anys després, ens hem guanyat el dret a dir prou"
 - text: "Llarena demana la detenció de Comín i Ponsatí aprofitant que són a Itàlia amb Puigdemont"
 - text: "Assegura l'expert que en un 46% els catalans s'inclouen dins del que es denomina com el doble sentiment identitari. És a dir, se senten tant catalans com espanyols. 1 de cada cinc, en canvi, té un sentiment excloent, només se senten catalans, i un 4% sol espanyol."
---

# roberta-base-ca-finetuned-catalonia-independence-detector

This model is a fine-tuned version of [BSC-TeMU/roberta-base-ca](https://huggingface.co/BSC-TeMU/roberta-base-ca) on the catalonia_independence dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6065
- Accuracy: 0.7612

<details>

## Training and evaluation data

The data was collected over 12 days during February and March of 2019 from tweets posted in Barcelona, and during September of 2018 from tweets posted in the town of Terrassa, Catalonia.

Each corpus is annotated with three classes: AGAINST, FAVOR and NEUTRAL, which express the stance towards the target - independence of Catalonia.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 377  | 0.6311          | 0.7453   |
| 0.7393        | 2.0   | 754  | 0.6065          | 0.7612   |
| 0.5019        | 3.0   | 1131 | 0.6340          | 0.7547   |
| 0.3837        | 4.0   | 1508 | 0.6777          | 0.7597   |
| 0.3837        | 5.0   | 1885 | 0.7232          | 0.7582   |


</details>

### Model in action 🚀

Fast usage with **pipelines**:

```python

from transformers import pipeline

model_path = "JonatanGk/roberta-base-ca-finetuned-catalonia-independence-detector"
independence_analysis = pipeline("text-classification", model=model_path, tokenizer=model_path)

independence_analysis(
    "Assegura l'expert que en un 46% els catalans s'inclouen dins del que es denomina com el doble sentiment identitari. És a dir, se senten tant catalans com espanyols. 1 de cada cinc, en canvi, té un sentiment excloent, només se senten catalans, i un 4% sol espanyol."
    )
# Output:
[{'label': 'AGAINST', 'score': 0.7457581758499146}]

independence_analysis(
    "Llarena demana la detenció de Comín i Ponsatí aprofitant que són a Itàlia amb Puigdemont"
    )
# Output:
[{'label': 'NEUTRAL', 'score': 0.7436802983283997}] 
    
independence_analysis(
    "Puigdemont, a l'estat espanyol: Quatre anys després, ens hem guanyat el dret a dir prou"
    )
# Output:
[{'label': 'FAVOR', 'score': 0.9040119647979736}]


```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonatanGk/Shared-Colab/blob/master/Catalonia_independence_Detector_(CATALAN).ipynb#scrollTo=j29NHJtOyAVU)


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3


## Citation

Thx to HF.co & [@lewtun](https://github.com/lewtun) for Dataset ;)

> Special thx to [Manuel Romero/@mrm8488](https://huggingface.co/mrm8488) as my mentor & R.C.

> Created by [Jonatan Luna](https://JonatanGk.github.io) | [LinkedIn](https://www.linkedin.com/in/JonatanGk/)
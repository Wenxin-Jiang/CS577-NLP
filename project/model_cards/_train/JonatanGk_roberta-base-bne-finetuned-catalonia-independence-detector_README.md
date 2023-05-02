---
license: apache-2.0
language: es
tags:
- "spanish"
datasets:
- catalonia_independence
metrics:
- accuracy
model-index:
- name: roberta-base-bne-finetuned-mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: catalonia_independence
      type: catalonia_independence
      args: spanish
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7880893300248138
widget:
 - text: "Junqueras, sobre la decisión judicial sobre Puigdemont: La justicia que falta en el Estado llega y llegará de Europa"
 - text: "Desconvocada la manifestación del domingo en Barcelona en apoyo a Puigdemont"
---

# roberta-base-bne-finetuned-catalonia-independence-detector

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the catalonia_independence dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9415
- Accuracy: 0.7881

<details>

## Model description

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
| No log        | 1.0   | 378  | 0.5534          | 0.7558   |
| 0.6089        | 2.0   | 756  | 0.5315          | 0.7643   |
| 0.2678        | 3.0   | 1134 | 0.7336          | 0.7816   |
| 0.0605        | 4.0   | 1512 | 0.8809          | 0.7866   |
| 0.0605        | 5.0   | 1890 | 0.9415          | 0.7881   |

</details>

### Model in action 🚀

Fast usage with **pipelines**:

```python

from transformers import pipeline

model_path = "JonatanGk/roberta-base-bne-finetuned-catalonia-independence-detector"
independence_analysis = pipeline("text-classification", model=model_path, tokenizer=model_path)

independence_analysis(
    "Junqueras, sobre la decisión judicial sobre Puigdemont: La justicia que falta en el Estado llega y llegará de Europa"
    )

# Output:
[{'label': 'FAVOR', 'score': 0.9936726093292236}]

independence_analysis(
    "El desafío independentista queda adormecido, y eso que el Gobierno ha sido muy claro en que su propuesta para Cataluña es una agenda de reencuentro, centrada en inversiones e infraestructuras")

# Output:
[{'label': 'AGAINST', 'score': 0.7508948445320129}]

independence_analysis(
    "Desconvocada la manifestación del domingo en Barcelona en apoyo a Puigdemont"
    )

# Output:
[{'label': 'NEUTRAL', 'score': 0.9966907501220703}]

```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonatanGk/Shared-Colab/blob/master/Catalonia_independence_Detector_(SPANISH).ipynb#scrollTo=uNMOXJz38W6U)

### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3

## Citation
Thx to HF.co & [@lewtun](https://github.com/lewtun) for Dataset ;)


> Special thx to [Manuel Romero/@mrm8488](https://huggingface.co/mrm8488) as my mentor & R.C.

> Created by [Jonatan Luna](https://JonatanGk.github.io) | [LinkedIn](https://www.linkedin.com/in/JonatanGk/)
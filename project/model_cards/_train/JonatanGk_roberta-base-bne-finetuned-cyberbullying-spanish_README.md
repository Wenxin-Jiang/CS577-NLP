---
language: es
tags:
- "spanish"
metrics:
- accuracy
widget:
 - text: "Eres mas pequeño que un pitufo!"
 - text: "Eres muy feo!"
 - text: "Odio tu forma de hablar!"
 - text: "Eres tan fea que cuando eras pequeña te echaban de comer por debajo de la puerta."

---

# roberta-base-bne-finetuned-ciberbullying-spanish

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the dataset generated scrapping all social networks (Twitter, Youtube ...) to detect ciberbullying on Spanish.

It achieves the following results on the evaluation set:

- Loss: 0.1657
- Accuracy: 0.9607

## Training and evaluation data

I use the concatenation from multiple datasets generated scrapping social networks (Twitter,Youtube,Discord...)  to fine-tune this model. The total number of sentence pairs is above 360k sentences.

## Training procedure

<details>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Accuracy | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:---------------:|
| 0.1512        | 1.0   | 22227 | 0.9501   | 0.1418          |
| 0.1253        | 2.0   | 44454 | 0.9567   | 0.1499          |
| 0.0973        | 3.0   | 66681 | 0.9594   | 0.1397          |
| 0.0658        | 4.0   | 88908 | 0.9607   | 0.1657          |

</details>

### Model in action 🚀

Fast usage with **pipelines**:

```python
from transformers import pipeline

model_path = "JonatanGk/roberta-base-bne-finetuned-ciberbullying-spanish"
bullying_analysis = pipeline("text-classification", model=model_path, tokenizer=model_path)

bullying_analysis(
    "Desde que te vi me enamoré de ti."
    )

# Output:
[{'label': 'Not_bullying', 'score': 0.9995710253715515}]

bullying_analysis(
    "Eres tan fea que cuando eras pequeña te echaban de comer por debajo de la puerta."
    )
# Output:
[{'label': 'Bullying', 'score': 0.9918262958526611}] 
    
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonatanGk/Shared-Colab/blob/master/Cyberbullying_detection_(SPANISH).ipynb)

### Framework versions

- Transformers 4.10.3
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3


> Special thx to [Manuel Romero/@mrm8488](https://huggingface.co/mrm8488) as my mentor & R.C.

> Created by [Jonatan Luna](https://JonatanGk.github.io) | [LinkedIn](https://www.linkedin.com/in/JonatanGk/)
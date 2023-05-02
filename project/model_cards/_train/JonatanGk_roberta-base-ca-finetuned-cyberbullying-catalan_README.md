---
language: ca
tags:
- "catalan"
metrics:
- accuracy
widget:
 - text: "Ets més petita que un barrufet!!"
 - text: "Ets tan lletja que et donaven de menjar per sota la porta."
 
---
# roberta-base-ca-finetuned-cyberbullying-catalan

This model is a fine-tuned version of [BSC-TeMU/roberta-base-ca](https://huggingface.co/BSC-TeMU/roberta-base-ca) on the dataset generated scrapping all social networks (Twitter, Youtube ...) to detect cyberbullying on Catalan.

It achieves the following results on the evaluation set:
- Loss: 0.1508
- Accuracy: 0.9665

## Training and evaluation data

I use the concatenation from multiple datasets generated scrapping social networks (Twitter,Youtube,Discord...)  to fine-tune this model. The total number of sentence pairs is above 410k sentences. Trained similar method at [roberta-base-bne-finetuned-cyberbullying-spanish](https://huggingface.co/JonatanGk/roberta-base-bne-finetuned-cyberbullying-spanish)

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

</details>

### Model in action 🚀

Fast usage with **pipelines**:

```python
from transformers import pipeline

model_path = "JonatanGk/roberta-base-ca-finetuned-ciberbullying-catalan"
bullying_analysis = pipeline("text-classification", model=model_path, tokenizer=model_path)

bullying_analysis(
    "Des que et vaig veure m'en vaig enamorar de tu."
    )
    
# Output:
[{'label': 'Not_bullying', 'score': 0.9996786117553711}]

bullying_analysis(
    "Ets tan lletja que et donaven de menjar per sota la porta."
    )
    
# Output:
[{'label': 'Bullying', 'score': 0.9927878975868225}]
    
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonatanGk/Shared-Colab/blob/master/Cyberbullying_detection_(CATALAN).ipynb)

### Framework versions
- Transformers 4.10.3
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3

## Citation

```bibtex
@inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
}
```

> Special thx to [Manuel Romero/@mrm8488](https://huggingface.co/mrm8488) as my mentor & R.C.

> Created by [Jonatan Luna](https://JonatanGk.github.io) | [LinkedIn](https://www.linkedin.com/in/JonatanGk/)

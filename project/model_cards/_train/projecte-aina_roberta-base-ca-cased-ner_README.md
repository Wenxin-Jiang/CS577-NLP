---

language:

- ca

license: apache-2.0

tags:

- "catalan"

- "named entity recognition"

- "ner"

- "CaText"

- "Catalan Textual Corpus"

datasets:

- "projecte-aina/ancora-ca-ner"  

metrics:

- f1

model-index:
- name: roberta-base-ca-cased-ner
  results:
  - task: 
      type: token-classification 
    dataset:
      type:   projecte-aina/ancora-ca-ner
      name: ancora-ca-ner
    metrics:
      - type: f1
        value: 0.8813

widget:

- text: "Em dic Lluïsa i visc a Santa Maria del Camí." 

- text: "L'Aina, la Berta i la Norma són molt amigues."

- text: "El Martí llegeix el Cavall Fort."

---

# Catalan BERTa (RoBERTa-base) finetuned for Named Entity Recognition.

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-uses-and-limitations)
- [How to Use](#how-to-use)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
- [Evaluation](#evaluation)
   - [Variable and metrics](#variable-and-metrics)
   - [Evaluation results](#evaluation-results)
- [Additional information](#addional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer))
</details>


## Model description

The **roberta-base-ca-cased-ner** is a Named Entity Recognition (NER) model for the Catalan language fine-tuned from the [BERTa](https://huggingface.co/PlanTL-GOB-ES/roberta-base-ca) model, a [RoBERTa](https://arxiv.org/abs/1907.11692) base model pre-trained on a medium-size corpus collected from publicly available corpora and crawlers (check the BERTa model card for more details).

## Intended uses and limitations


## How to use


## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training
We used the NER dataset in Catalan called [Ancora-ca-ner](https://huggingface.co/datasets/projecte-aina/ancora-ca-ner) for training and evaluation.

## Evaluation 
We evaluated the _roberta-base-ca-cased-ner_ on the Ancora-ca-ner test set against standard multilingual and monolingual baselines:

| Model        | Ancora-ca-ner (F1)| 
| ------------|:-------------|
| roberta-base-ca-cased-ner | **88.13** |
| mBERT       | 86.38 |
| XLM-RoBERTa | 87.66 | 
| WikiBERT-ca | 77.66 |

For more details, check the fine-tuning and evaluation scripts in the official [GitHub repository](https://github.com/projecte-aina/club).

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to aina@bsc.es

### Copyright
Copyright (c) 2021 Text Mining Unit at Barcelona Supercomputing Center 

### Licensing Information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Citation information

If you use any of these resources (datasets or models) in your work, please cite our latest paper:
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

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.
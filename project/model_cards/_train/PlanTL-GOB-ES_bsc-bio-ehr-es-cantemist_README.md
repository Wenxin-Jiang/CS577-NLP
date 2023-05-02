---
language: 
  - es
tags:
- biomedical
- clinical
- eHR
- spanish
license: apache-2.0
datasets:
- "PlanTL-GOB-ES/cantemist-ner"
metrics:
- f1

model-index:
- name: PlanTL-GOB-ES/bsc-bio-ehr-es-cantemist
  results:
  - task:
      type: token-classification
    dataset:
      name: cantemist-ner
      type: PlanTL-GOB-ES/cantemist-ner
    metrics:
      - name: f1
        type: f1
        value: 0.8340
widget:
- text: "El diagnóstico definitivo de nuestro paciente fue de un Adenocarcinoma de pulmón cT2a cN3 cM1a Estadio IV (por una única lesión pulmonar contralateral) PD-L1 90%, EGFR negativo, ALK negativo y ROS-1 negativo."
- text: "Durante el ingreso se realiza una TC, observándose un nódulo pulmonar en el LII y una masa renal derecha indeterminada. Se realiza punción biopsia del nódulo pulmonar, con hallazgos altamente sospechosos de carcinoma."
- text: "Trombosis paraneoplásica con sospecha de hepatocarcinoma por imagen, sobre hígado cirrótico, en paciente con índice Child-Pugh B."

---


# Spanish RoBERTa-base biomedical model finetuned for the Named Entity Recognition (NER) task on the Cantemist dataset.

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)
  
</details>

## Model description
A fine-tuned version of the [bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) model, a [RoBERTa](https://arxiv.org/abs/1907.11692) base model and has been pre-trained using the largest Spanish biomedical corpus known to date, composed of biomedical documents, clinical cases and EHR documents for a total of 1.1B tokens of clean and deduplicated text processed.

For more details about the corpora and training, check the _bsc-bio-ehr-es_ model card.

## Intended uses and limitations

## How to use

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated. 

## Training
The dataset used is [CANTEMIST](https://huggingface.co/datasets/PlanTL-GOB-ES/cantemist-ner), a NER dataset annotated with tumor morphology entities. For further information, check the [official website](https://temu.bsc.es/cantemist/).

## Evaluation 
F1 Score: 0.8340

For evaluation details visit our [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es).

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to <plantl-gob-es@bsc.es>

### Copyright
Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

### Citing information
If you use these models, please cite our work:

```bibtext
@inproceedings{carrino-etal-2022-pretrained,
    title = "Pretrained Biomedical Language Models for Clinical {NLP} in {S}panish",
    author = "Carrino, Casimiro Pio  and
      Llop, Joan  and
      P{\`a}mies, Marc  and
      Guti{\'e}rrez-Fandi{\~n}o, Asier  and
      Armengol-Estap{\'e}, Jordi  and
      Silveira-Ocampo, Joaqu{\'\i}n  and
      Valencia, Alfonso  and
      Gonzalez-Agirre, Aitor  and
      Villegas, Marta",
    booktitle = "Proceedings of the 21st Workshop on Biomedical Language Processing",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.bionlp-1.19",
    doi = "10.18653/v1/2022.bionlp-1.19",
    pages = "193--199",
    abstract = "This work presents the first large-scale biomedical Spanish language models trained from scratch, using large biomedical corpora consisting of a total of 1.1B tokens and an EHR corpus of 95M tokens. We compared them against general-domain and other domain-specific models for Spanish on three clinical NER tasks. As main results, our models are superior across the NER tasks, rendering them more convenient for clinical NLP applications. Furthermore, our findings indicate that when enough data is available, pre-training from scratch is better than continual pre-training when tested on clinical tasks, raising an exciting research question about which approach is optimal. Our models and fine-tuning scripts are publicly available at HuggingFace and GitHub.",
}
```

### Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.

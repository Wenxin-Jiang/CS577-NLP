---

language:

- es

license: apache-2.0

tags:

- "legal"

- "spanish"

datasets:

- "legal_ES"

- "temu_legal"  

metrics:

- "ppl"

widget:
- text: "La ley fue <mask> finalmente." 
- text: "El Tribunal <mask> desestimó el recurso de amparo."
- text: "Hay base legal dentro del marco <mask> actual."

---

# RoBERTa base trained with Spanish Legal Domain Corpora

## Table of contents
<details>
<summary>Click to expand</summary>

- [Overview](#overview)
- [Model description](#model-description)
- [Intended uses and limitations](#intended-uses-and-limitations)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citation Information](#citation-information)
  - [Disclaimer](#disclaimer)
  
</details>


## Overview
- **Architecture:** roberta-base
- **Language:** Spanish
- **Task:** fill-mask
- **Data:** Legal

## Model description
The **RoBERTalex** is a transformer-based masked language model for the Spanish language. It is based on the [RoBERTa](https://arxiv.org/abs/1907.11692) base model and has been pre-trained using a large [Spanish Legal Domain Corpora](https://zenodo.org/record/5495529), with a total of 8.9GB of text.

## Intended uses and limitations
The **RoBERTalex** model is ready-to-use only for masked language modeling to perform the Fill Mask task (try the inference API or read the next section).
However, it is intended to be fine-tuned on non-generative downstream tasks such as Question Answering, Text Classification, or Named Entity Recognition.
You can use the raw model for fill mask or fine-tune it to a downstream task.

## How to use
Here is how to use this model:

```python
>>> from transformers import pipeline
>>> from pprint import pprint
>>> unmasker = pipeline('fill-mask', model='PlanTL-GOB-ES/RoBERTalex')
>>> pprint(unmasker("La ley fue <mask> finalmente."))
[{'score': 0.21217258274555206,
  'sequence': ' La ley fue modificada finalmente.',
  'token': 5781,
  'token_str': ' modificada'},
 {'score': 0.20414969325065613,
  'sequence': ' La ley fue derogada finalmente.',
  'token': 15951,
  'token_str': ' derogada'},
 {'score': 0.19272951781749725,
  'sequence': ' La ley fue aprobada finalmente.',
  'token': 5534,
  'token_str': ' aprobada'},
 {'score': 0.061143241822719574,
  'sequence': ' La ley fue revisada finalmente.',
  'token': 14192,
  'token_str': ' revisada'},
 {'score': 0.041809432208538055,
  'sequence': ' La ley fue aplicada finalmente.',
  'token': 12208,
  'token_str': ' aplicada'}]

```

Here is how to use this model to get the features of a given text in PyTorch:

```python
>>> from transformers import RobertaTokenizer, RobertaModel
>>> tokenizer = RobertaTokenizer.from_pretrained('PlanTL-GOB-ES/RoBERTalex')
>>> model = RobertaModel.from_pretrained('PlanTL-GOB-ES/RoBERTalex')
>>> text = "Gracias a los datos legales se ha podido desarrollar este modelo del lenguaje."
>>> encoded_input = tokenizer(text, return_tensors='pt')
>>> output = model(**encoded_input)
>>> print(output.last_hidden_state.shape)
torch.Size([1, 16, 768])
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training data
The [Spanish Legal Domain Corpora](https://zenodo.org/record/5495529) corpora comprise multiple digital resources and it has a total of 8.9GB of textual data. Part of it has been obtained
from [previous work](https://aclanthology.org/2020.lt4gov-1.6/). To obtain a high-quality training corpus, the corpus has been preprocessed with a pipeline of operations, including among others, sentence splitting, language detection, filtering of bad-formed sentences, and deduplication of repetitive contents. During the process, document boundaries are kept.

### Training procedure
The training corpus has been tokenized using a byte version of Byte-Pair Encoding (BPE) used in the original [RoBERTA](https://arxiv.org/abs/1907.11692) model with a vocabulary size of 50,262 tokens.

The **RoBERTalex** pre-training consists of a masked language model training, that follows the approach employed for the RoBERTa base. The model was trained until convergence with 2 computing nodes, each one with 4 NVIDIA V100 GPUs of 16GB VRAM.

## Evaluation 

Due to the lack of domain-specific evaluation data, the model was evaluated on general domain tasks, where it obtains reasonable performance. We fine-tuned the model in the following task:

| Dataset      | Metric   | **RoBERtalex**   |
|--------------|----------|------------|
| UD-POS       | F1       |     0.9871 |
| CoNLL-NERC   | F1       |     0.8323 |
| CAPITEL-POS  | F1       |     0.9788|
| CAPITEL-NERC | F1       |     0.8394 |
| STS          | Combined |     0.7374 |
| MLDoc        | Accuracy |     0.9417 |
| PAWS-X       | F1       |     0.7304 |
| XNLI         | Accuracy |     0.7337 |

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

## Citing information

```
@misc{gutierrezfandino2021legal,
      title={Spanish Legalese Language Model and Corpora}, 
      author={Asier Gutiérrez-Fandiño and Jordi Armengol-Estapé and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2021},
      eprint={2110.12201},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third  parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
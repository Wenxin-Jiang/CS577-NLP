---
language: "ca"
license: mit
tags:
- summarization
widget:
- text: "El projecte AINA generarà els recursos digitals i lingüístics necessaris per facilitar el desenvolupament d’aplicacions basades en la intel·ligència artificial i les tecnologies de la llengua, com ara els assistents de veu, els traductors automàtics o els agents conversacionals en català. L’objectiu últim és que la ciutadania pugui participar en català en el món digital al mateix nivell que els parlants d’una llengua global, com ara l’anglès, i evitar així l’extinció digital de la llengua. El primer recurs generat és el corpus del català per entrenar els algoritmes d’intel·ligència artificial (IA), el més gran creat fins al moment, amb 1.770 milions de metadades associades a paraules. El proper pas serà generar els models de la llengua, models de la parla i models de traducció utilitzant xarxes neuronals multicapa, perquè les empreses que creen aplicacions basades en intel·ligència artificial (IA), com ara assistents de veu, traductors automàtics, agents conversacionals, etc., puguin fer-ho fàcilment en català."
- text: "El Govern vol que el català també sigui una llengua útil per a la tecnologia i per comunciar-se amb les màquines. Per això, el projecte AINA, impulsat pel Departament de la Vicepresidència, Polítiques Digitals i Territori en col·laboració amb el Barcelona Supercomputing Center (BSC), llançarà el 17 de febrer una campanya de captació de veus per generar el primer corpus o \"diccionari\" de veu del català amb l'objectiu de fer que la tecnologia parli i entengui el català i la ciutadania s'hi pugui relacionar amb aquesta llengua. Per a l'executiu, aquest projecte és d'una \"importància cabdal\", com ha detallat el vicepresident, Jordi Puigneró, també per reforçar la llengua catalana a Internet. El pressupost que s'hi destinarà aquest any és de tres milions d'euros. Per això, amb el lema \"La nostra llengua és la teva veu\", convida la ciutadania de totes les variants dialectals del català ha compartir la seva veu mitjançant la lectura d'uns textos. La fita que s'ha marcat AINA per aquest any és la creació de la primera versió d'aquest diccionari de veus en català, amb \"com més hores de veu i com més diverses millor\". El Govern confia en una bona resposta a la campanya, que arrencarà a partir de demà, i que es desplegarà per tot el territori de parla catalana, per comptar amb diverses variants dialectals. No hi ha limitació d'edat per a qui vulgui participar, i és important que la gent que participi es registri per obtenir més informació sobre genere, edat i distribució geogràfica. Ara com ara hi ha 1.000 hores de veu i el repte és aconseguir arribar a les 2.000 (amb transcripció) aquest any. El vicepresident i conseller de Polítiques Digitals, Jordi Puigneró, ha recordat que fa un any es va donar el tret de sortida al projecte AINA, una aposta per a l'ús del català en l'àmbit tecnològic. El projecte implica un impuls del català en les eines digitals i per \"conquerir nous territoris\", que passen per noves plataformes i nous dispositius. També és un projecte per \"garantir drets\". \"Els catalanes tenim dret a poder relacionar-nos en català amb les maquines i evitar haver de canviar de llengua a l'hora de parlar amb les maquines\", ha remarcat Puigneró. Un altre objectiu d'aquest projecte passa per \"generar talent digital\" i un ecosistema en l'àmbit de la intel·ligència artificial. \"Ens toca ser un país digital\", ha insistit Puigneró. I per què AINA? \"La filla de la Norma, que porta el nom de la seva àvia, Aina Moll, la primera directora de política lingüística de la Generalitat\", ha explicat el vicepresident. Per tot plegat, aquest dimecres arrenca la campanya de captació de veus. \"Volem socialitzar AINA cap a la ciutadania i que molta gent vulgui ser la seva parella lingüística i pugui aprendre el català\", ha dit Puigneró, que ha demanat que aquesta sigui una tasca de tots. El projecte, a dia d'avui, ja coneix la sintaxis del català. En aquesta nova fase, a partir de demà, també ha de conèixer el lèxic i la semàntica, i tota la part oral de la llengua catalana. \"Si ja tenim la columna vertebral i l'esquelet, ara hem de construir la seva musculatura\", ha apuntat el vicepresident. La campanya es farà a través d'una web que permetrà que qualsevol persona pugui ensenyar a AINA a aprendre català. I com es pot fer? És senzill. A partir que arrenqui la campanya, qui estigui interessat en col·laborar haurà d'entrar a www.projecteaina.cat i anar a l'espai corresponent. Un cop allà, haurà de destinar una estona a llegir frases que li proposarà la plataforma i podrà validar també frases d'altres persones."
datasets:
- projecte-aina/casum
---
## BART-Ca fine-tuned on the CaSum dataset for summarization

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
    - [Tokenization](#tokenization)
    - [Hyperparameters](#hyperparameters)
- [Evaluation](#evaluation)
   - [Variable and metrics](#variable-and-metrics)
   - [Evaluation results](#evaluation-results)
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

The [BART-ca](https://huggingface.co/projecte-aina/bart-base-ca) model has been fine-tuned on summarization with the [CaSum](https://huggingface.co/datasets/projecte-aina/casum) dataset that has been created along with the model. We also evaluate on an out-of-distribution dataset, [VilaSum](https://huggingface.co/datasets/projecte-aina/vilasum).

The model has been fine-tuned on news articles and is expected to work best with that type of text.

## Intended uses and limitations
You can use this model for text summarization. 

## How to use

Here is how to use this model with the [pipeline API](https://huggingface.co/transformers/main_classes/pipelines.html):

```python
from transformers import pipeline
summarizer = pipeline("summarization", model="projecte-aina/bart-base-ca-casum")
ARTICLE = """"El projecte AINA generarà els recursos digitals i lingüístics necessaris per facilitar el desenvolupament d’aplicacions basades en la intel·ligència artificial i les tecnologies de la llengua, com ara els assistents de veu, els traductors automàtics o els agents conversacionals en català. L’objectiu últim és que la ciutadania pugui participar en català en el món digital al mateix nivell que els parlants d’una llengua global, com ara l’anglès, i evitar així l’extinció digital de la llengua. El primer recurs generat és el corpus del català per entrenar els algoritmes d’intel·ligència artificial (IA), el més gran creat fins al moment, amb 1.770 milions de metadades associades a paraules. El proper pas serà generar els models de la llengua, models de la parla i models de traducció utilitzant xarxes neuronals multicapa, perquè les empreses que creen aplicacions basades en intel·ligència artificial (IA), com ara assistents de veu, traductors automàtics, agents conversacionals, etc., puguin fer-ho fàcilment en català."""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
>>> [{'summary_text': 'El projecte AINA generarà els recursos digitals i lingüístics necessaris per al desenvolupament d’aplicacions basades en la intel·ligència artificial en català’'}]
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Training data

As training data, we used the [CaSum](https://huggingface.co/datasets/projecte-aina/casum) dataset extracted from a newswire corpus crawled from the [Catalan News Agency](https://www.acn.cat/).

### Training procedure

#### Tokenization

The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2) with a vocabulary size of 51,200 tokens. 

#### Hyperparameters

The fine-tuning hyperparameters were taken from the fairseq's [Fine-tuning BART on CNN-Dailymail summarization task](https://github.com/facebookresearch/fairseq/blob/main/examples/bart/README.summarization.md) example.

## Evaluation

### Variable and metrics

We use Rouge-1 and Rouge-L for evaluation on two different test sets: the [CaSum](https://huggingface.co/datasets/projecte-aina/casum) test set and an out of distribution test set, [VilaSum](https://huggingface.co/datasets/projecte-aina/vilasum).

### Evaluation results

Below the evaluation results on the summarization task compared with the multilingual mBERT and the Catalan [NASCA](https://huggingface.co/ELiRF/NASCA) with two different testsets: [CaSum](https://huggingface.co/datasets/projecte-aina/casum) and [VilaSum](https://huggingface.co/datasets/projecte-aina/vilasum).

|Test set  | Model  | Rouge-1  |  Rouge-L  |
| ------------|:-------------:| -----:|:------|
|CaSum | BART-Ca  |  41.39  |  36.14  |
| | NASCA  |  24.42  |  19.89  |
| | mBART  |  **43.95**  |  **38.11**  |
|VilaSum  | BART-Ca  |  **35.04**  |  **29.70**  |
| | NASCA  |  23.18 |  19.09 |
| | mBART  |  33.17  |  27.52  |


## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to aina@bsc.es

### Copyright
Copyright (c) 2022 Text Mining Unit at Barcelona Supercomputing Center 

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by MT4All CEF project and the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Citation information

If you use any of these resources (datasets or models) in your work, please cite our latest preprint:

```bibtex
@misc{degibert2022sequencetosequence,
      title={Sequence-to-Sequence Resources for Catalan}, 
      author={Ona de Gibert and Ksenia Kharitonova and Blanca Calvo Figueras and Jordi Armengol-Estapé and Maite Melero},
      year={2022},
      eprint={2202.06871},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.

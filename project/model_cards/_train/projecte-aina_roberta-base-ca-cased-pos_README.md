---

language:

- ca

license: apache-2.0

tags:

- "catalan"

- "part of speech tagging"

- "pos"

- "CaText"

- "Catalan Textual Corpus"

datasets:

- "universal_dependencies"

metrics:

- f1

inference:
  parameters:
    aggregation_strategy: "first"
    
model-index:
- name: roberta-base-ca-cased-pos
  results:
  - task: 
      type: token-classification 
    dataset:
      type:   universal_dependencies
      name: Ancora-ca-POS
    metrics:
      - name: F1
        type: f1
        value: 0.9893832385244624

widget:

- text: "Em dic Lluïsa i visc a Santa Maria del Camí." 

- text: "L'Aina, la Berta i la Norma són molt amigues."

- text: "El Martí llegeix el Cavall Fort."

---

# Catalan BERTa (roberta-base-ca) finetuned for Part-of-speech-tagging (POS)

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

The **roberta-base-ca-cased-pos** is a Part-of-speech-tagging (POS) model for the Catalan language fine-tuned from the roberta-base-ca model, a [RoBERTa](https://arxiv.org/abs/1907.11692) base model pre-trained on a medium-size corpus collected from publicly available corpora and crawlers.

## Intended uses and limitations

**roberta-base-ca-cased-pos** model can be used to Part-of-speech-tagging (POS) a text. The model is limited by its training dataset and may not generalize well for all use cases.

## How to use

Here is how to use this model:

```python
from transformers import pipeline
from pprint import pprint

nlp = pipeline("token-classification", model="projecte-aina/roberta-base-ca-cased-pos")
example = "Em dic Lluïsa i visc a Santa Maria del Camí."

pos_results = nlp(example)
pprint(pos_results)
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Training data
We used the POS dataset in Catalan from the [Universal Dependencies Treebank](https://huggingface.co/datasets/universal_dependencies) we refer to _Ancora-ca-pos_ for training and evaluation.

### Training procedure
The model was trained with a batch size of 16 and a learning rate of 5e-5 for 5 epochs. We then selected the best checkpoint using the downstream task metric in the corresponding development set and then evaluated it on the test set.

## Evaluation

### Variable and metrics

This model was finetuned maximizing F1 score.

## Evaluation results
We evaluated the _roberta-base-ca-cased-pos_ on the Ancora-ca-ner test set against standard multilingual and monolingual baselines:


| Model        | AnCora-Ca-POS (F1)   | 
| ------------|:-------------|
| roberta-base-ca-cased-pos |**98.93** |
| mBERT       | 98.82 |
| XLM-RoBERTa | 98.89 | 
| WikiBERT-ca | 97.60 | 

For more details, check the fine-tuning and evaluation scripts in the official [GitHub repository](https://github.com/projecte-aina/club).

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
This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Citation Information  
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


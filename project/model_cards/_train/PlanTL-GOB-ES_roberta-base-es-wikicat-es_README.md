---

language:

- es

license: apache-2.0

tags:

- "español"

- "text classification"

- "WikiCAT_esv2"
datasets:
- "projecte-aina/WikiCAT_esv2"

metrics:

- f1-macro

model-index:
- name: roberta-base-es-wikicat-es
  results:
  - task: 
      type: text-classification 
    dataset:
      type: projecte-aina/WikiCAT_esv2
      name: WikiCAT_esv2
    metrics:
      - name: F1-macro
        type: f1
        value: 0.76632
      - name: Accuracy
        type: accuracy
        value: 0.79347
        
widget:
- text: "Sedna es el cuerpo menor del sistema solar número 90377; concretamente es un objeto transneptuniano."
- text: "El Fútbol Club Barcelona, conocido popularmente como Barça, es una entidad polideportiva con sede en Barcelona, España."

---

# Spanish BERTa-v2 (roberta-base-es) finetuned for Text Classification.

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-uses-and-limitations)
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
  - [Disclaimer](#disclaimer)
  
</details>

## Model description

The **roberta-base-es-wikicat-es** is a Text Classification model for the Catalan language fine-tuned from the [roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) model, a [RoBERTa](https://arxiv.org/abs/1907.11692) base model pre-trained on a medium-size corpus collected from publicly available corpora and crawlers (check the roberta-base-bne model card for more details).

## Intended uses and limitations

**roberta-base-es-wikicat-es** model can be used to classify texts. The model is limited by its training dataset and may not generalize well for all use cases.

## How to use

Here is how to use this model:

```python
from transformers import pipeline
from pprint import pprint
nlp = pipeline("text-classification", model="roberta-base-es-wikicat-es")
example = "Sedna es el cuerpo menor del sistema solar número 90377; concretamente es un objeto transneptuniano."
tc_results = nlp(example)
pprint(tc_results)
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Training data
We used the TC dataset in Spanish called [WikiCAT_esv2](https://huggingface.co/datasets/PlanTL-GOB-ES/WikiCAT_esv2) for training and evaluation.

### Training procedure
The model was trained with a batch size of 16 and three learning rates (1e-5, 3e-5, 5e-5) for 5 epochs. We then selected the best learning rate (2e-5) and checkpoint (epoch 3) using the downstream task metric in the corresponding development set.

## Evaluation

### Variable and metrics

This model was finetuned maximizing F1 (macro) score.

### Evaluation results
We evaluated the _roberta-base-es-wikicat-es_ on the WikiCAT_esv2 dev set:
| Model        | WikiCAT_ca (F1)| 
| ------------|:-------------|
| rroberta-base-es-wikicat-es | 0.76632 |

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


## Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


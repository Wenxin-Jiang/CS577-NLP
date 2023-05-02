---
language: nl
license: mit
pipeline_tag: text-classification
inference: false
---

# A-PROOF ICF-domains Classification

## Description

A fine-tuned multi-label classification model that detects 9 [WHO-ICF](https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health) domains in clinical text in Dutch. The model is based on a pre-trained Dutch medical language model ([link to be added]()), a RoBERTa model, trained from scratch on clinical notes of the Amsterdam UMC.

## ICF domains
The model can detect 9 domains, which were chosen due to their relevance to recovery from COVID-19:

ICF code | Domain | name in repo
---|---|---
b440 | Respiration functions | ADM
b140 | Attention functions | ATT
d840-d859 | Work and employment | BER
b1300 | Energy level | ENR
d550 | Eating | ETN
d450 | Walking | FAC
b455 | Exercise tolerance functions | INS
b530 | Weight maintenance functions | MBW
b152 | Emotional functions | STM

## Intended uses and limitations
- The model was fine-tuned (trained, validated and tested) on medical records from the Amsterdam UMC (the two academic medical centers of Amsterdam). It might perform differently on text from a different hospital or text from non-hospital sources (e.g. GP records).
- The model was fine-tuned with the [Simple Transformers](https://simpletransformers.ai/) library. This library is based on Transformers but the model cannot be used directly with Transformers `pipeline` and classes; doing so would generate incorrect outputs. For this reason, the API on this page is disabled.

## How to use
To generate predictions with the model, use the [Simple Transformers](https://simpletransformers.ai/) library:
```
from simpletransformers.classification import MultiLabelClassificationModel

model = MultiLabelClassificationModel(
    'roberta',
    'CLTL/icf-domains',
    use_cuda=False,
)

example = 'Nu sinds 5-6 dagen progressieve benauwdheidsklachten (bij korte stukken lopen al kortademig), terwijl dit eerder niet zo was.'
predictions, raw_outputs = model.predict([example])
```
The predictions look like this:
```
[[1, 0, 0, 0, 0, 1, 1, 0, 0]]
```
The indices of the multi-label stand for:
```
[ADM, ATT, BER, ENR, ETN, FAC, INS, MBW, STM]
```
In other words, the above prediction corresponds to assigning the labels ADM, FAC and INS to the example sentence.

The raw outputs look like this:
```
[[0.51907885 0.00268032 0.0030862  0.03066113 0.00616694 0.64720929
  0.67348498 0.0118863  0.0046311 ]]
```
For this model, the threshold at which the prediction for a label flips from 0 to 1 is **0.5**.

## Training data
- The training data consists of clinical notes from medical records (in Dutch) of the Amsterdam UMC. Due to privacy constraints, the data cannot be released.
- The annotation guidelines used for the project can be found [here](https://github.com/cltl/a-proof-zonmw/tree/main/resources/annotation_guidelines).

## Training procedure
The default training parameters of Simple Transformers were used, including:
- Optimizer: AdamW
- Learning rate: 4e-5
- Num train epochs: 1
- Train batch size: 8
- Threshold: 0.5

## Evaluation results
The evaluation is done on a sentence-level (the classification unit) and on a note-level (the aggregated unit which is meaningful for the healthcare professionals).

### Sentence-level
| | ADM | ATT | BER | ENR | ETN | FAC | INS | MBW | STM
|---|---|---|---|---|---|---|---|---|---
precision | 0.98 | 0.98 | 0.56 | 0.96 | 0.92 | 0.84 | 0.89 | 0.79 | 0.70
recall | 0.49 | 0.41 | 0.29 | 0.57 | 0.49 | 0.71 | 0.26 | 0.62 | 0.75
F1-score | 0.66 | 0.58 | 0.35 | 0.72 | 0.63 | 0.76 | 0.41 | 0.70 | 0.72
support | 775 | 39 | 54 | 160 | 382 | 253 | 287 | 125 | 181

### Note-level
| | ADM | ATT | BER | ENR | ETN | FAC | INS | MBW | STM
|---|---|---|---|---|---|---|---|---|---
precision | 1.0 | 1.0 | 0.66 | 0.96 | 0.95 | 0.84 | 0.95 | 0.87 | 0.80
recall | 0.89 | 0.56 | 0.44 | 0.70 | 0.72 | 0.89 | 0.46 | 0.87 | 0.87
F1-score | 0.94 | 0.71 | 0.50 | 0.81 | 0.82 | 0.86 | 0.61 | 0.87 | 0.84
support | 231 | 27 | 34 | 92 | 165 | 95 | 116 | 64 | 94

## Authors and references
### Authors
Jenia Kim, Piek Vossen

### References
TBD
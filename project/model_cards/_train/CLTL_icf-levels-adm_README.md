---
language: nl
license: mit
pipeline_tag: text-classification
inference: false
---

# Regression Model for Respiration Functioning Levels (ICF b440)

## Description
A fine-tuned regression model that assigns a functioning level to Dutch sentences describing respiration functions. The model is based on a pre-trained Dutch medical language model ([link to be added]()): a RoBERTa model, trained from scratch on clinical notes of the Amsterdam UMC. To detect sentences about respiration functions in clinical text in Dutch, use the [icf-domains](https://huggingface.co/CLTL/icf-domains) classification model.

## Functioning levels
Level | Meaning
---|---
4 | No problem with respiration, and/or respiratory rate is normal (EWS: 9-20).
3 | Shortness of breath in exercise (saturation &ge;90), and/or respiratory rate is slightly increased (EWS: 21-30).
2 | Shortness of breath in rest (saturation &ge;90), and/or respiratory rate is fairly increased (EWS: 31-35).
1 | Needs oxygen at rest or during exercise (saturation &lt;90), and/or respiratory rate &gt;35.
0 | Mechanical ventilation is needed.

The predictions generated by the model might sometimes be outside of the scale (e.g. 4.2); this is normal in a regression model.

## Intended uses and limitations
- The model was fine-tuned (trained, validated and tested) on medical records from the Amsterdam UMC (the two academic medical centers of Amsterdam). It might perform differently on text from a different hospital or text from non-hospital sources (e.g. GP records).
- The model was fine-tuned with the [Simple Transformers](https://simpletransformers.ai/) library. This library is based on Transformers but the model cannot be used directly with Transformers `pipeline` and classes; doing so would generate incorrect outputs. For this reason, the API on this page is disabled.

## How to use
To generate predictions with the model, use the [Simple Transformers](https://simpletransformers.ai/) library:
```
from simpletransformers.classification import ClassificationModel

model = ClassificationModel(
    'roberta',
    'CLTL/icf-levels-adm',
    use_cuda=False,
)

example = 'Nu sinds 5-6 dagen progressieve benauwdheidsklachten (bij korte stukken lopen al kortademig), terwijl dit eerder niet zo was.'
_, raw_outputs = model.predict([example])
predictions = np.squeeze(raw_outputs)
```
The prediction on the example is:
```
2.26
```
The raw outputs look like this:
```
[[2.26074648]]
```

## Training data
- The training data consists of clinical notes from medical records (in Dutch) of the Amsterdam UMC. Due to privacy constraints, the data cannot be released.
- The annotation guidelines used for the project can be found [here](https://github.com/cltl/a-proof-zonmw/tree/main/resources/annotation_guidelines).

## Training procedure
The default training parameters of Simple Transformers were used, including:
- Optimizer: AdamW
- Learning rate: 4e-5
- Num train epochs: 1
- Train batch size: 8

## Evaluation results
The evaluation is done on a sentence-level (the classification unit) and on a note-level (the aggregated unit which is meaningful for the healthcare professionals).

| | Sentence-level | Note-level
|---|---|---
mean absolute error | 0.48 | 0.37
mean squared error | 0.55 | 0.34
root mean squared error | 0.74 | 0.58

## Authors and references
### Authors
Jenia Kim, Piek Vossen

### References
TBD

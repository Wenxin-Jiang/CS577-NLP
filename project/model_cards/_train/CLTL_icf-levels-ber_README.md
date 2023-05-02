---
language: nl
license: mit
pipeline_tag: text-classification
inference: false
---

# Regression Model for Work and Employment Functioning Levels (ICF d840-d859)

## Description
A fine-tuned regression model that assigns a functioning level to Dutch sentences describing work and employment functions. The model is based on a pre-trained Dutch medical language model ([link to be added]()): a RoBERTa model, trained from scratch on clinical notes of the Amsterdam UMC. To detect sentences about work and employment functions in clinical text in Dutch, use the [icf-domains](https://huggingface.co/CLTL/icf-domains) classification model.

## Functioning levels
Level | Meaning
---|---
4 | Can work/study fully (like when healthy).
3 | Can work/study almost fully.
2 | Can work/study only for about 50\%, or can only work at home and cannot go to school / office.
1 | Work/study is severely limited.
0 | Cannot work/study.

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
    'CLTL/icf-levels-ber',
    use_cuda=False,
)

example = 'Fysiek zwaar werk is niet mogelijk, maar administrative taken zou zij wel aan moeten kunnen.'
_, raw_outputs = model.predict([example])
predictions = np.squeeze(raw_outputs)
```
The prediction on the example is:
```
2.41
```
The raw outputs look like this:
```
[[2.40793037]]
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
mean absolute error | 1.56 | 1.49
mean squared error | 3.06 | 2.85
root mean squared error | 1.75 | 1.69

## Authors and references
### Authors
Jenia Kim, Piek Vossen

### References
TBD
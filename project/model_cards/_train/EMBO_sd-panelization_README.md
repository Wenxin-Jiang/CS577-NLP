---
language: 
- english
thumbnail: 
tags:
- token classification
- 
license: agpl-3.0
datasets:
- EMBO/sd-nlp
metrics:
-
---

# sd-panelization

## Model description

This model is a [RoBERTa base model](https://huggingface.co/roberta-base) that was further trained using a masked language modeling task on a compendium of english scientific textual examples from the life sciences using the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang). It was then fine-tuned for token classification on the SourceData [sd-nlp](https://huggingface.co/datasets/EMBO/sd-nlp) dataset with the `PANELIZATION` task to perform 'parsing' or 'segmentation' of figure legends into fragments corresponding to sub-panels.

Figures are usually composite representations of results obtained with heterogeneous experimental approaches and systems. Breaking figures into panels allows identifying more coherent descriptions of individual scientific experiments.

## Intended uses & limitations

#### How to use

The intended use of this model is for 'parsing' figure legends into sub-fragments corresponding to individual panels as used in SourceData annotations (https://sourcedata.embo.org). 

To have a quick check of the model:

```python
from transformers import pipeline, RobertaTokenizerFast, RobertaForTokenClassification
example = """Fig 4. a, Volume density of early (Avi) and late (Avd) autophagic vacuoles.a, Volume density of early (Avi) and late (Avd) autophagic vacuoles from four independent cultures. Examples of Avi and Avd are shown in b and c, respectively. Bars represent 0.4����m. d, Labelling density of cathepsin-D as estimated in two independent experiments. e, Labelling density of LAMP-1."""
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_len=512)
model = RobertaForTokenClassification.from_pretrained('EMBO/sd-panelization')
ner = pipeline('ner', model, tokenizer=tokenizer)
res = ner(example)
for r in res: print(r['word'], r['entity'])
```

#### Limitations and bias

The model must be used with the `roberta-base` tokenizer.

## Training data

The model was trained for token classification using the [`EMBO/sd-nlp PANELIZATION`](https://huggingface.co/datasets/EMBO/sd-nlp) dataset which includes manually annotated examples.

## Training procedure

The training was run on an NVIDIA DGX Station with 4XTesla V100 GPUs.

Training code is available at https://github.com/source-data/soda-roberta

- Model fine-tuned: EMBO/bio-lm
- Tokenizer vocab size: 50265
- Training data: EMBO/sd-nlp
- Dataset configuration: PANELIZATION
- TTraining with 2175 examples.                                  
- Evaluating on 622 examples. 
- Training on 2 features: `O`, `B-PANEL_START`
- Epochs: 1.3
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `learning_rate`: 0.0001
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0

## Eval results

Testing on 1802 examples from test set with `sklearn.metrics`:

```                                                                             
              precision    recall  f1-score   support

 PANEL_START       0.89      0.95      0.92      5427

   micro avg       0.89      0.95      0.92      5427
   macro avg       0.89      0.95      0.92      5427
weighted avg       0.89      0.95      0.92      5427
```

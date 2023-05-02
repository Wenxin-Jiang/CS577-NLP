---
language: 
- english
thumbnail: 
tags:
- token classification
license: agpl-3.0
datasets:
- EMBO/sd-nlp
metrics:
-
---

# sd-ner

## Model description

This model is a [RoBERTa base model](https://huggingface.co/roberta-base) that was further trained using a masked language modeling task on a compendium of English scientific textual examples from the life sciences using the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang). It was then fine-tuned for token classification on the SourceData [sd-nlp](https://huggingface.co/datasets/EMBO/sd-nlp) dataset with the `NER` configuration to perform Named Entity Recognition of bioentities. 


## Intended uses & limitations

#### How to use

The intended use of this model is for Named Entity Recognition of biological entities used in SourceData annotations (https://sourcedata.embo.org), including small molecules, gene products (genes and proteins), subcellular components, cell line and cell types, organ and tissues, species as well as experimental methods.

To have a quick check of the model:

```python
from transformers import pipeline, RobertaTokenizerFast, RobertaForTokenClassification
example = """<s> F. Western blot of input and eluates of Upf1 domains purification in a Nmd4-HA strain. The band with the # might corresponds to a dimer of Upf1-CH, bands marked with a star correspond to residual signal with the anti-HA antibodies (Nmd4). Fragments in the eluate have a smaller size because the protein A part of the tag was removed by digestion with the TEV protease. G6PDH served as a loading control in the input samples </s>"""
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_len=512)
model = RobertaForTokenClassification.from_pretrained('EMBO/sd-ner')
ner = pipeline('ner', model, tokenizer=tokenizer)
res = ner(example)
for r in res:
    print(r['word'], r['entity'])
```

#### Limitations and bias

The model must be used with the `roberta-base` tokenizer.

## Training data

The model was trained for token classification using the [EMBO/sd-nlp dataset](https://huggingface.co/datasets/EMBO/sd-nlp) dataset which includes manually annotated examples.

## Training procedure

The training was run on an NVIDIA DGX Station with 4XTesla V100 GPUs.

Training code is available at https://github.com/source-data/soda-roberta

- Model fine-tuned: EMBO/bio-lm
- Tokenizer vocab size: 50265
- Training data: EMBO/sd-nlp
- Dataset configuration: NER
- Training with 48771 examples.
- Evaluating on 13801 examples.
- Training on 15 features: O, I-SMALL_MOLECULE, B-SMALL_MOLECULE, I-GENEPROD, B-GENEPROD, I-SUBCELLULAR, B-SUBCELLULAR, I-CELL, B-CELL, I-TISSUE, B-TISSUE, I-ORGANISM, B-ORGANISM, I-EXP_ASSAY, B-EXP_ASSAY
- Epochs: 0.6
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `learning_rate`: 0.0001
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0

## Eval results

Testing on 7178 examples of test set with `sklearn.metrics`:

```
                precision    recall  f1-score   support

          CELL       0.69      0.81      0.74      5245
     EXP_ASSAY       0.56      0.57      0.56     10067
      GENEPROD       0.77      0.89      0.82     23587
      ORGANISM       0.72      0.82      0.77      3623
SMALL_MOLECULE       0.70      0.80      0.75      6187
   SUBCELLULAR       0.65      0.72      0.69      3700
        TISSUE       0.62      0.73      0.67      3207

     micro avg       0.70      0.79      0.74     55616
     macro avg       0.67      0.77      0.72     55616
  weighted avg       0.70      0.79      0.74     55616

{'test_loss': 0.1830928772687912, 'test_accuracy_score': 0.9334821000160841, 'test_precision': 0.6987463009514112, 'test_recall': 0.789682825086306, 'test_f1': 0.7414366506288511, 'test_runtime': 61.0547, 'test_samples_per_second': 117.567, 'test_steps_per_second': 1.851}
```

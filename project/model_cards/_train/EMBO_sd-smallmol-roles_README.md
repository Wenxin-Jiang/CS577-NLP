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

# sd-smallmol-roles

## Model description

This model is a [RoBERTa base model](https://huggingface.co/roberta-base) that was further trained using a masked language modeling task on a compendium of english scientific textual examples from the life sciences using the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang). It has then been fine-tuned for token classification on the SourceData [sd-nlp](https://huggingface.co/datasets/EMBO/sd-nlp) dataset with the `SMALL_MOL_ROLES` configuration to perform pure context-dependent semantic role classification of bioentities.


## Intended uses & limitations

#### How to use

The intended use of this model is to infer the semantic role of small molecules with regard to the causal hypotheses tested in experiments reported in scientific papers. 

To have a quick check of the model:

```python
from transformers import pipeline, RobertaTokenizerFast, RobertaForTokenClassification
example = """<s>The <mask> overexpression in cells caused an increase in <mask> expression.</s>"""
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_len=512)
model = RobertaForTokenClassification.from_pretrained('EMBO/sd-smallmol-roles')
ner = pipeline('ner', model, tokenizer=tokenizer)
res = ner(example)
for r in res:
    print(r['word'], r['entity'])
```

#### Limitations and bias

The model must be used with the `roberta-base` tokenizer.

## Training data

The model was trained for token classification using the [EMBO/sd-nlp dataset](https://huggingface.co/datasets/EMBO/sd-nlp) which includes manually annotated examples.

## Training procedure

The training was run on a NVIDIA DGX Station with 4XTesla V100 GPUs.

Training code is available at https://github.com/source-data/soda-roberta

- Model fine tuned: EMBL/bio-lm
- Tokenizer vocab size: 50265
- Training data: EMBO/sd-nlp
- Dataset configuration: SMALL_MOL_ROLES
- Training with 48771 examples.
- Evaluating on 13801 examples.
- Training on 15 features: O, I-CONTROLLED_VAR, B-CONTROLLED_VAR, I-MEASURED_VAR, B-MEASURED_VAR
- Epochs: 0.33
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `learning_rate`: 0.0001
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0

## Eval results

On 7178 example of test set with `sklearn.metrics`:

```                                                                                                                                                           
                precision    recall  f1-score   support

CONTROLLED_VAR       0.76      0.90      0.83      2946
  MEASURED_VAR       0.60      0.71      0.65       852

     micro avg       0.73      0.86      0.79      3798
     macro avg       0.68      0.80      0.74      3798
  weighted avg       0.73      0.86      0.79      3798

{'test_loss': 0.011743436567485332, 'test_accuracy_score': 0.9951612532624371, 'test_precision': 0.7261345852895149, 'test_recall': 0.8551869404949973, 'test_f1': 0.7853947527505744, 'test_runtime': 58.0378, 'test_samples_per_second': 123.678, 'test_steps_per_second': 1.947}
```

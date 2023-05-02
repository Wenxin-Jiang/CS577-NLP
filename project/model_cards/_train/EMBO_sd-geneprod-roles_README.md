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

# sd-geneprod-roles

## Model description

This model is a [RoBERTa base model](https://huggingface.co/roberta-base) that was further trained using a masked language modeling task on a compendium of English scientific textual examples from the life sciences using the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang). It was then fine-tuned for token classification on the SourceData [sd-nlp](https://huggingface.co/datasets/EMBO/sd-nlp) dataset with the `GENEPROD_ROLES` configuration to perform pure context-dependent semantic role classification of bioentities.


## Intended uses & limitations

#### How to use

The intended use of this model is to infer the semantic role of gene products (genes and proteins) with regard to the causal hypotheses tested in experiments reported in scientific papers. 

To have a quick check of the model:

```python
from transformers import pipeline, RobertaTokenizerFast, RobertaForTokenClassification
example = """<s>The <mask> overexpression in cells caused an increase in <mask> expression.</s>"""
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_len=512)
model = RobertaForTokenClassification.from_pretrained('EMBO/sd-geneprod-roles')
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

The training was run on an NVIDIA DGX Station with 4XTesla V100 GPUs.

Training code is available at https://github.com/source-data/soda-roberta

- Model fine-tuned: EMBL/bio-lm
- Tokenizer vocab size: 50265
- Training data: EMBO/sd-nlp
- Dataset configuration: GENEPROD_ROLES
- Training with 48771 examples.
- Evaluating on 13801 examples.
- Training on 15 features: O, I-CONTROLLED_VAR, B-CONTROLLED_VAR, I-MEASURED_VAR, B-MEASURED_VAR
- Epochs: 0.9
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

CONTROLLED_VAR       0.81      0.86      0.83      7835
  MEASURED_VAR       0.82      0.85      0.84      9330

     micro avg       0.82      0.85      0.83     17165
     macro avg       0.82      0.85      0.83     17165
  weighted avg       0.82      0.85      0.83     17165
  
{'test_loss': 0.03846803680062294, 'test_accuracy_score': 0.9854472664459946, 'test_precision': 0.8156312625250501, 'test_recall': 0.8535974366443344, 'test_f1': 0.8341825841897008, 'test_runtime': 58.7369, 'test_samples_per_second': 122.206, 'test_steps_per_second': 1.924}
```

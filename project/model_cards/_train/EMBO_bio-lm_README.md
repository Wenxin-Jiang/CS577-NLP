---
language: 
- english
thumbnail: 
tags:
- language model
license: 
datasets:
- EMBO/biolang
metrics:
-
---

# bio-lm

## Model description

This model is a [RoBERTa base pre-trained model](https://huggingface.co/roberta-base) that was further trained using a masked language modeling task on a compendium of english scientific textual examples from the life sciences using the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang).

## Intended uses & limitations

#### How to use

The intended use of this model is to be fine-tuned for downstream tasks, token classification in particular.

To have a quick check of the model as-is in a fill-mask task:

```python
from transformers import pipeline, RobertaTokenizerFast
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_len=512)
text = "Let us try this model to see if it <mask>."
fill_mask = pipeline(
    "fill-mask",
    model='EMBO/bio-lm',
    tokenizer=tokenizer
)
fill_mask(text)
```

#### Limitations and bias

This model should be fine-tuned on a specifi task like token classification.
The model must be used with the `roberta-base` tokenizer.

## Training data

The model was trained with a masked language modeling taskon the [BioLang dataset](https://huggingface.co/datasets/EMBO/biolang) wich includes 12Mio examples from abstracts and figure legends extracted from papers published in life sciences.

## Training procedure

The training was run on a NVIDIA DGX Station with 4XTesla V100 GPUs.

Training code is available at https://github.com/source-data/soda-roberta

- Command: `python -m lm.train /data/json/oapmc_abstracts_figs/ MLM`
- Tokenizer vocab size: 50265
- Training data: EMBO/biolang MLM
- Training with: 12005390 examples
- Evaluating on: 36713 examples
- Epochs: 3.0
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- tensorboard run: lm-MLM-2021-01-27T15-17-43.113766

End of training:
```
trainset: 'loss': 0.8653350830078125
validation set: 'eval_loss': 0.8192330598831177, 'eval_recall': 0.8154601116513597
```

## Eval results

Eval on test set:
```
recall: 0.814471959728645
```

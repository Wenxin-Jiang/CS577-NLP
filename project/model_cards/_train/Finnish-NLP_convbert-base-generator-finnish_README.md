---
language:
- fi
license: apache-2.0
tags:
- finnish
- convbert
datasets:
- Finnish-NLP/mc4_fi_cleaned
- wikipedia
widget:
- text: "Moikka olen [MASK] kielimalli."

---

# ConvBERT for Finnish

Pretrained ConvBERT model on Finnish language using a replaced token detection (RTD) objective. ConvBERT was introduced in
[this paper](https://arxiv.org/abs/2008.02496)
and first released at [this page](https://github.com/yitu-opensource/ConvBert).

**Note**: this model is the ConvBERT generator model intented to be used for the fill-mask task. The ConvBERT discriminator model intented to be used for fine-tuning on downstream tasks like text classification is released here [Finnish-NLP/convbert-base-finnish](https://huggingface.co/Finnish-NLP/convbert-base-finnish)

## Model description

Finnish ConvBERT is a transformers model pretrained on a very large corpus of Finnish data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts.

More precisely, it was pretrained with the replaced token detection (RTD) objective. Instead of masking the input like in BERT's masked language modeling (MLM) objective, this approach corrupts the input by replacing some tokens with plausible alternatives sampled from a small generator model. Then, instead of training a model that predicts the original identities of the corrupted tokens, a discriminative model is trained that predicts whether each token in the corrupted input was replaced by a generator model's sample or not. Thus, this training approach resembles Generative Adversarial Nets (GAN).

This way, the model learns an inner representation of the Finnish language that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled sentences for instance, you can train a standard classifier using the features produced by the ConvBERT model as inputs.

Compared to BERT and ELECTRA models, ConvBERT model utilizes a span-based
dynamic convolution to replace some of the global self-attention heads for modeling local input sequence
dependencies. These convolution heads, together with the rest of the self-attention
heads, form a new mixed attention block that should be more efficient at both global
and local context learning.

## Intended uses & limitations

You can use this generator model mainly just for the fill-mask task. For other tasks, check the [Finnish-NLP/convbert-base-finnish](https://huggingface.co/Finnish-NLP/convbert-base-finnish) model instead.

### How to use

Here is how to use this model directly with a pipeline for fill-mask task:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Finnish-NLP/convbert-base-generator-finnish')
>>> unmasker("Moikka olen [MASK] kielimalli.")
[{'score': 0.08341152966022491,
  'token': 4619,
  'token_str': 'suomalainen',
  'sequence': 'Moikka olen suomalainen kielimalli.'},
 {'score': 0.02831297740340233,
  'token': 25583,
  'token_str': 'ranskalainen',
  'sequence': 'Moikka olen ranskalainen kielimalli.'},
 {'score': 0.027857203036546707,
  'token': 37714,
  'token_str': 'kiinalainen',
  'sequence': 'Moikka olen kiinalainen kielimalli.'},
 {'score': 0.027701903134584427,
  'token': 21614,
  'token_str': 'ruotsalainen',
  'sequence': 'Moikka olen ruotsalainen kielimalli.'},
 {'score': 0.026388710364699364,
  'token': 591,
  'token_str': 'hyvä',
  'sequence': 'Moikka olen hyvä kielimalli.'}]
```

### Limitations and bias

The training data used for this model contains a lot of unfiltered content from the internet, which is far from neutral. Therefore, the model can have biased predictions. This bias will also affect all fine-tuned versions of this model.

## Training data

This Finnish ConvBERT model was pretrained on the combination of five datasets:
- [mc4_fi_cleaned](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned), the dataset mC4 is a multilingual colossal, cleaned version of Common Crawl's web crawl corpus. We used the Finnish subset of the mC4 dataset and further cleaned it with our own text data cleaning codes (check the dataset repo).
- [wikipedia](https://huggingface.co/datasets/wikipedia) We used the Finnish subset of the wikipedia (August 2021) dataset
- [Yle Finnish News Archive 2011-2018](http://urn.fi/urn:nbn:fi:lb-2017070501)
- [Finnish News Agency Archive (STT)](http://urn.fi/urn:nbn:fi:lb-2018121001)
- [The Suomi24 Sentences Corpus](http://urn.fi/urn:nbn:fi:lb-2020021803)

Raw datasets were cleaned to filter out bad quality and non-Finnish examples. Together these cleaned datasets were around 84GB of text.

## Training procedure

### Preprocessing

The texts are tokenized using WordPiece and a vocabulary size of 50265. The inputs are sequences of 512 consecutive tokens. Texts are not lower cased so this model is case-sensitive: it makes a difference between finnish and Finnish.

### Pretraining

The model was trained on TPUv3-8 VM, sponsored by the [Google TPU Research Cloud](https://sites.research.google/trc/about/), for 1M steps. The optimizer used was a AdamW with learning rate 1e-4, learning rate warmup for 20000 steps and linear decay of the learning rate after.

Training code was from the official [ConvBERT repository](https://github.com/yitu-opensource/ConvBert) and also some instructions was used from [here](https://github.com/stefan-it/turkish-bert/blob/master/convbert/CHEATSHEET.md).

## Evaluation results

For evaluation results, check the [Finnish-NLP/convbert-base-finnish](https://huggingface.co/Finnish-NLP/convbert-base-finnish) model repository instead.

## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗
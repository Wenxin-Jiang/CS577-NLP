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

---

# ConvBERT for Finnish

Pretrained ConvBERT model on Finnish language using a replaced token detection (RTD) objective. ConvBERT was introduced in
[this paper](https://arxiv.org/abs/2008.02496)
and first released at [this page](https://github.com/yitu-opensource/ConvBert).

**Note**: this model is the ConvBERT discriminator model intented to be used for fine-tuning on downstream tasks like text classification. The ConvBERT generator model intented to be used for fill-mask task is released here [Finnish-NLP/convbert-base-generator-finnish](https://huggingface.co/Finnish-NLP/convbert-base-generator-finnish)

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

You can use the raw model for extracting features or fine-tune it to a downstream task like text classification.

### How to use

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import ConvBertTokenizer, ConvBertModel
import torch

tokenizer = ConvBertTokenizer.from_pretrained("Finnish-NLP/convbert-base-finnish")
model = ConvBertModel.from_pretrained("Finnish-NLP/convbert-base-finnish")

inputs = tokenizer("Joka kuuseen kurkottaa, se katajaan kapsahtaa", return_tensors="pt")
outputs = model(**inputs)
print(outputs.last_hidden_state)
```

and in TensorFlow:

```python
from transformers import ConvBertTokenizer, TFConvBertModel

tokenizer = ConvBertTokenizer.from_pretrained("Finnish-NLP/convbert-base-finnish")
model = TFConvBertModel.from_pretrained("Finnish-NLP/convbert-base-finnish")

inputs = tokenizer("Joka kuuseen kurkottaa, se katajaan kapsahtaa", return_tensors="tf")
outputs = model(inputs)
print(outputs.last_hidden_state)
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

Evaluation was done by fine-tuning the model on downstream text classification task with two different labeled datasets: [Yle News](https://github.com/spyysalo/yle-corpus) and [Eduskunta](https://github.com/aajanki/eduskunta-vkk). Yle News classification fine-tuning was done with two different sequence lengths: 128 and 512 but Eduskunta only with 128 sequence length.
When fine-tuned on those datasets, this model (the first row of the table) achieves the following accuracy results compared to the [FinBERT (Finnish BERT)](https://huggingface.co/TurkuNLP/bert-base-finnish-cased-v1) model and to our other models:

|                                               | Average  | Yle News 128 length | Yle News 512 length | Eduskunta 128 length |
|-----------------------------------------------|----------|---------------------|---------------------|----------------------|
|Finnish-NLP/convbert-base-finnish              |86.98     |94.04                |95.02                |71.87                 |
|Finnish-NLP/electra-base-discriminator-finnish |86.25     |93.78                |94.77                |70.20                 |
|Finnish-NLP/roberta-large-wechsel-finnish      |88.19     |**94.91**            |95.18                |74.47                 |
|Finnish-NLP/roberta-large-finnish-v2           |88.17     |94.46                |95.22                |74.83                 |
|Finnish-NLP/roberta-large-finnish              |88.02     |94.53                |95.23                |74.30                 |
|TurkuNLP/bert-base-finnish-cased-v1            |**88.82** |94.90                |**95.49**            |**76.07**             |

To conclude, this ConvBERT model wins the ELECTRA model while losing to other models but is still fairly competitive compared to our roberta-large models when taking into account that this ConvBERT model has 106M parameters when roberta-large models have 355M parameters. ConvBERT winning the ELECTRA is also in line with the findings of the [ConvBERT paper](https://arxiv.org/abs/2008.02496).

## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗
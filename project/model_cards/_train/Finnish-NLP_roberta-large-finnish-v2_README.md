---
language:
- fi
license: apache-2.0
tags:
- finnish
- roberta
datasets:
- Finnish-NLP/mc4_fi_cleaned
- wikipedia
widget:
- text: "Moikka olen <mask> kielimalli."

---

# RoBERTa large model for Finnish

This **Finnish-NLP/roberta-large-finnish-v2** model is a new version of the previously trained [Finnish-NLP/roberta-large-finnish](https://huggingface.co/Finnish-NLP/roberta-large-finnish) model. Training hyperparameters were same but the training dataset was cleaned better with the goal to get better performing language model through the better cleaned data. Based on the model evaluations (check the table at the end), slightly better cleaned data didn't seem to produce better performing model. 

Pretrained RoBERTa model on Finnish language using a masked language modeling (MLM) objective. RoBERTa was introduced in
[this paper](https://arxiv.org/abs/1907.11692) and first released in
[this repository](https://github.com/pytorch/fairseq/tree/master/examples/roberta). This model is case-sensitive: it
makes a difference between finnish and Finnish.

## Model description

Finnish RoBERTa is a transformers model pretrained on a large corpus of Finnish data in a self-supervised fashion. This means
it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of
publicly available data) with an automatic process to generate inputs and labels from those texts. 

More precisely, it was pretrained with the Masked language modeling (MLM) objective. Taking a sentence, the model
randomly masks 15% of the words in the input then run the entire masked sentence through the model and has to predict
the masked words. This is different from traditional recurrent neural networks (RNNs) that usually see the words one
after the other, or from autoregressive models like GPT which internally mask the future tokens. It allows the model to
learn a bidirectional representation of the sentence.

This way, the model learns an inner representation of the Finnish language that can then be used to extract features
useful for downstream tasks: if you have a dataset of labeled sentences for instance, you can train a standard
classifier using the features produced by the RoBERTa model as inputs.

## Intended uses & limitations

You can use the raw model for masked language modeling, but it's mostly intended to be fine-tuned on a downstream task.

Note that this model is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked)
to make decisions, such as sequence classification, token classification or question answering. For tasks such as text
generation you should look at model like GPT2.

### How to use

You can use this model directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Finnish-NLP/roberta-large-finnish-v2')
>>> unmasker("Moikka olen <mask> kielimalli.")

[{'score': 0.04741518571972847,
  'token': 763,
  'token_str': ' hyvä',
  'sequence': 'Moikka olen hyvä kielimalli.'},
 {'score': 0.036977022886276245,
  'token': 505,
  'token_str': ' myös',
  'sequence': 'Moikka olen myös kielimalli.'},
 {'score': 0.025283709168434143,
  'token': 3089,
  'token_str': ' huono',
  'sequence': 'Moikka olen huono kielimalli.'},
 {'score': 0.022848006337881088,
  'token': 1852,
  'token_str': ' toinen',
  'sequence': 'Moikka olen toinen kielimalli.'},
 {'score': 0.019232941791415215,
  'token': 1029,
  'token_str': ' siis',
  'sequence': 'Moikka olen siis kielimalli.'}]
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import RobertaTokenizer, RobertaModel
tokenizer = RobertaTokenizer.from_pretrained('Finnish-NLP/roberta-large-finnish-v2')
model = RobertaModel.from_pretrained('Finnish-NLP/roberta-large-finnish-v2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```python
from transformers import RobertaTokenizer, TFRobertaModel
tokenizer = RobertaTokenizer.from_pretrained('Finnish-NLP/roberta-large-finnish-v2')
model = TFRobertaModel.from_pretrained('Finnish-NLP/roberta-large-finnish-v2', from_pt=True)
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

### Limitations and bias

The training data used for this model contains a lot of unfiltered content from the internet, which is far from
neutral. Therefore, the model can have biased predictions.

## Training data

This Finnish RoBERTa model was pretrained on the combination of five datasets:
- [mc4_fi_cleaned](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned), the dataset mC4 is a multilingual colossal, cleaned version of Common Crawl's web crawl corpus. We used the Finnish subset of the mC4 dataset and further cleaned it with our own text data cleaning codes (check the dataset repo).
- [wikipedia](https://huggingface.co/datasets/wikipedia) We used the Finnish subset of the wikipedia (August 2021) dataset
- [Yle Finnish News Archive](http://urn.fi/urn:nbn:fi:lb-2017070501)
- [Finnish News Agency Archive (STT)](http://urn.fi/urn:nbn:fi:lb-2018121001)
- [The Suomi24 Sentences Corpus](http://urn.fi/urn:nbn:fi:lb-2020021803)

Raw datasets were cleaned to filter out bad quality and non-Finnish examples. Together these cleaned datasets were around 84GB of text.

## Training procedure

### Preprocessing

The texts are tokenized using a byte version of Byte-Pair Encoding (BPE) and a vocabulary size of 50265. The inputs of
the model take pieces of 512 contiguous token that may span over documents. The beginning of a new document is marked
with `<s>` and the end of one by `</s>`

The details of the masking procedure for each sentence are the following:
- 15% of the tokens are masked.
- In 80% of the cases, the masked tokens are replaced by `<mask>`.

- In 10% of the cases, the masked tokens are replaced by a random token (different) from the one they replace.
- In the 10% remaining cases, the masked tokens are left as is.

Contrary to BERT, the masking is done dynamically during pretraining (e.g., it changes at each epoch and is not fixed).

### Pretraining

The model was trained on TPUv3-8 VM, sponsored by the [Google TPU Research Cloud](https://sites.research.google/trc/about/), for 520k train steps (2 epochs, batch size 512) with a sequence length of 128 and continuing for 520k steps (1 epoch, batch size 64) with a sequence length of 512. The optimizer used for the 128 sequence training was AdamW, and for the 512 sequence training it was Adafactor (to save memory). Learning rate was 2e-4, \\(\beta_{1} = 0.9\\), \\(\beta_{2} = 0.98\\) and \\(\epsilon = 1e-6\\), learning rate warmup for 1500 steps and linear decay of the learning rate after.

## Evaluation results

Evaluation was done by fine-tuning the model on downstream text classification task with two different labeled datasets: [Yle News](https://github.com/spyysalo/yle-corpus) and [Eduskunta](https://github.com/aajanki/eduskunta-vkk). Yle News classification fine-tuning was done with two different sequence lengths: 128 and 512 but Eduskunta only with 128 sequence length.
When fine-tuned on those datasets, this model (the first row of the table) achieves the following accuracy results compared to the [FinBERT (Finnish BERT)](https://huggingface.co/TurkuNLP/bert-base-finnish-cased-v1) model and to our previous [Finnish-NLP/roberta-large-finnish](https://huggingface.co/Finnish-NLP/roberta-large-finnish) model:

|                                        | Average  | Yle News 128 length | Yle News 512 length | Eduskunta 128 length |
|----------------------------------------|----------|---------------------|---------------------|----------------------|
|Finnish-NLP/roberta-large-finnish-v2    |88.17     |94.46                |95.22                |74.83                 |
|Finnish-NLP/roberta-large-finnish       |88.02     |94.53                |95.23                |74.30                 |
|TurkuNLP/bert-base-finnish-cased-v1     |**88.82** |**94.90**            |**95.49**            |**76.07**             |

To conclude, this model didn't significantly improve compared to our previous [Finnish-NLP/roberta-large-finnish](https://huggingface.co/Finnish-NLP/roberta-large-finnish) model. This model is also slightly (~ 1%) losing to the [FinBERT (Finnish BERT)](https://huggingface.co/TurkuNLP/bert-base-finnish-cased-v1) model.

## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗
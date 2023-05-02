---
language:
- fi
license: apache-2.0
tags:
- finnish
- t5
- t5x
- seq2seq
datasets:
- Finnish-NLP/mc4_fi_cleaned
- wikipedia
inference: false

---

# T5-base-nl36 for Finnish

Pretrained T5 model on Finnish language using a span-based masked language modeling (MLM) objective. T5 was introduced in
[this paper](https://arxiv.org/abs/1910.10683)
and first released at [this page](https://github.com/google-research/text-to-text-transfer-transformer).

**Note:** The Hugging Face inference widget is deactivated because this model needs a text-to-text fine-tuning on a specific downstream task to be useful in practice. As an example of a fine-tuned Finnish T5 model, you can check [Finnish-NLP/t5-small-nl24-casing-punctuation-correction](https://huggingface.co/Finnish-NLP/t5-small-nl24-casing-punctuation-correction) which has been fine-tuned to correct missing casing and punctuation for Finnish text.

## Model description

T5 is an encoder-decoder model and treats all NLP problems in a text-to-text format.

Finnish T5 is a transformers model pretrained on a very large corpus of Finnish data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and outputs from those texts.

More precisely, it was pretrained with the span-based masked language modeling (MLM) objective. Spans of the input sequence are masked by so-called sentinel tokens (a.k.a unique mask tokens) and the output sequence is formed as a concatenation of the same sentinel tokens and the real masked tokens. This way, the model learns an inner representation of the Finnish language.

This model used the [T5 v1.1](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#t511) improvements compared to the original T5 model during the pretraining:
- GEGLU activation in feed-forward hidden layer, rather than ReLU - see [here](https://arxiv.org/abs/2002.05202)
- Dropout was turned off in pretraining (quality win). Dropout should be re-enabled during fine-tuning
- Pretrained on span-based masked language modeling (MLM) objective only without mixing in the downstream tasks
- No parameter sharing between embedding and classifier layer

This model also used the "efficient" T5 architecture findings presented in [this paper](https://arxiv.org/abs/2109.10686). In a nutshell, the paper indicates that a Deep-Narrow model architecture is favorable for downstream performance compared to other model architectures of similar parameter count. To be more precise, model depth is defined as the number of transformer blocks that are stacked sequentially.

This model uses the [t5-efficient-base-nl36](https://huggingface.co/google/t5-efficient-base-nl36) architecture's layer depth which means both the encoder and the decoder have 36 transformer layers compared to the original T5 "base" model's architecture of 12 transformer layers.

In total, this model has 814 million parameters.

## Intended uses & limitations

This model was only pretrained in a self-supervised way excluding any supervised training. Therefore, this model has to be fine-tuned before it is usable on a downstream task, like text classification, unlike the Google's original T5 model. **Note:** You most likely need to fine-tune these T5 models without mixed precision so fine-tune them with full fp32 precision. You can also find more fine-tuning tips from [here](https://discuss.huggingface.co/t/t5-finetuning-tips), for example.

### How to use

Here is how to use this model in PyTorch:

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Finnish-NLP/t5-base-nl36-finnish")
model = T5ForConditionalGeneration.from_pretrained("Finnish-NLP/t5-base-nl36-finnish")
```

and in TensorFlow:

```python
from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Finnish-NLP/t5-base-nl36-finnish")
model = T5ForConditionalGeneration.from_pretrained("Finnish-NLP/t5-base-nl36-finnish", from_pt=True)
```

### Limitations and bias

The training data used for this model contains a lot of unfiltered content from the internet, which is far from neutral. Therefore, the model can have biased predictions. This bias will also affect all fine-tuned versions of this model.

## Training data

This Finnish T5 model was pretrained on the combination of six datasets:
- [mc4_fi_cleaned](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned), the dataset mC4 is a multilingual colossal, cleaned version of Common Crawl's web crawl corpus. We used the Finnish subset of the mC4 dataset and further cleaned it with our own text data cleaning codes (check the dataset repo).
- [wikipedia](https://huggingface.co/datasets/wikipedia) We used the Finnish subset of the wikipedia (August 2021) dataset
- [Yle Finnish News Archive 2011-2018](http://urn.fi/urn:nbn:fi:lb-2017070501)
- [Yle Finnish News Archive 2019-2020](http://urn.fi/urn:nbn:fi:lb-2021050401)
- [Finnish News Agency Archive (STT)](http://urn.fi/urn:nbn:fi:lb-2018121001)
- [The Suomi24 Sentences Corpus](http://urn.fi/urn:nbn:fi:lb-2020021803)

Raw datasets were automatically cleaned to filter out bad quality and non-Finnish examples. Also, a [perplexity](https://huggingface.co/course/chapter7/3#perplexity-for-language-models) score was calculated for all texts with a KenLM model which was trained with very clean Finnish texts only. This perplexity score can then be used to determine how "clean" Finnish language the text contains. Lastly, all datasets were concatenated and the top 90% perplexity score was used as a filtering threshold to filter out the worst quality 10% of texts. Together these cleaned datasets were around 76GB of text.

## Training procedure

### Preprocessing

The texts are tokenized using WordPiece and a vocabulary size of 32000. The inputs and the outputs are sequences of 512 consecutive tokens. Texts are not lower cased so this model is case-sensitive: it makes a difference between finnish and Finnish.

### Pretraining

The model was trained on TPUv3-8 VM, sponsored by the [Google TPU Research Cloud](https://sites.research.google/trc/about/), for 1M steps with a batch size of 64 (in total 33B tokens). The optimizer used was a AdaFactor with learning rate warmup for 10K steps with a constant learning rate of 1e-2, and then an inverse square root decay (exponential decay) of the learning rate after.

Training code was from the Google's Jax/Flax based [t5x framework](https://github.com/google-research/t5x) and also some t5x task definitions were adapted from [Per's t5x work](https://huggingface.co/pere).

## Evaluation results

Evaluation was done by fine-tuning the model on a downstream text classification task with two different labeled Finnish datasets: [Yle News](https://github.com/spyysalo/yle-corpus) and [Eduskunta](https://github.com/aajanki/eduskunta-vkk). Classification fine-tuning was done with a sequence length of 128 tokens.

When fine-tuned on those datasets, this model (the sixth row of the table) achieves the following accuracy results compared to our other T5 models and their parameter counts:

|                                                       | Model parameters | Yle News accuracy   | Eduskunta accuracy   |
|-------------------------------------------------------|------------------|---------------------|----------------------|
|Finnish-NLP/t5-tiny-nl6-finnish                        | 31 million       |92.80                |69.07                 |
|Finnish-NLP/t5-mini-nl8-finnish                        | 72 million       |93.89                |71.43                 |
|Finnish-NLP/t5-small-nl16-finnish                      | 184 million      |94.46                |74.00                 |
|Finnish-NLP/t5-small-nl24-finnish                      | 260 million      |**94.68**            |74.90                 |
|Finnish-NLP/byt5-base-finnish                          | 582 million      |92.33                |73.13                 |
|Finnish-NLP/t5-base-nl36-finnish                       | 814 million      |94.40                |**75.97**             |
|Finnish-NLP/t5-large-nl36-finnish                      | 1425 million     |94.17                |73.50                 |


Fine-tuning Google's multilingual mT5 models on the same datasets we can clearly see that our monolingual Finnish T5 models achieve much better results on Finnish text classification:

|                                                       | Model parameters | Yle News accuracy   | Eduskunta accuracy   |
|-------------------------------------------------------|------------------|---------------------|----------------------|
|google/mt5-small                                       | 301 million      |91.51                |64.10                 |
|google/mt5-base                                        | 583 million      |92.71                |68.40                 |


## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗
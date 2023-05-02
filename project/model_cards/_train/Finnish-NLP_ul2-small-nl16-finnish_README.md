---
language:
- fi
license: apache-2.0
tags:
- finnish
- t5
- t5x
- seq2seq
- ul2
datasets:
- Finnish-NLP/mc4_fi_cleaned
- wikipedia
inference: false

---

# UL2-small-nl16 for Finnish

Pretrained T5 model on Finnish language using a UL2 (Mixture-of-Denoisers) objective. T5 model was introduced in
[this paper](https://arxiv.org/abs/1910.10683)
and first released at [this page](https://github.com/google-research/text-to-text-transfer-transformer).
The UL2 objective was introduced in
[this paper](https://arxiv.org/abs/2205.05131)
and first released at [this page](https://github.com/google-research/google-research/tree/master/ul2).

**Note:** The Hugging Face inference widget is deactivated because this model needs a text-to-text fine-tuning on a specific downstream task to be useful in practice. As an example of a fine-tuned Finnish T5 model, you can check [Finnish-NLP/t5-small-nl24-casing-punctuation-correction](https://huggingface.co/Finnish-NLP/t5-small-nl24-casing-punctuation-correction) which has been fine-tuned to correct missing casing and punctuation for Finnish text.

## Model description

T5 is an encoder-decoder model and treats all NLP problems in a text-to-text format.

Finnish T5 is a transformers model pretrained on a very large corpus of Finnish data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and outputs from those texts.

This model used the [T5 v1.1](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#t511) improvements compared to the original T5 model during the pretraining:
- GEGLU activation in feed-forward hidden layer, rather than ReLU - see [here](https://arxiv.org/abs/2002.05202)
- Dropout was turned off in pretraining (quality win). Dropout should be re-enabled during fine-tuning
- Pretrained on self-supervised objective only without mixing in the downstream tasks
- No parameter sharing between embedding and classifier layer

This model also used the "efficient" T5 architecture findings presented in [this paper](https://arxiv.org/abs/2109.10686). In a nutshell, the paper indicates that a Deep-Narrow model architecture is favorable for downstream performance compared to other model architectures of similar parameter count. To be more precise, model depth is defined as the number of transformer blocks that are stacked sequentially.

This model uses the [t5-efficient-small-nl16](https://huggingface.co/google/t5-efficient-small-nl16) architecture's layer depth which means both the encoder and the decoder have 16 transformer layers compared to the original T5 "small" model's architecture of 6 transformer layers.

In total, this model has 184 million parameters.

### UL2 pretraining objective

This model was pretrained with the UL2's Mixture-of-Denoisers (MoD) objective, that combines diverse pre-training paradigms together. UL2 frames different objective functions for training language models as denoising tasks, where the model has to recover missing sub-sequences of a given input. During pre-training it uses a novel mixture-of-denoisers that samples from a varied set of such objectives, each with different configurations. UL2 is trained using a mixture of three denoising tasks: (1) R-denoising (or regular span corruption), which emulates the standard T5 span corruption objective; (2) X-denoising (or extreme span corruption); and (3) S-denoising (or sequential PrefixLM). During pre-training, we sample from the available denoising tasks based on user-specified ratios.

UL2 introduces a notion of mode switching, wherein downstream fine-tuning is associated with specific pre-training denoising task. During the pretraining, a paradigm token is inserted to the input (`[NLU]` for R-denoising, `[NLG]` for X-denoising, or `[S2S]` for S-denoising) indicating the denoising task at hand. Then, during fine-tuning the same input token should be inserted to get the best performance for different downstream fine-tuning tasks.

## Intended uses & limitations

This model was only pretrained in a self-supervised way excluding any supervised training. Therefore, this model has to be fine-tuned before it is usable on a downstream task, like text classification, unlike the Google's original T5 model. **Note:** You most likely need to fine-tune these T5/UL2 models without mixed precision so fine-tune them with full fp32 precision. You can also find more fine-tuning tips from [here](https://discuss.huggingface.co/t/t5-finetuning-tips), for example.

**Note**: For fine-tuning, most likely you can get better results if you insert a prefix token of `[NLU]`, `[NLG]`, or `[S2S]` to your input texts. For general language understanding fine-tuning tasks, you could use the `[NLU]` token. For GPT-style causal language generation, you could use the `[S2S]` token. The token `[NLG]` of the X-denoising pretrain task is somewhat mix between the language understanding and causal language generation so the token `[NLG]` could maybe be used for language generation fine-tuning too.

### How to use

Here is how to use this model in PyTorch:

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Finnish-NLP/ul2-small-nl16-finnish")
model = T5ForConditionalGeneration.from_pretrained("Finnish-NLP/ul2-small-nl16-finnish")
```

and in TensorFlow:

```python
from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Finnish-NLP/ul2-small-nl16-finnish")
model = T5ForConditionalGeneration.from_pretrained("Finnish-NLP/ul2-small-nl16-finnish", from_pt=True)
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

The model was trained on TPUv3-8 VM, sponsored by the [Google TPU Research Cloud](https://sites.research.google/trc/about/), for 500K steps with a batch size of 256 (in total 66B tokens). The optimizer used was a AdaFactor with learning rate warmup for 10K steps with a constant learning rate of 1e-2, and then an inverse square root decay (exponential decay) of the learning rate after.

Training code was from the Google's Jax/Flax based [t5x framework](https://github.com/google-research/t5x) and also some t5x task definitions were adapted from [Per's t5x work](https://huggingface.co/pere).

The UL2 training objective code used with the [t5x framework](https://github.com/google-research/t5x) was copied and slightly modified from the [UL2 paper](https://arxiv.org/pdf/2205.05131.pdf) appendix chapter 9.2. Used UL2 objective code is available in this repository in the files `ul2_objective.py` and `tasks.py`.
UL2's mixture-of-denoisers configuration was otherwise equal to the UL2 paper but for the rate of mixing denoisers, 20% for S-denoising was used (suggested at the paper chapter 4.5) and the rest was divided equally between the R-denoising and X-denoising (i.e. 40% for both).

## Evaluation results

Evaluation was done by fine-tuning the model on a downstream text classification task with two different labeled Finnish datasets: [Yle News](https://github.com/spyysalo/yle-corpus) and [Eduskunta](https://github.com/aajanki/eduskunta-vkk). Classification fine-tuning was done with a sequence length of 128 tokens. Also, for UL2 models a prefix token of `[NLU]` has been added to each input text.

When fine-tuned on those datasets, this model (the third row of the table) achieves the following accuracy results compared to our other UL2 models and their parameter counts:

|                                                       | Model parameters | Yle News accuracy   | Eduskunta accuracy   |
|-------------------------------------------------------|------------------|---------------------|----------------------|
|Finnish-NLP/ul2-tiny-nl6-finnish                       | 31 million       |92.88                |69.40                 |
|Finnish-NLP/ul2-mini-nl8-finnish                       | 72 million       |93.83                |70.10                 |
|Finnish-NLP/ul2-small-nl16-finnish                     | 184 million      |94.25                |74.63                 |
|Finnish-NLP/ul2-small-nl24-finnish                     | 260 million      |94.03                |73.87                 |
|Finnish-NLP/ul2-base-nl36-finnish                      | 814 million      |94.35                |75.47                 |


Results of fine-tuning our T5 models (with the original T5 pretraining task) on the same datasets are following:

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
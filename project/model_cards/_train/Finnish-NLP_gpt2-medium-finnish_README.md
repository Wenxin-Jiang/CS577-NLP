---
language:
- fi
license: apache-2.0
tags:
- finnish
- gpt2
datasets:
- Finnish-NLP/mc4_fi_cleaned
- wikipedia
widget:
- text: "Tekstiä tuottava tekoäly on"

---

# GPT-2 medium for Finnish

Pretrained GPT-2 medium model on Finnish language using a causal language modeling (CLM) objective. GPT-2 was introduced in
[this paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
and first released at [this page](https://openai.com/blog/better-language-models/).

**Note**: this model is 345M parameter variant as in Huggingface's [GPT-2-medium config](https://huggingface.co/gpt2-medium), so not the famous big 1.5B parameter variant by OpenAI. We also have bigger 774M parameter variant [gpt2-large-finnish](https://huggingface.co/Finnish-NLP/gpt2-large-finnish) available which performs better compared to this model.

## Model description

Finnish GPT-2 is a transformers model pretrained on a very large corpus of Finnish data in a self-supervised fashion. This
means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots
of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely,
it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence,
shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the
predictions for the token `i` only uses the inputs from `1` to `i` but not the future tokens.

This way, the model learns an inner representation of the Finnish language that can then be used to extract features
useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a
prompt.

## Intended uses & limitations

You can use the raw model for text generation or fine-tune it to a downstream task. See the
[model hub](https://huggingface.co/models?filter=gpt2) to look for fine-tuned versions on a task that interests you.

### How to use

You can use this model directly with a pipeline for text generation:

```python
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='Finnish-NLP/gpt2-medium-finnish')
>>> generator("Tekstiä tuottava tekoäly on", max_length=30, num_return_sequences=5)

[{'generated_text': 'Tekstiä tuottava tekoäly on tullut ihmisten arkeen viime vuosina. Se auttaa hahmottamaan ja tulkitsemaan monimutkaisia kokonaisuuksia ja ilmiöitä, joita ihmiset tekevät esimerkiksi ruokakaupassa'},
 {'generated_text': 'Tekstiä tuottava tekoäly on jo ottanut haltuunsa myös ihmisten käyttämiä sovelluksia ja esimerkiksi pankkipalveluita. Sen vuoksi tekoäly on tärkeä kumppani etenkin yritysten liiketoiminnan kehittämisessä.-'},
 {'generated_text': 'Tekstiä tuottava tekoäly on tekoälylle luonnollinen valinta, sillä sen avulla voi kommunikoida ihmisten kanssa hyvin pitkälle samalla tavalla kuin tietokoneiden kanssa. Se on kehittynyt muun'},
 {'generated_text': 'Tekstiä tuottava tekoäly on ihmisen kehittämä tekoäly, jota ei vielä ole pystytty rakentamaan. Tekoäly kykenee toimimaan esimerkiksi matemaattisissa, tilastollisissa ja sosiaalisissa'},
 {'generated_text': 'Tekstiä tuottava tekoäly on jo niin iso juttu ettei sitä kannata rajoittaakaan. Ja jos se saadaan käyttöön, niin se voi jo pian syrjäyttää perinteisen'}]
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('Finnish-NLP/gpt2-medium-finnish')
model = GPT2Model.from_pretrained('Finnish-NLP/gpt2-medium-finnish')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```python
from transformers import GPT2Tokenizer, TFGPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('Finnish-NLP/gpt2-medium-finnish')
model = TFGPT2Model.from_pretrained('Finnish-NLP/gpt2-medium-finnish', from_pt=True)
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

### Limitations and bias

The training data used for this model contains a lot of unfiltered content from the internet, which is far from neutral. Therefore, the model can have biased predictions. This bias will also affect all fine-tuned versions of this model.

As with all language models, it is hard to predict in advance how the Finnish GPT-2 will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results.

## Training data

This Finnish GPT-2 model was pretrained on the combination of six datasets:
- [mc4_fi_cleaned](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned), the dataset mC4 is a multilingual colossal, cleaned version of Common Crawl's web crawl corpus. We used the Finnish subset of the mC4 dataset and further cleaned it with our own text data cleaning codes (check the dataset repo).
- [wikipedia](https://huggingface.co/datasets/wikipedia) We used the Finnish subset of the wikipedia (August 2021) dataset
- [Yle Finnish News Archive 2011-2018](http://urn.fi/urn:nbn:fi:lb-2017070501)
- [Yle Finnish News Archive 2019-2020](http://urn.fi/urn:nbn:fi:lb-2021050401)
- [Finnish News Agency Archive (STT)](http://urn.fi/urn:nbn:fi:lb-2018121001)
- [The Suomi24 Sentences Corpus](http://urn.fi/urn:nbn:fi:lb-2020021803)

Raw datasets were cleaned to filter out bad quality and non-Finnish examples. Together these cleaned datasets were around 84GB of text.

## Training procedure

### Preprocessing

The texts are tokenized using a byte-level version of Byte Pair Encoding (BPE) (for unicode characters) and a
vocabulary size of 50,257. The inputs are sequences of 512 consecutive tokens.

### Pretraining

The model was trained on TPUv3-8 VM, sponsored by the [Google TPU Research Cloud](https://sites.research.google/trc/about/), for 360k steps (a bit over 1 epoch, 128 batch size). The optimizer used was a AdamW with learning rate 1e-4, learning rate warmup for 4000 steps and cosine decay of the learning rate after.


## Evaluation results

Evaluation was done using the *validation* split of the [mc4_fi_cleaned](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned) dataset with [Perplexity](https://huggingface.co/course/chapter7/3#perplexity-for-language-models) (smaller score the better) as the evaluation metric. As seen from the table below, this model (the first row of the table) performs better than our smaller [gpt2-finnish](https://huggingface.co/Finnish-NLP/gpt2-finnish) model variant but loses to our bigger [gpt2-large-finnish](https://huggingface.co/Finnish-NLP/gpt2-large-finnish) model.

|                                          | Perplexity |
|------------------------------------------|------------|
|Finnish-NLP/gpt2-medium-finnish           |34.08       |
|Finnish-NLP/gpt2-finnish                  |44.19       |
|Finnish-NLP/gpt2-large-finnish            |**30.74**   |

## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗
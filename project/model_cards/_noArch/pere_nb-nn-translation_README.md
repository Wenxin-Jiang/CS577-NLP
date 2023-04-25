---
language: no
license: cc-by-4.0
tags:
- translation
datasets:
- oscar
widget:
- text: Skriv inn en tekst som du ønsker å oversette til en annen målform.
---


# 🇳🇴 Bokmål ⇔ Nynorsk 🇳🇴  
Norwegian has two relatively similar written languages; Bokmål and Nynorsk. Historically Nynorsk is a written norm based on dialects curated by the linguist Ivar Aasen in the mid-to-late 1800s, whereas Bokmål is a gradual 'Norwegization' of written Danish.
The two written languages are considered equal and citizens have a right to receive public service information in their primary and prefered language. Even though this right has been around for a long time only between 5-10% of Norwegian texts are written in Nynorsk. Nynorsk is therefore a low-resource language within a low-resource language.

Apart from some word-list based engines, there are not any working off-the-shelf machine learning-based translation models. Translation between Bokmål and Nynorsk is not available in Google Translate. 

## Demo
|   |   |
|---|---|
| Widget                                | Try the widget in the top right corner |
| Huggingface Spaces                    | [Spaces Demo](https://huggingface.co/spaces/NbAiLab/nb2nn)                           |
|   |   |

## Pretraining a T5-base
There is an [mt5](https://huggingface.co/google/mt5-base) that includes Norwegian. Unfortunately a very small part of this is Nynorsk; there is only around 1GB Nynorsk text in mC4. Despite this, the mt5 also gives a BLEU score above 80. During the project we extracted all available Nynorsk text from the [Norwegian Colossal Corpus](https://github.com/NBAiLab/notram/blob/master/guides/corpus_v2_summary.md) at the National Library of Norway, and matched it (by material type i.e. book, newspapers and so on) with an equal amount of Bokmål. The corpus collection is described [here](https://github.com/NBAiLab/notram/blob/master/guides/nb_nn_balanced_corpus.md) and the total size is 19GB. 

## Finetuning - BLEU-SCORE 88.17 🎉
The central finetuning data of the project have been 200k translation units (TU) i.e. aligned pairs of sentences in the respective languages extracted from textbooks of various subjects and newspapers.

Training for [10] epochs with a learning rate of [7e-4], a batch size of [32] and a max source and target length of [512] fine tuning reached a SACREBLEU score of [88.03] at training and a test score of [**88.17**] after training. 

## This is not a translator
We found out that we were able to get almost identical BLEU-score with training it both ways, and letting the model decide if the input is in Bokmål or Nynorsk. This way we can train one model instead of two. We call it a language switcher.

## Future work
The following Google Docs Add-on is currently pending approval.
![Add-on](bm2nn_demo.gif)

## How to use the model
```python
# Set up the pipeline
from transformers import pipeline
translator = pipeline("translation", model='pere/nb-nn-translation')

# Do the translation
text = "Hun vil ikke gi bort sine personlige data."
print(translator(text, max_length=255))

```
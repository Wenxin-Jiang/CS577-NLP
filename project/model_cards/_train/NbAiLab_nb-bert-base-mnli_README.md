---
language: no
license: cc-by-4.0
thumbnail: https://raw.githubusercontent.com/NBAiLab/notram/master/images/nblogo_2.png
pipeline_tag: zero-shot-classification
tags:
- nb-bert
- zero-shot-classification
- pytorch
- tensorflow
- norwegian
- bert
datasets:
- mnli
- multi_nli
- xnli
widget:
- example_title: Nyhetsartikkel om FHI
  text: Folkehelseinstituttets mest optimistiske anslag er at alle voksne er ferdigvaksinert innen midten av september.
  candidate_labels: helse, politikk, sport, religion
---

**Release 1.0** (March 11, 2021)

# NB-Bert base model finetuned on Norwegian machine translated MNLI

## Description
The most effective way of creating a good classifier is to finetune a pre-trained model for the specific task at hand. However, in many cases this is simply impossible. 
[Yin et al.](https://arxiv.org/abs/1909.00161) proposed a very clever way of using pre-trained MNLI models as zero-shot sequence classifiers. The methods works by reformulating the question to an MNLI hypothesis. If we want to figure out if a text is about "sport", we simply state that "This text is about sport" ("Denne teksten handler om sport").

When the model is finetuned on the 400k large MNLI task, it is in many cases able to solve this classification tasks. There are no MNLI-set of this size in Norwegian but we have trained it on a machine translated version of the original MNLI-set.

## Testing the model
For testing the model, we recommend the [NbAiLab Colab Notebook](https://colab.research.google.com/gist/peregilk/769b5150a2f807219ab8f15dd11ea449/nbailab-mnli-norwegian-demo.ipynb)

## Hugging Face zero-shot-classification pipeline
The easiest way to try this out is by using the Hugging Face pipeline. Please, note that you will get better results when using Norwegian hypothesis template instead of the default English one. 
```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="NbAiLab/nb-bert-base-mnli")
```
You can then use this pipeline to classify sequences into any of the class names you specify.
```python
sequence_to_classify = 'Folkehelseinstituttets mest optimistiske anslag er at alle voksne er ferdigvaksinert innen midten av september.'
candidate_labels = ['politikk', 'helse', 'sport', 'religion']
hypothesis_template = 'Dette eksempelet er {}.'
classifier(sequence_to_classify, candidate_labels, hypothesis_template=hypothesis_template, multi_class=True)

# {'labels': ['helse', 'politikk', 'sport', 'religion'], 
# 'scores': [0.4210019111633301, 0.0674605593085289, 0.000840459018945694, 0.0007541406666859984],
# 'sequence': 'Folkehelseinstituttets mest optimistiske anslag er at alle over 18 år er ferdigvaksinert innen midten av september.'}

``` 

## More information

For more information on the model, see

https://github.com/NBAiLab/notram

Here you will also find a Colab explaining more in details how to use the zero-shot-classification pipeline.
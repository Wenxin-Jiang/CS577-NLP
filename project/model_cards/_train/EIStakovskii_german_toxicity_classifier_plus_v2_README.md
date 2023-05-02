---
language: de        # <-- my language
widget:
 - text: "Guten morgen, meine Liebe"
   example_title: "NOT TOXIC 1"
 - text: "Ich scheiß drauf."
   example_title: "TOXIC 1"
 - text: "Ich liebe dich"
   example_title: "NOT TOXIC 2" 
 - text: "Ich hab die Schnauze voll von diesen Irren."
   example_title: "TOXIC 2" 
 - text: "Ich wünsche Ihnen einen schönen Tag!"   
   example_title: "NOT TOXIC 3"
 - text: "Nigger"
   example_title: "TOXIC 3" 
 - text: "Du bist schon wieder zu spät!"   
   example_title: "NOT TOXIC 4"
 - text: "Beweg deinen AArschhh hier rüber"
   example_title: "TOXIC 4" 
   
license: other
---
## Description
NB: this version of the model is the improved version of [EIStakovskii/german_toxicity_classifier_plus](https://huggingface.co/EIStakovskii/german_toxicity_classifier_plus).
To see the source code of training and the data please follow [the github link](https://github.com/eistakovskii/NLP_projects/tree/main/TEXT_CLASSIFICATION).

This model was trained for toxicity labeling.

The model was fine-tuned based off [the dbmdz/bert-base-german-cased model](https://huggingface.co/dbmdz/bert-base-german-cased).

To use the model:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model = 'EIStakovskii/german_toxicity_classifier_plus_v2')

print(classifier("Verpiss dich von hier"))

```

## Metrics (at validation):

epoch|step|eval_accuracy|eval_f1|eval_loss
-|-|-|-|-
0.8|1200|0.9132176234979973|0.9113535629048755|0.24135465919971466

## Comparison against Perspective

This model was compared against the Google's [Perspective API](https://developers.perspectiveapi.com/s/?language=en_US) that similarly detects toxicity. 
Two models were tested on two datasets: the size of [200 sentences](https://github.com/eistakovskii/NLP_projects/blob/main/TEXT_CLASSIFICATION/data/Toxicity_Classifiers/DE_FR/test/test_de_200.csv) and [400 sentences](https://github.com/eistakovskii/NLP_projects/blob/main/TEXT_CLASSIFICATION/data/Toxicity_Classifiers/DE_FR/test/test_de_400.csv). 
The first one (arguably harder) was collected from the sentences of the [JigSaw](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data) and [DeTox](https://github.com/hdaSprachtechnologie/detox) datasets.
The second one (easier) was collected from the combination of sources: both from JigSaw and DeTox as well as [Paradetox](https://github.com/s-nlp/multilingual_detox/tree/main/data) translations and sentences extracted from [Reverso Context](https://context.reverso.net/translation/) by keywords.

# german_toxicity_classifier_plus_v2
size|accuracy|f1 
-|-|-
200|0.767|0.787
400|0.9650|0.9651

# Perspective
size|accuracy|f1 
-|-|-
200|0.834|0.820
400|0.892|0.885
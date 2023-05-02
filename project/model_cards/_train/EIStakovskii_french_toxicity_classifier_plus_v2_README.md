---
language: fr        # <-- my language
widget:
 - text: "J'aime ta coiffure"
   example_title: "NOT TOXIC 1" 
 - text: "Va te faire foutre"
   example_title: "TOXIC 1"
 - text: "Quel mauvais temps, n'est-ce pas ?"
   example_title: "NOT TOXIC 2" 
 - text: "J'espère que tu vas mourir, connard !"
   example_title: "TOXIC 2"
 - text: "j'aime beaucoup ta veste"   
   example_title: "NOT TOXIC 3"

license: other
---
## Description
NB: this version of the model is the improved version of [EIStakovskii/french_toxicity_classifier_plus](https://huggingface.co/EIStakovskii/french_toxicity_classifier_plus).
To see the source code of training and the data please follow [the github link](https://github.com/eistakovskii/NLP_projects/tree/main/TEXT_CLASSIFICATION/data/Toxicity_Classifiers/DE_FR).

This model was trained for toxicity labeling.

The model was fine-tuned based off [the CamemBERT language model](https://huggingface.co/camembert-base).


To use the model:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model = 'EIStakovskii/french_toxicity_classifier_plus_v2')

print(classifier("Foutez le camp d'ici!"))

```

## Metrics (at validation):

epoch|step|eval_accuracy|eval_f1|eval_loss
-|-|-|-|-
1.16|1600|0.9015412511332729|0.8968269048071442|0.3014959990978241

## Comparison against Perspective

This model was compared against the Google's [Perspective API](https://developers.perspectiveapi.com/s/?language=en_US) that similarly detects toxicity. 
Two models were tested on two datasets: the size of [200 sentences](https://github.com/eistakovskii/NLP_projects/blob/main/TEXT_CLASSIFICATION/data/Toxicity_Classifiers/DE_FR/test/test_fr_200.csv) and [400 sentences](https://github.com/eistakovskii/NLP_projects/blob/main/TEXT_CLASSIFICATION/data/Toxicity_Classifiers/DE_FR/test/test_fr_400.csv). 
The first one (arguably harder) was collected from the sentences of the [JigSaw](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data) and [DeTox](https://github.com/hdaSprachtechnologie/detox) datasets.
The second one (easier) was collected from the combination of sources: both from JigSaw and DeTox as well as [Paradetox](https://github.com/s-nlp/multilingual_detox/tree/main/data) translations and sentences extracted from [Reverso Context](https://context.reverso.net/translation/) by keywords.

# french_toxicity_classifier_plus_v2
size|accuracy|f1 
-|-|-
200|0.783|0.803
400|0.890|0.879

# Perspective
size|accuracy|f1 
-|-|-
200|0.826|0.795
**400|0.632|0.418

**I suspect that Perspective has such a low score in the case of the FR dataset (400) because it refuses to trigger on the words "merde" and "putain" and some more rarer words in French like "cul" and so on.
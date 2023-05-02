---
language: de        # <-- my language
datasets:
- news_commentary
widget:
 - text: "Unberechenbar, gefährlich, ja, auf jeden Fall."
   example_title: "Fluent example 1"
 - text: "Aber hinterher... oh, oh..."
   example_title: "Fluent example 2"
 - text: "Nettes Haus, was? - Ja."
   example_title: "Fluent example 3"
 - text: "Wissqween Sisssasde, adddddqwe12was Mdddilednberg war, 122huh?"
   example_title: "Disfluent example 1"
 - text: "asdaojn;klL:JjJALSJD"
   example_title: "Disfluent example 2"
 - text: "Was dDadasdDasein erster aaaaEind2ruck?"
   example_title: "Disfluent example 3"      

license: other
---

This model was trained for evaluating linguistic acceptability and grammaticality. The finetuning was carried out based off [the bert-base-german-cased](https://huggingface.co/bert-base-german-cased). 

To use the model:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model = 'EIStakovskii/bert-base-german-cased_fluency')

print(classifier("Wissqween Sisssasde, adddddqwe12was Mdddilednberg war, 122huh?"))

```

Label_1 means ACCEPTABLE - the sentence is perfectly understandable by native speakers and has no serious grammatic and syntactic flaws.

Label_0 means NOT ACCEPTABLE - the sentence is flawed both orthographically and grammatically.

The model was trained on 50 thousand German sentences from [the news_commentary dataset](https://huggingface.co/datasets/news_commentary). Out of 50 thousand 25 thousand sentences were algorithmically corrupted using [the open source Python library](https://github.com/eistakovskii/text_corruption_plus). The library was originally developed by [aylliote](https://github.com/aylliote/corruption), but it was slightly adapted for the purposes of this model.

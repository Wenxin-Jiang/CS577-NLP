---
language: fr        # <-- my language
datasets:
- news_commentary
widget:
 - text: "Ne laisse aucun résidu. Ne nécessite pas de nettoyage après l'application."
   example_title: "Fluent example 1"
 - text: "Nous n'avons pas d'argent et aucune relation."
   example_title: "Fluent example 2"
 - text: "C'est marrant comme tout le monde oublie ça, hein ?"
   example_title: "Fluent example 3"
 - text: "Il estaaaaaaaaaaad impr2éviswwible, oui,i,v.1 danfaagereux."
   example_title: "Disfluent example 1"
 - text: "L'hépssasdati@!@@!te, oui, une pleaaane indemnisation."
   example_title: "Disfluent example 2"
 - text: "Après une\\s hééésiéétation,!!! j'ai fait signe que oui."
   example_title: "Disfluent example 3"      

license: other
---
This model was trained for evaluating linguistic acceptability and grammaticality. The finetuning was carried out based off [the camembert-base model](https://huggingface.co/camembert/camembert-base).

To use the model:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model = 'EIStakovskii/camembert_base_fluency')

print(classifier("Il estaaaaaaaaaaad impr2éviswwible, oui,i,v.1 danfaagereux."))

```

Label_1 means ACCEPTABLE - the sentence is perfectly understandable by native speakers and has no serious grammatic and syntactic flaws.

Label_0 means NOT ACCEPTABLE - the sentence is flawed both orthographically and grammatically.

The model was trained on 50 thousand French sentences from [the news_commentary dataset](https://huggingface.co/datasets/news_commentary). Out of 50 thousand 25 thousand sentences were algorithmically corrupted using [the open source Python library](https://github.com/eistakovskii/text_corruption_plus). The library was originally developed by [aylliote](https://github.com/aylliote/corruption), but it was slightly adapted for the purposes of this model.
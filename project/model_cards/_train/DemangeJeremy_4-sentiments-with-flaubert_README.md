---
language: fr
tags: 
- sentiments
- text-classification
- flaubert 
- french
- flaubert-large
---

# Modèle de détection de 4 sentiments avec FlauBERT (mixed, negative, objective, positive) 

### Comment l'utiliser ?

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

loaded_tokenizer = AutoTokenizer.from_pretrained('flaubert/flaubert_large_cased')
loaded_model = AutoModelForSequenceClassification.from_pretrained("DemangeJeremy/4-sentiments-with-flaubert")

nlp = pipeline('sentiment-analysis', model=loaded_model, tokenizer=loaded_tokenizer)

print(nlp("Je suis plutôt confiant."))
```

```
[{'label': 'OBJECTIVE', 'score': 0.3320835530757904}]
```

## Résultats de l'évaluation du modèle

| Epoch | Validation Loss | Samples Per Second |
|:------:|:--------------:|:------------------:|
|     1 |        2.219246 |          49.476000 |
|     2 |        1.883753 |          47.259000 |
|     3 |        1.747969 |          44.957000 |
|     4 |        1.695606 |          43.872000 |
|     5 |        1.641470 |          45.726000 |


## Citation

Pour toute utilisation de ce modèle, merci d'utiliser cette citation : 

> Jérémy Demange, Four sentiments with FlauBERT, (2021), Hugging Face repository, <https://huggingface.co/DemangeJeremy/4-sentiments-with-flaubert>

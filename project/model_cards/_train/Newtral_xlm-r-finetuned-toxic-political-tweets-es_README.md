---
language: es
license: apache-2.0
---

# xlm-r-finetuned-toxic-political-tweets-es

This model is based on the pre-trained model [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) and was fine-tuned on a dataset of tweets from members of the [Spanish Congress of the Deputies](https://www.congreso.es/) annotated regarding the level of political toxicity they generate.

### Inputs

The model has been trained on the text of Spanish tweets authored by politicians in 2021, so this is the input expected and its performance can degrade when applied to texts from other domains.

### Outputs

The model predicts 2 signals of political toxicity:

* Toxic: the tweet has at least some degree of toxicity.
* Very Toxic: the tweet has a strong degree of toxicity.

A value between 0 and 1 is predicted for each signal.

### Intended uses & limitations 

The model was created to be used as a toxicity detector of spanish tweets from Spanish Congress Deputies. If the intended use is other one, for instance; toxicity detection on films reviews, the results won't be reliable and you might look for another model with this concrete purpose.


### How to use

The model can be used directly with a text-classification pipeline:

```python
>>> from transformers import pipeline
>>> text = "Es usted un auténtico impresentable, su señoría."
>>> pipe = pipeline("text-classification", model="Newtral/xlm-r-finetuned-toxic-political-tweets-es")
>>> pipe(text, return_all_scores=True)

[[{'label': 'toxic', 'score': 0.92560875415802},
  {'label': 'very toxic', 'score': 0.8310967683792114}]]
```

### Training procedure
The pre-trained model was fine-tuned for sequence classification using the following hyperparameters, which were selected from a validation set:

* Batch size = 32
* Learning rate = 2e-5
* Epochs = 5
* Max length = 64

The optimizer used was AdamW and the loss optimized was binary cross-entropy with class weights proportional to the class imbalance.
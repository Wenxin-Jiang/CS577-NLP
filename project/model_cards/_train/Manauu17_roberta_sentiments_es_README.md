# roberta_sentiments_es , a Sentiment Analysis model for Spanish sentences

This is a roBERTa-base model trained on ~58M tweets and finetuned for sentiment analysis. This model currently supports Spanish sentences


## Example of classification

```python
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
import pandas as pd
from scipy.special import softmax

MODEL = 'Manauu17/roberta_sentiments_es_en'

tokenizer = AutoTokenizer.from_pretrained(MODEL)

# PyTorch
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

text = ['@usuario siempre es bueno la opinión de un playo',
'Bendito año el que me espera']

encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
output = model(**encoded_input)
scores = output[0].detach().numpy()

# TensorFlow
model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)

text = ['La guerra no es buena para nadie.','Espero que mi jefe me de mañana libre']
encoded_input = tokenizer(text, return_tensors='tf', padding=True, truncation=True)
output = model(encoded_input) 
scores = output[0].numpy()


# Results
def get_scores(model_output, labels_dict):
  scores = softmax(model_output)
  frame = pd.DataFrame(scores, columns=labels.values())
  frame.style.highlight_max(axis=1,color="green")
  return frame

```
Output: 

```
# PyTorch
get_scores(scores, labels_dict).style.highlight_max(axis=1, color="green")

     Negative    Neutral     Positive
0    0.000607    0.004851    0.906596
1    0.079812    0.006650    0.001484

# TensorFlow
get_scores(scores, labels_dict).style.highlight_max(axis=1, color="green")

     Negative    Neutral     Positive
0    0.017030    0.008920    0.000667
1    0.000260    0.001695    0.971429


```

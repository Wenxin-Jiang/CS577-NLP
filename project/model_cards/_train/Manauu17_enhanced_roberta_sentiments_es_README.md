# roberta_sentiments_es_en , A Sentiment Analysis model for Spanish sentences

This is a roBERTa-base model trained on ~58M tweets and finetuned for sentiment analysis. This model currently supports Spanish sentences

This is a enhanced version of 'Manauu17/roberta_sentiments_es' following the BERT's SOAT to acquire best results. The last 4 hidden layers were concatenated folowing dense layers to get classification results. 

## Example of classification

```python
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
import pandas as pd
from scipy.special import softmax

MODEL = 'Manauu17/enhanced_roberta_sentiments_es'

tokenizer = AutoTokenizer.from_pretrained(MODEL)

# PyTorch
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

text = ['@usuario siempre es bueno la opinión de un playo',
'Bendito año el que me espera']

encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
output = model(**encoded_input)
scores = output[0].detach().numpy()

labels_dict = model.config.id2label

# Results
def get_scores(model_output, labels_dict):
  scores = softmax(model_output)
  frame = pd.DataFrame(scores, columns=model.config.id2label.values())
  frame.style.highlight_max(axis=1,color="green")
  return frame


# PyTorch
get_scores(scores, labels_dict).style.highlight_max(axis=1, color="green")


```
Output: 

```
# PyTorch
get_scores(scores, labels_dict).style.highlight_max(axis=1, color="green")

     Negative    Neutral     Positive
0    0.000607    0.004851    0.906596
1    0.079812    0.006650    0.001484

```

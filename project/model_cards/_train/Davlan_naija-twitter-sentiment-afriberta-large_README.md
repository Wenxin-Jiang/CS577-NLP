Hugging Face's logo
---
language: 
- hau
- ibo
- pcm
- yor
- multilingual

---
# naija-twitter-sentiment-afriberta-large
## Model description
**naija-twitter-sentiment-afriberta-large** is the first multilingual twitter **sentiment classification** model for four (4) Nigerian languages (Hausa, Igbo, Nigerian Pidgin, and Yorùbá) based on a fine-tuned  castorini/afriberta_large large model.  
It achieves the **state-of-the-art performance** for the twitter sentiment classification task trained on the [NaijaSenti corpus](https://github.com/hausanlp/NaijaSenti). 
The model has been trained to classify tweets into 3 sentiment classes: negative, neutral and positive
Specifically, this model is a *xlm-roberta-large* model that was fine-tuned on an aggregation of 4 Nigerian language datasets obtained from [NaijaSenti](https://github.com/hausanlp/NaijaSenti) dataset. 

## Intended uses & limitations
#### How to use
You can use this model with Transformers for Sentiment Classification.
```python
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax

MODEL = "Davlan/naija-twitter-sentiment-afriberta-large"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

text = "I like you"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
scores = output[0][0].detach().numpy()
scores = softmax(scores)

id2label = {0:"positive", 1:"neutral", 2:"negative"}

ranking = np.argsort(scores)
ranking = ranking[::-1]
for i in range(scores.shape[0]):
    l = id2label[ranking[i]]
    s = scores[ranking[i]]
    print(f"{i+1}) {l} {np.round(float(s), 4)}")
```
#### Limitations and bias
This model is limited by its training dataset and domain i.e Twitter. This may not generalize well for all use cases in different domains.  


## Training procedure
This model was trained on a single Nvidia RTX 2080 GPU with recommended hyperparameters from the [original NaijaSenti paper](https://arxiv.org/abs/2201.08277).
## Eval results on Test set (F-score), average over 5 runs.
language|F1-score
-|-
hau |81.2
ibo |80.8
pcm |74.5
yor |80.4

### BibTeX entry and citation info
```
@inproceedings{Muhammad2022NaijaSentiAN,
  title={NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis},
  author={Shamsuddeen Hassan Muhammad and David Ifeoluwa Adelani and Sebastian Ruder and Ibrahim Said Ahmad and Idris Abdulmumin and Bello Shehu Bello and Monojit Choudhury and Chris C. Emezue and Saheed Salahudeen Abdullahi and Anuoluwapo Aremu and Alipio Jeorge and Pavel B. Brazdil},
  year={2022}
}
```



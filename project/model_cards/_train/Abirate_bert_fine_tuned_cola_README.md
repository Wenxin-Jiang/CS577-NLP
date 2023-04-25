
## Petrained Model BERT: base model (cased)
BERT base model (cased) is a pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in this [paper](https://arxiv.org/abs/1810.04805) and first released in this [repository](https://github.com/google-research/bert). This model is case-sensitive: it makes a difference between english and English.



## Pretained Model Description
BERT is an auto-encoder transformer model pretrained on a large corpus of English data (English Wikipedia + Books Corpus) in a self-supervised fashion. This means the targets are computed from the inputs themselves, and humans are not needed to label the data. It was pretrained with two objectives:

- Masked language modeling (MLM)
- Next sentence prediction (NSP)

## Fine-tuned Model Description: BERT fine-tuned Cola
The pretrained model could be fine-tuned on other NLP tasks. The BERT model has been fine-tuned on a cola dataset from the GLUE BENCHAMRK, which is an academic benchmark that aims to measure the performance of ML models. Cola is one of the 11 datasets in this GLUE BENCHMARK. 

By fine-tuning BERT on cola dataset, the model is now able to classify a given setence gramatically and semantically as acceptable or not acceptable

## How to use ?
###### Directly with a pipeline for a text-classification NLP task
```python
from transformers import pipeline
cola = pipeline('text-classification', model='Abirate/bert_fine_tuned_cola')
cola("Tunisia is a beautiful country")

[{'label': 'acceptable', 'score': 0.989352285861969}]
```
###### Breaking down all the steps (Tokenization, Modeling, Postprocessing)
```python
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf
import numpy as np  

tokenizer = AutoTokenizer.from_pretrained('Abirate/bert_fine_tuned_cola')
model = TFAutoModelForSequenceClassification.from_pretrained("Abirate/bert_fine_tuned_cola")
text = "Tunisia is a beautiful country."
encoded_input = tokenizer(text, return_tensors='tf')

#The logits
output = model(encoded_input)
#Postprocessing
probas_output = tf.math.softmax(tf.squeeze(output['logits']), axis = -1)
class_preds = np.argmax(probas_output, axis = -1)

#Predicting the class acceptable or not acceptable
model.config.id2label[class_preds]

#Result 
'acceptable'
```
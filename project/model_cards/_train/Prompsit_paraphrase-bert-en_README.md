---
pipeline_tag: text-classification
inference: false
language: en
tags:
- transformers
---

# Prompsit/paraphrase-bert-en

This model allows to evaluate paraphrases for a given phrase.  
We have fine-tuned this model from pretrained "bert-base-uncased".

Model built under a TSI-100905-2019-4 project, co-financed by Ministry of Economic Affairs and Digital Transformation from the Government of Spain.

# How to use it

The model answer the following question: Is "phrase B" a paraphrase of "phrase A".
Please note that we're considering phrases instead of sentences. Therefore, we must take into account that the model doesn't expect to find punctuation marks or long pieces of text.

Resulting probabilities correspond to classes:  
* 0: Not a paraphrase
* 1: It's a paraphrase



So, considering the phrase "may be addressed" and a candidate paraphrase like "could be included", you can use the model like this:


```
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Prompsit/paraphrase-bert-en")
model = AutoModelForSequenceClassification.from_pretrained("Prompsit/paraphrase-bert-en")

input = tokenizer('may be addressed','could be included',return_tensors='pt')
logits = model(**input).logits
soft = torch.nn.Softmax(dim=1)
print(soft(logits))
```
Code output is:
 ``` 
 tensor([[0.1592, 0.8408]], grad_fn=<SoftmaxBackward>) 
 ```

As the probability of 1 (=It's a paraphrase) is 0.84 and the probability of 0 (=It is not a paraphrase) is 0.15, we can conclude, for our previous example, that "could be included" is a paraphrase of "may be addressed".



# Evaluation results

We have used as test dataset 16500 pairs of phrases human tagged. 

Metrics obtained are:

```
metrics={
 'test_loss': 0.5660144090652466, 
 'test_accuracy': 0.8170742794799527, 
 'test_precision': 0.7043977055449331, 
 'test_recall': 0.5978578383641675, 
 'test_f1': 0.6467696629213483, 
 'test_matthews_correlation': 0.5276716223607356, 
 'test_runtime': 19.3345, 
 'test_samples_per_second': 568.88, 
 'test_steps_per_second': 17.792
}

``` 
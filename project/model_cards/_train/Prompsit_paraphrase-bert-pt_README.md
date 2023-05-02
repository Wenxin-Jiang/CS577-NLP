---

pipeline_tag: text-classification
inference: false
language: pt
tags:
- transformers

---

# Prompsit/paraphrase-bert-pt

This model allows to evaluate paraphrases for a given phrase.  

We have fine-tuned this model from pretrained "neuralmind/bert-base-portuguese-cased".

Model built under a TSI-100905-2019-4 project, co-financed by Ministry of Economic Affairs and Digital Transformation from the Government of Spain.

# How to use it

The model answer the following question: Is "phrase B" a paraphrase of "phrase A".

Please note that we're considering phrases instead of sentences. Therefore, we must take into account that the model doesn't expect to find punctuation marks or long pieces of text.

Resulting probabilities correspond to classes:  

* 0: Not a paraphrase
* 1: It's a paraphrase

So, considering the phrase "logo após o homicídio" and a candidate paraphrase like "pouco depois do assassinato", you can use the model like this:

```

import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("Prompsit/paraphrase-bert-pt")
model = AutoModelForSequenceClassification.from_pretrained("Prompsit/paraphrase-bert-pt")

input = tokenizer('logo após o homicídio','pouco depois do assassinato',return_tensors='pt')
logits = model(**input).logits
soft = torch.nn.Softmax(dim=1)
print(soft(logits))

```

Code output is:

 ``` 

 tensor([[0.2137, 0.7863]], grad_fn=<SoftmaxBackward>)

 ```

As the probability of 1 (=It's a paraphrase) is 0.7863 and the probability of 0 (=It is not a paraphrase) is 0.2137, we can conclude, for our previous example, that "pouco depois do assassinato" is a paraphrase of "logo após o homicidio".

# Evaluation results

We have used as test dataset 16500 pairs of phrases human tagged. 

Metrics obtained are:

```
metrics={
 'test_loss': 0.6074697375297546, 
 'test_accuracy': 0.7809, 
 'test_precision': 0.7157638466220329, 
 'test_recall': 0.40551724137931033, 
 'test_f1': 0.5177195685670262, 
 'test_matthews_correlation': 0.41603913834665324, 
 'test_runtime': 16.4585, 
 'test_samples_per_second': 607.587, 
 'test_steps_per_second': 19.017
}
```
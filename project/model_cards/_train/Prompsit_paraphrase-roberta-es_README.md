---

pipeline_tag: text-classification
inference: false
language: es
tags:
- transformers

---

# Prompsit/paraphrase-roberta-es

This model allows to evaluate paraphrases for a given phrase.  

We have fine-tuned this model from pretrained "PlanTL-GOB-ES/roberta-base-bne".

Model built under a TSI-100905-2019-4 project, co-financed by Ministry of Economic Affairs and Digital Transformation from the Government of Spain.

# How to use it

The model answer the following question: Is "phrase B" a paraphrase of "phrase A".

Please note that we're considering phrases instead of sentences. Therefore, we must take into account that the model doesn't expect to find punctuation marks or long pieces of text.

Resulting probabilities correspond to classes:  

* 0: Not a paraphrase
* 1: It's a paraphrase

So, considering the phrase "se buscarán acuerdos" and a candidate paraphrase like "se deberá obtener el acuerdo", you can use the model like this:

```

import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("Prompsit/paraphrase-roberta-es")
model = AutoModelForSequenceClassification.from_pretrained("Prompsit/paraphrase-roberta-es")

input = tokenizer('se buscarán acuerdos','se deberá obtener el acuerdo',return_tensors='pt')
logits = model(**input).logits
soft = torch.nn.Softmax(dim=1)
print(soft(logits))

```

Code output is:

 ``` 

 tensor([[0.2266, 0.7734]], grad_fn=<SoftmaxBackward>)

 ```

As the probability of 1 (=It's a paraphrase) is 0.77 and the probability of 0 (=It is not a paraphrase) is 0.22, we can conclude, for our previous example, that "se deberá obtener el acuerdo" is a paraphrase of "se buscarán acuerdos".


# Evaluation results

We have used as test dataset 16500 pairs of phrases human tagged. 
Metrics obtained are:

```
metrics={
 'test_loss': 0.4869941473007202, 
 'test_accuracy': 0.8003636363636364, 
 'test_precision': 0.6692456479690522, 
 'test_recall': 0.5896889646357052, 
 'test_f1': 0.6269535673839184, 
 'test_matthews_correlation': 0.49324489316659575, 
 'test_runtime': 27.1537, 
 'test_samples_per_second': 607.652, 
 'test_steps_per_second': 19.003
 }

```
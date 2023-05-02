---
language: 
- fr
thumbnail: 
tags: 
- zero-shot-classification
- xnli
- nli
- fr
license: mit
pipeline_tag: zero-shot-classification
datasets: 
- xnli
metrics: 
- accuracy
---

# camembert-base-xnli

## Model description

Camembert-base model fine-tuned on french part of XNLI dataset. <br>
One of the few Zero-Shot classification model working on french 🇫🇷

## Intended uses & limitations

#### How to use

Two different usages : 

- As a Zero-Shot sequence classifier : 

```python
classifier = pipeline("zero-shot-classification", 
                      model="BaptisteDoyen/camembert-base-xnli")

sequence = "L'équipe de France joue aujourd'hui au Parc des Princes"
candidate_labels = ["sport","politique","science"]
hypothesis_template = "Ce texte parle de {}."    

classifier(sequence, candidate_labels, hypothesis_template=hypothesis_template)     
# outputs :                                        
# {'sequence': "L'équipe de France joue aujourd'hui au Parc des Princes",
# 'labels': ['sport', 'politique', 'science'],
# 'scores': [0.8595073223114014, 0.10821866989135742, 0.0322740375995636]}                      
```

- As a premise/hypothesis checker : <br>
The idea is here to compute a probability of the form \\( P(premise|hypothesis ) \\)

```python
# load model and tokenizer
nli_model = AutoModelForSequenceClassification.from_pretrained("BaptisteDoyen/camembert-base-xnli")
tokenizer = AutoTokenizer.from_pretrained("BaptisteDoyen/camembert-base-xnli") 
# sequences
premise = "le score pour les bleus est élevé"
hypothesis = "L'équipe de France a fait un bon match"
# tokenize and run through model
x = tokenizer.encode(premise, hypothesis, return_tensors='pt')
logits = nli_model(x)[0]
# we throw away "neutral" (dim 1) and take the probability of
# "entailment" (0) as the probability of the label being true 
entail_contradiction_logits = logits[:,::2]
probs = entail_contradiction_logits.softmax(dim=1)
prob_label_is_true = probs[:,0]
prob_label_is_true[0].tolist() * 100
# outputs
# 86.40775084495544
```

## Training data

Training data is the french fold of the [XNLI](https://research.fb.com/publications/xnli-evaluating-cross-lingual-sentence-representations/) dataset released in 2018 by Facebook. <br>
Available with great ease using the ```datasets``` library :

```python
from datasets import load_dataset
dataset = load_dataset('xnli', 'fr')                     
```

## Training/Fine-Tuning procedure

Training procedure is here pretty basic and was performed on the cloud using a single GPU. <br>
Main training parameters :
- ```lr = 2e-5```  with  ```lr_scheduler_type = "linear"```
- ```num_train_epochs = 4```
- ```batch_size = 12``` (limited by GPU-memory)
- ```weight_decay = 0.01```
- ```metric_for_best_model = "eval_accuracy"```

## Eval results

We obtain the following results on ```validation``` and ```test``` sets:

| Set        | Accuracy    |
| ---------- |-------------| 
| validation | 81.4        | 
| test       | 81.7        |

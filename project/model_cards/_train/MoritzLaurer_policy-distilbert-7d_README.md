---
language: 
- en
tags:
- text-classification
metrics:
- accuracy (balanced)
- F1 (weighted)
widget:
- text: "70-85% of the population needs to get vaccinated against the novel coronavirus to achieve herd immunity."

---


# Policy-DistilBERT-7d

## Model description

This model was trained on 129.669 manually annotated sentences to classify text into one of seven political categories: 'Economy', 'External Relations', 'Fabric of Society', 'Freedom and Democracy', 'Political System', 'Welfare and Quality of Life' or 'Social Groups'.

## Intended uses & limitations

#### How to use the model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "MoritzLaurer/policy-distilbert-7d"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "The new variant first detected in southern England in September is blamed for sharp rises in levels of positive tests in recent weeks in London, south-east England and the east of England"

input = tokenizer(text, truncation=True, return_tensors="pt")
output = model(input["input_ids"])
# the output corresponds to the following labels:
# 0: external relations, 1: freedom and democracy, 2: political system, 3: economy, 4: welfare and quality of life, 5: fabric of society, 6: social groups

# output to dictionary
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["external relations", "freedom and democracy", "political system", "economy", "welfare and quality of life", "fabric of society", "social groups"]
prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
print(prediction)
#{'external relations': 0.0, 'freedom and democracy': 0.0, 'political system': 0.9, 'economy': 0.4, 
# 'welfare and quality of life': 98.3, 'fabric of society': 0.3, 'social groups': 0.0}

```

### Training data

Policy-DistilBERT-7d was trained on the English-speaking subset of the [Manifesto Project Dataset (MPDS2020a)](https://manifesto-project.wzb.eu/datasets). The model was trained on 129.669 sentences from 164 political manifestos from 55 political parties in 8 English-speaking countries (Australia, Canada, Ireland, Israel, New Zealand, South Africa, United Kingdom, United States). The manifestos were published between 1992 - 2019. 

The Manifesto Project mannually annotates individual sentences from political party manifestos in 7 main political domains: 'Economy', 'External Relations', 'Fabric of Society', 'Freedom and Democracy', 'Political System', 'Welfare and Quality of Life' or 'Social Groups' - see the [codebook](https://manifesto-project.wzb.eu/down/data/2020b/codebooks/codebook_MPDataset_MPDS2020b.pdf) for the exact definitions of each domain. 


### Training procedure

`distilbert-base-uncased` was trained using the Hugging Face trainer with the following hyperparameters. The hyperparameters were determined using a hyperparameter search on a 15% validation set. 

```
training_args = TrainingArguments(
    num_train_epochs=5,              # total number of training epochs
    learning_rate=4e-05,
    per_device_train_batch_size=4,   # batch size per device during training
    per_device_eval_batch_size=4,    # batch size for evaluation
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    weight_decay=0.02,               # strength of weight decay
    fp16=True                        # mixed precision training
)
```

### Eval results

The model was evaluated using 15% of the sentences (85-15 train-test split).

accuracy (balanced)   | F1 (weighted) | precision | recall | accuracy (not balanced) 
-------|---------|----------|---------|----------
0.745  | 0.773 | 0.772 | 0.771 | 0.771

Please note that the label distribution in the dataset is imbalanced:
```
Welfare and Quality of Life    0.327225
Economy                        0.259191
Fabric of Society              0.111800
Political System               0.095081
Social Groups                  0.094371
External Relations             0.063724
Freedom and Democracy          0.048608
```

[Balanced accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html) and [weighted F1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html) were therefore used to evaluate model performance.


## Limitations and bias

The model was trained on sentences in political manifestos from parties in the 8 countries mentioned above between 1992-2019, manually annotated by the [Manifesto Project](https://manifesto-project.wzb.eu/information/documents/information). The model output therefore reproduces the limitations of the dataset in terms of country coverage, time span, domain definitions and potential biases of the annotators - as any supervised machine learning model would. Applying the model to other types of data (other types of texts, countries etc.) will reduce performance. 


### BibTeX entry and citation info

```bibtex
@unpublished{
  title={Policy-DistilBERT},
  author={Moritz Laurer},
  year={2020},
  note={Unpublished paper}
}
```
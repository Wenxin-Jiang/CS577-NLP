---
license: mit
metrics:
- accuracy
- precision
- recall
model-index:
- name: RoBERTa-RILE
  results: []
widget: 
- text: "Russia must end the war."
- text: "Democratic institutions must be supported."
- text: "The state must fight political corruption."
- text: "Our energy economy must be nationalised."
- text: "We must increase social spending."

---


# RoBERTa-RILE

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on data from the [Manifesto Project](https://manifesto-project.wzb.eu/).


## Model description

This model was trained on 115,943 manually annotated sentences to classify text into one of three political categories: "neutral", "left", "right".


## Intended uses & limitations

The model output reproduces the limitations of the dataset in terms of country coverage, time span, domain definitions and potential biases of the annotators - as any supervised machine learning model would. Applying the model to other types of data (other types of texts, countries etc.) will reduce performance.

```python
from transformers import pipeline
import pandas as pd
classifier = pipeline(
    task="text-classification",
    model="niksmer/RoBERTa-RILE")
# Load text data you want to classify
text = pd.read_csv("example.csv")["text_you_want_to_classify"].to_list()
# Inference
output = classifier(text)
# Print output
pd.DataFrame(output).head()
```

## Training and evaluation data

## Training and evaluation data

RoBERTa-RILE was trained on the English-speaking subset of the [Manifesto Project Dataset (MPDS2021a)](https://manifesto-project.wzb.eu/datasets). The model was trained on 115,943 sentences from 163 political manifestos in 7 English-speaking countries (Australia, Canada, Ireland, New Zealand, South Africa, United Kingdom, United States). The manifestos were published between 1992 - 2020. 

| Country        | Count manifestos | Count sentences | Time span        |
|----------------|------------------|-----------------|--------------------|
| Australia      | 18               | 14,887          | 2010-2016          |
| Ireland        | 23               | 24,966          | 2007-2016          |
| Canada         | 14               | 12,344          | 2004-2008 & 2015   |
| New Zealand    | 46               | 35,079          | 1993-2017          |
| South Africa   | 29               | 13,334          | 1994-2019          |
| USA            | 9                | 13,188          | 1992   & 2004-2020 |
| United Kingdom | 34               | 30,936          | 1997-2019          |

Canadian manifestos between 2004 and 2008 are used as test data.

The Manifesto Project mannually annotates individual sentences from political party manifestos in over 50 main categories - see the [codebook](https://manifesto-project.wzb.eu/down/papers/handbook_2021_version_5.pdf) for the exact definitions of each categorie. It has created a valid left-right-scale, the rile-index, to aaggregate manifesto in a standardized, onde-dimensional political space from left to right based on saliency-theory.
RoBERTa-RILE classifies texts based on the rile index.

### Tain data

Train data was slightly imbalanced.

| Label | Description | Count |
|------------|--------------|--------|
| 0          | neutral       | 52,277 |
| 1          | left       | 37,106 |
| 2          | right       | 26,560 |

Overall count: 115,943

### Validation data

The validation was created by chance.

| Label | Description | Count |
|------------|--------------|--------|
| 0          | neutral       | 9,198 |
| 1          | left       | 6,637 |
| 2          | right       | 4,626 |

Overall count: 20,461

### Test data

The test dataset contains ten canadian manifestos between 2004 and 2008.

| Label | Description | Count |
|------------|--------------|--------|
| 0          | neutral       | 3,881 |
| 1          | left       | 2,611 |
| 2          | right       | 1,838 |

Overall count: 8,330

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
```
training_args = TrainingArguments(
    warmup_ratio=0.05,
    weight_decay=0.1, 
    learning_rate=1e-05,
    fp16 = True,
    evaluation_strategy="epoch",
    num_train_epochs=5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    save_strategy="no",
    logging_dir='logs',   
    logging_strategy= 'steps',     
    logging_steps=10,
    push_to_hub=True,
    hub_strategy="end")
```

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1-micro | F1-macro | F1-weighted | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:--------:|:-----------:|:---------:|:------:|
| 0.7442        | 1.0   | 1812 | 0.6827          | 0.7120   | 0.7120   | 0.7007   | 0.7126      | 0.7120    | 0.7120 |
| 0.6447        | 2.0   | 3624 | 0.6618          | 0.7281   | 0.7281   | 0.7169   | 0.7281      | 0.7281    | 0.7281 |
| 0.5467        | 3.0   | 5436 | 0.6657          | 0.7309   | 0.7309   | 0.7176   | 0.7295      | 0.7309    | 0.7309 |
| 0.5179        | 4.0   | 7248 | 0.6654          | 0.7346   | 0.7346   | 0.7240   | 0.7345      | 0.7346    | 0.7346 |
| 0.4787        | 5.0   | 9060 | 0.6757          | 0.7350   | 0.7350   | 0.7241   | 0.7347      | 0.7350    | 0.7350 |

### Validation evaluation

| Model          | Micro F1-Score | Macro F1-Score | Weighted F1-Score |
|----------------|----------------|----------------|-------------------|
| RoBERTa-RILE |  0.74           | 0.72           | 0.73             |

### Test evaluation

| Model          | Micro F1-Score | Macro F1-Score | Weighted F1-Score |
|----------------|----------------|----------------|-------------------|
| RoBERTa-RILE | 0.69           | 0.67           | 0.69              |

### Evaluation per category

| Label                       | Validation F1-Score | Test F1-Score |
|-----------------------------|---------------------|---------------|
| neutral          | 0.77                | 0.74          |
| left       | 0.73                | 0.65          |
| right            | 0.67                | 0.62          |

### Evaluation based on saliency theory

Saliency theory is a theory to analyse politial text data. In sum, parties tend to write about policies in which they think that they are seen as competent.
Voters tend to assign advantages in policy competence in line to the assumed ideology of parties. Therefore you can analyze the share of policies parties tend to write about in their manifestos to analyze the party ideology.

The Manifesto Project presented for such an analysis the rile-index. For a quick overview, check [this](https://manifesto-project.wzb.eu/down/tutorials/main-dataset.html#measuring-parties-left-right-positions).

In the following plot, the predicted and original rile-indices are shown per manifesto in the test dataset. Overall the pearson correlation between the predicted and original rile-indices is 0.95. As alternative, you can use [ManiBERT](https://huggingface.co/niksmer/ManiBERT).

![image](english_robertarile_manifesto.png)

### Framework versions

- Transformers 4.16.2
- Pytorch 1.9.0+cu102
- Datasets 1.8.0
- Tokenizers 0.10.3

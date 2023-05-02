---
license: gpl-3.0
language: en
library: transformers
other: distilbert
datasets:
- Fake and real news dataset
---

# DistilBERT base cased model for Fake News Classification

## Model description

DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a
self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only,
with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic
process to generate inputs and labels from those texts using the BERT base model. 

This is a Fake News classification model finetuned [pretrained DistilBERT model](https://huggingface.co/distilbert-base-cased) on 
[Fake and real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

## Intended uses & limitations

This can only be used for the kind of news that are similar to the ones in the dataset,
please visit the [dataset's kaggle page](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) to see the data.

### How to use

You can use this model directly with a :

```python
>>> from transformers import pipeline
>>> classifier = pipeline("text-classification", model="Giyaseddin/distilbert-base-cased-finetuned-fake-and-real-news-dataset", return_all_scores=True)
>>> examples = ["Yesterday, Speaker Paul Ryan tweeted a video of himself on the Mexican border flying in a helicopter and traveling on horseback with US border agents. RT if you agree  It is time for The Wall. pic.twitter.com/s5MO8SG7SL  Paul Ryan (@SpeakerRyan) August 1, 2017It makes for great theater to see Republican Speaker Ryan pleading the case for a border wall, but how sincere are the GOP about building the border wall? Even after posting a video that appears to show Ryan s support for the wall, he still seems unsure of himself. It s almost as though he s testing the political winds when he asks Twitter users to retweet if they agree that we need to start building the wall. How committed is the (formerly?) anti-Trump Paul Ryan to building the border wall that would fulfill one of President Trump s most popular campaign promises to the American people? Does he have the what it takes to defy the wishes of corporate donors and the US Chamber of Commerce, and do the right thing for the national security and well-being of our nation?The Last Refuge- Republicans are in control of the House of Representatives, Republicans are in control of the Senate, a Republican President is in the White House, and somehow there s  negotiations  on how to fund the #1 campaign promise of President Donald Trump, the border wall.Here s the rub.Here s what pundits never discuss.The Republican party doesn t need a single Democrat to fund the border wall.A single spending bill could come from the House of Representatives that fully funds 100% of the border wall. The spending bill then goes to the senate, where again, it doesn t need a single Democrat vote because spending legislation is specifically what  reconciliation  was designed to facilitate. That House bill can pass the Senate with 51 votes and proceed directly to the President s desk for signature.So, ask yourself: why is this even a point of discussion?The honest answer, for those who are no longer suffering from Battered Conservative Syndrome, is that Republicans don t want to fund or build an actual physical barrier known as the Southern Border Wall.It really is that simple.If one didn t know better, they d almost think Speaker Ryan was attempting to emulate the man he clearly despised during the 2016 presidential campaign."]
>>> classifier(examples)
[[{'label': 'LABEL_0', 'score': 1.0},
  {'label': 'LABEL_1', 'score': 1.0119109106199176e-08}]]
```

### Limitations and bias

Even if the training data used for this model could be characterized as fairly neutral, this model can have biased
predictions. It also inherits some of
[the bias of its teacher model](https://huggingface.co/bert-base-uncased#limitations-and-bias).

This bias will also affect all fine-tuned versions of this model.

## Pre-training data

DistilBERT pretrained on the same data as BERT, which is [BookCorpus](https://yknzhu.wixsite.com/mbweb), a dataset
consisting of 11,038 unpublished books and [English Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia)
(excluding lists, tables and headers).

## Fine-tuning data

[Fake and real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)


## Training procedure

### Preprocessing

In the preprocessing phase, both the title and the text of the news are concatenated using a separator `[SEP]`.
This makes the full text as:

```
[CLS] Title Sentence [SEP] News text body [SEP]
```

The data are splitted according to the following ratio:
- Training set 60%.
- Validation set 20%.
- Test set 20%.

Lables are mapped as: `{fake: 0, true: 1}`

### Fine-tuning

The model was finetuned on GeForce GTX 960M for 5 hours. The parameters are:

|      Parameter      | Value | 
|:-------------------:|:-----:|
|    Learning rate    | 5e-5  | 
|    Weight decay     | 0.01  | 
| Training batch size |   4   | 
|       Epochs        |   3   | 

Here is the scores during the training:

|   Epoch    | Training Loss | 	 Validation Loss | 	 Accuracy |   	 F1    | 	 Precision | 	 Recall  |
|:----------:|:-------------:|:-----------------:|:----------:|:---------:|:-----------:|:---------:|
|     1      |   0.008300    |     	0.005783     | 	0.998330  | 	0.998252 |  	0.996511  | 	1.000000 |
|     2      |   0.000000    |     	0.000161     | 	0.999889  | 	0.999883 |  	0.999767  | 	1.000000 |
|     3      |   0.000000    |     	0.000122     | 	0.999889  | 	0.999883 |  	0.999767  | 	1.000000 |

## Evaluation results

When fine-tuned on downstream task of fake news binary classification, this model achieved the following results:
(scores are rounded to 2 floating points)

|              | precision | recall | f1-score | support |
|:------------:|:---------:|:------:|:--------:|:-------:|
|     Fake     |   1.00    |  1.00  |   1.00   |  4697   |
|     True     |   1.00    |  1.00  |   1.00   |  4283   |
|   accuracy   |     -     |   -    |   1.00   |  8980   |
|  macro avg   |   1.00    |  1.00  |   1.00   |  8980   |
| weighted avg |   1.00    |  1.00  |   1.00   |  8980   |

Confision matrix:


| Actual\Predicted  | Fake | True |
|:-----------------:|:----:|:----:|
|       Fake        | 4696 |  1   |
|       True        |  1   | 4282 |

The AUC score is 0.9997


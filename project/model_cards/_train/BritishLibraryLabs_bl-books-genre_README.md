---
language: multilingual
tags:
- genre
- books
- library
- historic
- glam
license: mit
metrics:
- f1
widget:
- text: >-
    Poems on various subjects. Whereto is prefixed a short essay on the
    structure of English verse
- text: >-
    Two Centuries of Soho: its institutions, firms, and amusements. By the
    Clergy of St. Anne's, Soho, J. H. Cardwell ... H. B. Freeman ... G. C.
    Wilton ... assisted by other contributors, etc
- text: The Adventures of Oliver Twist. [With plates.]
datasets:
- blbooksgenre
---

# British Library Books Genre Detector 

**Note** this model card is a work in progress. 

## Model description

This fine-tuned [`distilbert-base-cased`](https://huggingface.co/distilbert-base-cased) model is trained to predict whether a book from the [British Library's](https://www.bl.uk/) [Digitised printed books (18th-19th century)](https://www.bl.uk/collection-guides/digitised-printed-books) book collection is `fiction` or `non-fiction` based on the title of the book. 

## Intended uses & limitations

This model was trained on data created from the [Digitised printed books (18th-19th century)](https://www.bl.uk/collection-guides/digitised-printed-books) book collection. The datasets in this collection are comprised and derived from 49,455 digitised books (65,227 volumes) largely from the 19th Century. This dataset is dominated by English language books but also includes books in a number of other languages in much smaller numbers. Whilst a subset of this data has metadata relating to Genre, the majority of this dataset does not currently contain this information. 

This model was originally developed for use as part of the [Living with Machines](https://livingwithmachines.ac.uk/) project in order to be able to 'segment' this large dataset of books into different categories based on a 'crude' classification of genre i.e. whether the title was `fiction` or `non-fiction`. 

Particular areas where the model might be limited are:

### Title format
The model's training data (discussed more below) primarily consists of 19th Century book titles that have been catalogued according to British Library cataloguing practices. Since the approaches taken to cataloguing will vary across institutions running the model on titles from a different catalogue might introduce domain drift and lead to degraded model performance. 

To give an example of the types of titles includes in the training data here are 20 random examples: 

- 'The Canadian farmer. A missionary incident [Signed: W. J. H. Y, i.e. William J. H. Yates.]
- 'A new musical Interlude, called the Election [By M. P. Andrews.]',
- 'An Elegy written among the ruins of an Abbey. By the author of the Nun [E. Jerningham]',
- "The Baron's Daughter. A ballad by the author of Poetical Recreations [i.e. William C. Hazlitt] . F.P",
- 'A Little Book of Verse, etc',
- 'The Autumn Leaf Poems',
- 'The Battle of Waterloo, a poem',
- 'Maximilian, and other poems, etc',
- 'Fabellæ mostellariæ: or Devonshire and Wiltshire stories in verse; including specimens of the Devonshire dialect',
- 'The Grave of a Hamlet and other poems, chiefly of the Hebrides ... Selected, with an introduction, by his son J. Hogben']                                                                                                                                                                                                         

### Date                                                                                                                                                                                                    

The model was trained on data that spans the collection period of the [Digitised printed books (18th-19th century)](https://www.bl.uk/collection-guides/digitised-printed-books) book collection. This dataset covers a broad period (from 1500-1900). However, this dataset is skewed towards later years. The subset of training data i.e. data with genre annotations used to train this model has the following distribution for dates: 

|       | Date  |
|-------|------------|
| mean  |  1864.83   |
| std   |    43.0199 |
| min   |  1540      |
| 25%   |  1847      |
| 50%   |  1877      |
| 75%   |  1893      |


### Language 
  
Whilst the model is multilingual in so far as it has training data in non-English book titles, these appear much less frequently. An overview of the original training data's language counts are as follows:

| Language            | Count |
|---------------------|-------|
| English             | 22987 |
| Russian             |   461 |
| French              |   424 |
| Spanish             |   366 |
| German              |   347 |
| Dutch               |   310 |
| Italian             |   212 |
| Swedish             |   186 |
| Danish              |   164 |
| Hungarian           |   132 |
| Polish              |   112 |
| Latin               |    83 |
| Greek,Modern(1453-) |    42 |
| Czech               |    25 |
| Portuguese          |    24 |
| Finnish             |    14 |
| Serbian             |    10 |
| Bulgarian           |     7 |
| Icelandic           |     4 |
| Irish               |     4 |
| Hebrew              |     2 |
| NorwegianNynorsk    |     2 |
| Lithuanian          |     2 |
| Slovenian           |     2 |
| Cornish             |     1 |
| Romanian            |     1 |
| Slovak              |     1 |
| Scots               |     1 |
| Sanskrit            |     1 |

#### How to use

There are a few different ways to use the model. To run the model locally the easiest option is to use the 🤗 Transformers [`pipelines`](https://huggingface.co/transformers/main_classes/pipelines.html): 

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
tokenizer = AutoTokenizer.from_pretrained("davanstrien/bl-books-genre")
model = AutoModelForSequenceClassification.from_pretrained("davanstrien/bl-books-genre")
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
classifier("Oliver Twist")
```

This will return a dictionary with our predicted label and score
```
[{'label': 'Fiction', 'score': 0.9980145692825317}]
```

If you intend to use this model beyond initial experimentation, it is highly recommended to create some data to validate the model's predictions.  As the model was trained on a specific corpus of books titles, it is also likely to be beneficial to fine-tune the model if you want to run it across a collection of book titles that differ from those in the training corpus. 


## Training data

The training data was created using the [Zooniverse platform](zooniverse.org/) and the annotations were done by cataloguers from the [British Library](https://www.bl.uk/). [Snorkel](https://github.com/snorkel-team/snorkel) was used to expand on this original training data through various labelling functions. As a result, some of the labels are *not* generated by a human. More information on the process of creating the annotations can be found [here](https://github.com/Living-with-machines/genre-classification)

## Training procedure
The model was trained using the [`blurr`](https://github.com/ohmeow/blurr) library. A notebook showing the training process can be found in [Predicting Genre with Machine Learning](https://github.com/Living-with-machines/genre-classification).

## Eval results

The results of the model on a held-out training set are:

```
              precision    recall  f1-score   support

     Fiction       0.88      0.97      0.92       296
 Non-Fiction       0.98      0.93      0.95       554

    accuracy                           0.94       850
   macro avg       0.93      0.95      0.94       850
weighted avg       0.95      0.94      0.94       850
```

As discussed briefly in the bias and limitation sections of the model these results should be treated with caution.  **
---
tags:
- text-classification
- fastai
library_name: fastai
datasets:
- blbooksgenre
widget:
- text: "Poems on various subjects. Whereto is prefixed a short essay on the structure of English verse"
- text: "Two Centuries of Soho: its institutions, firms, and amusements. By the Clergy of St. Anne's, Soho, J. H. Cardwell ... H. B. Freeman ... G. C. Wilton ... assisted by other contributors, etc"
- text: "The Adventures of Oliver Twist. [With plates.]"
---

## Model description

This model is intended to predict, from the title of a book, whether it is 'fiction' or 'non-fiction'.

This model was trained on data created from the Digitised printed books (18th-19th Century) book collection. The datasets in this collection are comprised and derived from 49,455 digitised books (65,227 volumes), mainly from the 19th Century. This dataset is dominated by English language books and includes books in several other languages in much smaller numbers. 

This model was originally developed for use as part of the Living with Machines project to be able to 'segment' this large dataset of books into different categories based on a 'crude' classification of genre i.e. whether the title was `fiction` or `non-fiction`.

The model's training data (discussed more below) primarily consists of 19th Century book titles from the British Library Digitised printed books (18th-19th century) collection. These books have been catalogued according to British Library cataloguing practices. The model is likely to perform worse on any book titles from earlier or later periods. While the model is multilingual, it has training data in non-English book titles; these appear much less frequently.

## How to use

To use this within fastai, first [install](https://docs.fast.ai/#Installing) version 2 of the fastai library. You can load directly from the Hugging Face hub using the [`huggingface_hub`](https://github.com/huggingface/huggingface_hub) library. 

```python
from fastai import load_learner
from huggingface_hub import hf_hub_download
learn = load_learner(
    hf_hub_download('davanstrien/bl-books-genre-fastai', filename="model.pkl")
    )
learn.predict("Oliver Twist")
```

## Limitations and bias

The model was developed based on data from the British Library's Digitised printed books (18th-19th Century) collection. This dataset is not representative of books from the period covered with biases towards certain types (travel) and a likely absence of books that were difficult to digitise.

The formatting of the British Library books corpus titles may differ from other collections, resulting in worse performance on other collections. It is recommended to evaluate the performance of the model before applying it to your own data. Likely, this model won't perform well for contemporary book titles without further fine-tuning.

## Training data

The training data was created using the Zooniverse platform. British Library cataloguers carried out the majority of the annotations used as training data. More information on the process of creating the training data will be available soon. 

### Training procedure

Model training was carried out using the fastai library version 2.5.2. 

The notebook using for training the model is available at: https://github.com/Living-with-machines/genre-classification

## Eval result

The model was evaluated on a held out test set:
```
             precision    recall  f1-score   support

     Fiction       0.91      0.88      0.90       296
 Non-fiction       0.94      0.95      0.95       554

    accuracy                           0.93       850
   macro avg       0.93      0.92      0.92       850
weighted avg       0.93      0.93      0.93       850
```


---
language: nl
license: mit
datasets:
- dbrd
model-index:
- name: robbertje-merged-dutch-sentiment
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: dbrd
      type: sentiment-analysis
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9294064748201439
widget:
- text: "Ik erken dat dit een boek is, daarmee is alles gezegd."
- text: "Prachtig verhaal, heel mooi verteld en een verrassend einde... Een topper!"
thumbnail: "https://github.com/iPieter/robbertje/raw/master/images/robbertje_logo_with_name.png"
tags:
- Dutch
- Flemish
- RoBERTa
- RobBERT
---

<p align="center"> 
    <img src="https://github.com/iPieter/robbertje/raw/master/images/robbertje_logo_with_name.png" alt="RobBERTje: A collection of distilled Dutch models" width="75%">
 </p>

# RobBERTje finetuned for sentiment analysis on DBRD

This is a finetuned model based on [RobBERTje (merged)](https://huggingface.co/DTAI-KULeuven/robbertje-1-gb-non-shuffled). We used [DBRD](https://huggingface.co/datasets/dbrd), which consists of book reviews from [hebban.nl](hebban.nl). Hence our example sentences about books. We did some limited experiments to test if this also works for other domains, but this was not exactly amazing. 

We released a distilled model and a `base`-sized model. Both models perform quite well, so there is only a slight performance tradeoff:


| Model          | Identifier                                                             | Layers | #Params.  | Accuracy  |
|----------------|------------------------------------------------------------------------|--------|-----------|-----------|
| RobBERT (v2)   | [`DTAI-KULeuven/robbert-v2-dutch-sentiment`](https://huggingface.co/DTAI-KULeuven/robbert-v2-dutch-sentiment)    | 12     | 116 M     |93.3*      | 
| RobBERTje - Merged (p=0.5)| [`DTAI-KULeuven/robbertje-merged-dutch-sentiment`](https://huggingface.co/DTAI-KULeuven/robbertje-merged-dutch-sentiment) | 6 | 74 M      |92.9       |

*The results of RobBERT are of a different run than the one reported in the paper.

# Training data and setup
We used the [Dutch Book Reviews Dataset (DBRD)](https://huggingface.co/datasets/dbrd) from van der Burgh et al. (2019).
Originally, these reviews got a five-star rating, but this has been converted to positive (⭐️⭐️⭐️⭐️ and ⭐️⭐️⭐️⭐️⭐️), neutral (⭐️⭐️⭐️) and negative (⭐️ and ⭐️⭐️). 
We used 19.5k reviews for the training set, 528 reviews for the validation set and 2224 to calculate the final accuracy.

The validation set was used to evaluate a random hyperparameter search over the learning rate, weight decay and gradient accumulation steps. 
The full training details are available in [`training_args.bin`](https://huggingface.co/DTAI-KULeuven/robbert-v2-dutch-sentiment/blob/main/training_args.bin) as a binary PyTorch file. 

# Limitations and biases
- The domain of the reviews is limited to book reviews.
- Most authors of the book reviews were women, which could have caused [a difference in performance for reviews written by men and women](https://www.aclweb.org/anthology/2020.findings-emnlp.292). 

## Credits and citation

This project is created by [Pieter Delobelle](https://people.cs.kuleuven.be/~pieter.delobelle), [Thomas Winters](https://thomaswinters.be) and [Bettina Berendt](https://people.cs.kuleuven.be/~bettina.berendt/).
If you would like to cite our paper or models, you can use the following BibTeX:

```
@article{Delobelle_Winters_Berendt_2021,
	title        = {RobBERTje: A Distilled Dutch BERT Model},
	author       = {Delobelle, Pieter and Winters, Thomas and Berendt, Bettina},
	year         = 2021,
	month        = {Dec.},
	journal      = {Computational Linguistics in the Netherlands Journal},
	volume       = 11,
	pages        = {125–140},
	url          = {https://www.clinjournal.org/clinj/article/view/131}
}


@inproceedings{delobelle2020robbert,
    title = "{R}ob{BERT}: a {D}utch {R}o{BERT}a-based {L}anguage {M}odel",
    author = "Delobelle, Pieter  and
      Winters, Thomas  and
      Berendt, Bettina",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.292",
    doi = "10.18653/v1/2020.findings-emnlp.292",
    pages = "3255--3265"
}
```
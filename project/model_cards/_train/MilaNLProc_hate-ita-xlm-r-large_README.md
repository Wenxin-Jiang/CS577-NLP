---
language: it
license: gpl-3.0
tags:
- text classification
- abusive language
- hate speech
- offensive language

widget:
- text: "Ci sono dei bellissimi capibara!"
  example_title: "Hate Speech Classification 1"
- text: "Sei una testa di cazzo!!"
  example_title: "Hate Speech Classification 2"
- text: "Ti odio!"
  example_title: "Hate Speech Classification 3"


---



#
[Debora Nozza](http://dnozza.github.io/) •
[Federico Bianchi](https://federicobianchi.io/) •
[Giuseppe Attanasio](https://gattanasio.cc/)


# HATE-ITA Large 
HATE-ITA is a binary hate speech classification model for Italian social media text.

<img src="https://raw.githubusercontent.com/MilaNLProc/hate-ita/main/hateita.png?token=GHSAT0AAAAAABTEBAJ4PNDWAMU3KKIGUOCSYWG4IBA" width="200">

## Abstract

Online hate speech is a dangerous phenomenon that can (and should) be promptly counteracted properly. While Natural Language Processing has been successfully used for the purpose, many of the research efforts are directed toward the English language. This choice severely limits the classification power in non-English languages. In this paper, we test several learning frameworks for identifying hate speech in Italian text. We release **HATE-ITA, a set of multi-language models trained on a large set of English data and available Italian datasets**. HATE-ITA performs better than mono-lingual models and seems to adapt well also on language-specific slurs. We believe our findings will encourage research in other mid-to-low resource communities and provide a valuable benchmarking tool for the Italian community.

## Model

This model is the fine-tuned version of the [XLM-RoBERTa-large](https://huggingface.co/xlm-roberta-large) model. 

| Model                       | Download |
| ------                      | -------------------------|
| `hate-ita` | [Link](https://huggingface.co/MilaNLProc/hate-ita) |
| `hate-ita-xlm-r-base`   | [Link](https://huggingface.co/MilaNLProc/hate-ita-xlm-r-base) |
| `hate-ita-xlm-r-large`   | [Link](https://huggingface.co/MilaNLProc/hate-ita-xlm-r-large) |



## Usage

```python
from transformers import pipeline
classifier = pipeline("text-classification",model='MilaNLProc/hate-ita-xlm-r-large',top_k=2)
prediction = classifier("ti odio")
print(prediction)
```

## Citation
Please use the following BibTeX entry if you use this model in your project:
```
@inproceedings{nozza-etal-2022-hate-ita,
    title = {{HATE-ITA}: Hate Speech Detection in Italian Social Media Text},
    author = "Nozza, Debora and Bianchi, Federico and Attanasio, Giuseppe",
    booktitle = "Proceedings of the 6th Workshop on Online Abuse and Harms",
    year = "2022",
    publisher = "Association for Computational Linguistics"
}
```

## Ethical Statement
While promising, the results in this work should not be interpreted as a definitive assessment of the performance of hate speech detection in Italian. We are unsure if our model can maintain a stable and fair precision across the different targets and categories. HATE-ITA might overlook some sensible details, which practitioners should treat with care. 


## License 
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
---
language: it

tags:
- sentiment
- Italian
---

# FEEL-IT: Emotion and Sentiment Classification for the Italian Language

## FEEL-IT Python Package

You can find the package that uses this model for emotion and sentiment classification **[here](https://github.com/MilaNLProc/feel-it)** it is meant to be a very simple interface over HuggingFace models.

## License

Users should refer to the [following license](https://developer.twitter.com/en/developer-terms/commercial-terms)

## Abstract

Sentiment analysis is a common task to understand people's reactions online. Still, we often need more nuanced information: is the post negative because the user is angry or because they are sad?

An abundance of approaches has been introduced for tackling both tasks. However, at least for Italian, they all treat only one of the tasks at a time. We introduce *FEEL-IT*, a novel benchmark corpus of Italian Twitter posts annotated with four basic emotions: **anger, fear, joy, sadness**. By collapsing them, we can also do **sentiment analysis**. We evaluate our corpus on benchmark datasets for both emotion and sentiment classification, obtaining competitive results.

We release an [open-source Python library](https://github.com/MilaNLProc/feel-it), so researchers can use a model trained on FEEL-IT for inferring both sentiments and emotions from Italian text.

| Model                       | Download |
| ------                      | -------------------------|
| `feel-it-italian-sentiment` | [Link](https://huggingface.co/MilaNLProc/feel-it-italian-sentiment) |
| `feel-it-italian-emotion`   | [Link](https://huggingface.co/MilaNLProc/feel-it-italian-emotion) |


## Model

The *feel-it-italian-sentiment* model performs **sentiment analysis** on Italian. We fine-tuned the [UmBERTo model](https://huggingface.co/Musixmatch/umberto-commoncrawl-cased-v1) on our new dataset (i.e., FEEL-IT) obtaining state-of-the-art performances on different benchmark corpora.

## Data

Our data has been collected by annotating tweets from a broad range of topics. In total, we have 2037 tweets annotated with an emotion label. More details can be found in our paper (https://aclanthology.org/2021.wassa-1.8/).

## Performance

We evaluate our performance using [SENTIPOLC16 Evalita](http://www.di.unito.it/~tutreeb/sentipolc-evalita16/). We collapsed the FEEL-IT classes into 2 by mapping joy to the *positive* class and anger, fear and sadness into the *negative* class. We compare three different experimental configurations training on FEEL-IT, SENTIPOLC16, or both by testing on the SENTIPOLC16 test set.
The results show that training on FEEL-IT can provide better results on the SENTIPOLC16 test set than those that can be obtained with the SENTIPOLC16 training set.

| Training Dataset | Macro-F1 | Accuracy
| ------ | ------ |------ |
| SENTIPOLC16 | 0.80 | 0.81 |
| FEEL-IT | **0.81** | **0.84**  |
| FEEL-IT+SentiPolc | 0.81 | 0.82

## Usage

```python
from transformers import pipeline
classifier = pipeline("text-classification",model='MilaNLProc/feel-it-italian-sentiment',top_k=2)
prediction = classifier("Oggi sono proprio contento!")
print(prediction)
```

## Citation
Please use the following bibtex entry if you use this model in your project:
```
@inproceedings{bianchi2021feel,
    title = {{"FEEL-IT: Emotion and Sentiment Classification for the Italian Language"}},
    author = "Bianchi, Federico and Nozza, Debora and Hovy, Dirk",
    booktitle = "Proceedings of the 11th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis",
    year = "2021",
    publisher = "Association for Computational Linguistics",
}
```
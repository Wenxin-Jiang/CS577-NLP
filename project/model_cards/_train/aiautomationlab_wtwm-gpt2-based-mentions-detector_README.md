
---
language: 
  - de
tags:
  - text-classication
license: mit
metrics:
  - precision
  - recall
  - f1
widget:
- text: "Im Artikel wird leider nicht erwähnt, inwieweit und ob dadurch Natur zerstört werden muss."
---

# WTWM Newsroom Mentions Detector

Please node that this model originates from the ["What's there, what's missing"](https://interaktiv.br.de/ai-detect-newsroom-mentions-in-comments/) collaboration of [AI & Automation Labl of Bayerischer Rundfunk (BR hereafter)](https://www.br.de/extra/ai-automation-lab/index.html) and [Mitteldeutscher Rundfunk (mdr hereafter)](https://www.mdr.de/) as well as [ida](https://idalab.de/). The collaboration took place during the [JournalismAI fellowship '22](https://www.lse.ac.uk/media-and-communications/polis/JournalismAI/Fellowship-Programme) (see chapter **The fellowship** below). The model presented is part of the the documenation of the half year of project time. The related technical framework can be found a [github](https://github.com/br-data/wtwm-topic-modelling).

## The task

This is a model for the task of classifying whether or not a articles comment addresses the moderation team/authors of the media house that published the article. In this prototype stage the media houses are Bayerischer Rundfunk and Mitteldeutscher Rundfunk.

This classification task is implemented as a binary classification into:

label 0: the comment holds no mention

label 1: the comment addresses the moderation team/authors of the media house

We decided to use [german-gpt2](https://huggingface.co/dbmdz/german-gpt2) by MDZ of Bayerische Staatsbibliothek as the foundation model.

**This model is still work in progress and might be updated in the future.**


## Dataset & preprocessing

This model was finetuned on a corpus of 18.860 user comments with a share of user comments from BR and mdr websites and social media channels. The ratio of comments without mentions and with mentions is 92% to 8%. With the initial annotated data the share of comments with mentions was 2% of the data. To run the first round of training during the time of the [JournalismAI fellowship '22](https://www.lse.ac.uk/media-and-communications/polis/JournalismAI/Fellowship-Programme), we decided to augment the corpus by 1421 generated comments with mentions. The generated comments were annotated the same way as the initial data.
Please note, that the generated comments are merely meant to kick off the training of the prototype model. Retraining of the model in later iterations of our system will ignore the generated comments and solely depend on authentic comments.

The preprocessing of the data included:
- remove linebreaks
- remove html tags
- remove emojis
- remove formatting fragments (e.g. "---------", "......")
- remove gaps (~ two or more adjacent spaces)
- strip comments for whitespaces at the begin and end of the corpus

We advice to perform the same preprocessing steps when working with the mode.

## Training 

After multiple test runs of finetuning the present model was further trained using the following parameters:
- foundation_model: [german-gpt2](https://huggingface.co/dbmdz/german-gpt2)
- num_train_epochs: 4
- learning_rate: 2e-7
- weight_decay: 0.1
- metric_for_best_model: precision

### Example: Direct model evaluation

```python

from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
)

comment = "The preprocessed comment to classify"
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForSequenceClassification.from_pretrained(model_path)
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

result = pipe(comment)
label = result[0]["label"]
if label == "LABEL_1":
    has_mention = True
elif label == "LABEL_0":
    has_mention = False

print(f"Comment includes mention {has_mention}")
```

## Limitations

Clearly, the amount of training data was to small for a state of the art result. This can be seen in the evaluation chapter. Future rounds of retraining have to be performed. For the sake of completeness we publish this model here within [the projects documentation](https://interaktiv.br.de/ai-detect-newsroom-mentions-in-comments/).

An analysis of possible biases reproduced by the present model, regardless of whether they originate from our finetuning or the underlying gpt2 model, is beyond the scope of this work. We assume that biases exist within the model and an analysis will be a task for future work


## Evaluation
The model was evaluated on a held-out test set consisting of 10% of the corpus.


### Quantitative
As a general training approach we decided to optimize for the precision of the detection of the mentions in comments. This strategy best fits the high speed moderation challenge the moderation team's faces in everyday work. Our goal is to focus their attention only to comments that are very likely to contain a mention and not to confuse the moderation team with comments that don't contain mentions.  

In addition we decided not to include the accuracy score in our evaluation because its high values are misleading for the interpretation of the evaluation. This effect is because of the strong imbalance in the distribution between comments with and without mentions. E.g., a classification that would label each comment as without mentions would receive a accuracy of 0.92 percentage points of accuracy.

| mentions total | mentions predicted | precision | recall | f1 |
|-|-|-|-|-|
| 148 | 130 | 0.74 | 0.65 | 0.69 |

### Qualitative

A qualitative evaluation conducted by members of the BR and mdr in the daily context of the comment moderation live system resulted in a 88% human agreement on the publish comments.

## Conclusion

The qualitative evaluation of [this project](https://interaktiv.br.de/ai-detect-newsroom-mentions-in-comments/) makes us confident that the mediocre quantitative results can be overcome with a sufficiently large corpus and that the overall prototype of the project can be a usefull addition to comment moderation tools.


## The fellowship

[JournalismAI](https://www.lse.ac.uk/media-and-communications/polis/JournalismAI) is a project of [Polis](https://www.lse.ac.uk/media-and-communications/polis) – the journalism think-tank at the London School of Economics and Political Science – and it’s sponsored by the [Google News Initiative](https://newsinitiative.withgoogle.com/)). If you want to know more about the Fellowship and the other JournalismAI activities, [sign up for the newsletter](https://mailchi.mp/lse.ac.uk/journalismai) or get in touch with the team via hello@journalismai.info


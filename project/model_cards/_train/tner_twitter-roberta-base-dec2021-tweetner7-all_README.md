---
datasets:
- tner/tweetner7
metrics:
- f1
- precision
- recall
model-index:
- name: tner/twitter-roberta-base-dec2021-tweetner7-all
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tner/tweetner7
      type: tner/tweetner7
      args: tner/tweetner7
    metrics:
    - name: F1 (test_2021)
      type: f1
      value: 0.6447001005249637
    - name: Precision (test_2021)
      type: precision
      value: 0.6234607906675308
    - name: Recall (test_2021)
      type: recall
      value: 0.6674375578168362
    - name: Macro F1 (test_2021)
      type: f1_macro
      value: 0.5982200308213212
    - name: Macro Precision (test_2021)
      type: precision_macro
      value: 0.576608821080324
    - name: Macro Recall (test_2021)
      type: recall_macro
      value: 0.622268182336741
    - name: Entity Span F1 (test_2021)
      type: f1_entity_span
      value: 0.7793353811784417
    - name: Entity Span Precision (test_2020)
      type: precision_entity_span
      value: 0.7536184921149276
    - name: Entity Span Recall (test_2021)
      type: recall_entity_span
      value: 0.8068694344859488
    - name: F1 (test_2020)
      type: f1
      value: 0.6582010582010582
    - name: Precision (test_2020)
      type: precision
      value: 0.671343766864544
    - name: Recall (test_2020)
      type: recall
      value: 0.6455630513751947
    - name: Macro F1 (test_2020)
      type: f1_macro
      value: 0.619090119256277
    - name: Macro Precision (test_2020)
      type: precision_macro
      value: 0.6309214005692869
    - name: Macro Recall (test_2020)
      type: recall_macro
      value: 0.6088158080350003
    - name: Entity Span F1 (test_2020)
      type: f1_entity_span
      value: 0.7647525800476317
    - name: Entity Span Precision (test_2020)
      type: precision_entity_span
      value: 0.7802375809935205
    - name: Entity Span Recall (test_2020)
      type: recall_entity_span
      value: 0.7498702646600934

pipeline_tag: token-classification
widget:
- text: "Get the all-analog Classic Vinyl Edition of `Takin' Off` Album from {@herbiehancock@} via {@bluenoterecords@} link below: {{URL}}"
  example_title: "NER Example 1"
---
# tner/twitter-roberta-base-dec2021-tweetner7-all

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-dec2021](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021) on the 
[tner/tweetner7](https://huggingface.co/datasets/tner/tweetner7) dataset (`train_all` split).
Model fine-tuning is done via [T-NER](https://github.com/asahi417/tner)'s hyper-parameter search (see the repository
for more detail). It achieves the following results on the test set of 2021:
- F1 (micro): 0.6447001005249637
- Precision (micro): 0.6234607906675308
- Recall (micro): 0.6674375578168362
- F1 (macro): 0.5982200308213212
- Precision (macro): 0.576608821080324
- Recall (macro): 0.622268182336741



The per-entity breakdown of the F1 score on the test set are below:
- corporation: 0.5048128342245989
- creative_work: 0.45297029702970293
- event: 0.46761313220940554
- group: 0.6009661835748793
- location: 0.6592252133946159
- person: 0.8302430243024302
- product: 0.6717095310136157 

For F1 scores, the confidence interval is obtained by bootstrap as below:
- F1 (micro): 
    - 90%: [0.6358921767926183, 0.6542958612061787]
    - 95%: [0.6341987223616053, 0.6560992650244356] 
- F1 (macro): 
    - 90%: [0.6358921767926183, 0.6542958612061787]
    - 95%: [0.6341987223616053, 0.6560992650244356] 

Full evaluation can be found at [metric file of NER](https://huggingface.co/tner/twitter-roberta-base-dec2021-tweetner7-all/raw/main/eval/metric.json) 
and [metric file of entity span](https://huggingface.co/tner/twitter-roberta-base-dec2021-tweetner7-all/raw/main/eval/metric_span.json).

### Usage
This model can be used through the [tner library](https://github.com/asahi417/tner). Install the library via pip.   
```shell
pip install tner
```
[TweetNER7](https://huggingface.co/datasets/tner/tweetner7) pre-processed tweets where the account name and URLs are 
converted into special formats (see the dataset page for more detail), so we process tweets accordingly and then run the model prediction as below.  

```python
import re
from urlextract import URLExtract
from tner import TransformersNER

extractor = URLExtract()

def format_tweet(tweet):
    # mask web urls
    urls = extractor.find_urls(tweet)
    for url in urls:
        tweet = tweet.replace(url, "{{URL}}")
    # format twitter account
    tweet = re.sub(r"\b(\s*)(@[\S]+)\b", r'\1{\2@}', tweet)
    return tweet


text = "Get the all-analog Classic Vinyl Edition of `Takin' Off` Album from @herbiehancock via @bluenoterecords link below: http://bluenote.lnk.to/AlbumOfTheWeek"
text_format = format_tweet(text)
model = TransformersNER("tner/twitter-roberta-base-dec2021-tweetner7-all")
model.predict([text_format])
```
It can be used via transformers library but it is not recommended as CRF layer is not supported at the moment.

### Training hyperparameters

The following hyperparameters were used during training:
 - dataset: ['tner/tweetner7']
 - dataset_split: train_all
 - dataset_name: None
 - local_dataset: None
 - model: cardiffnlp/twitter-roberta-base-dec2021
 - crf: True
 - max_length: 128
 - epoch: 30
 - batch_size: 32
 - lr: 1e-05
 - random_seed: 0
 - gradient_accumulation_steps: 1
 - weight_decay: 1e-07
 - lr_warmup_step_ratio: 0.3
 - max_grad_norm: 1

The full configuration can be found at [fine-tuning parameter file](https://huggingface.co/tner/twitter-roberta-base-dec2021-tweetner7-all/raw/main/trainer_config.json).

### Reference
If you use the model, please cite T-NER paper and TweetNER7 paper.
- T-NER
```

@inproceedings{ushio-camacho-collados-2021-ner,
    title = "{T}-{NER}: An All-Round Python Library for Transformer-based Named Entity Recognition",
    author = "Ushio, Asahi  and
      Camacho-Collados, Jose",
    booktitle = "Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations",
    month = apr,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.eacl-demos.7",
    doi = "10.18653/v1/2021.eacl-demos.7",
    pages = "53--62",
    abstract = "Language model (LM) pretraining has led to consistent improvements in many NLP downstream tasks, including named entity recognition (NER). In this paper, we present T-NER (Transformer-based Named Entity Recognition), a Python library for NER LM finetuning. In addition to its practical utility, T-NER facilitates the study and investigation of the cross-domain and cross-lingual generalization ability of LMs finetuned on NER. Our library also provides a web app where users can get model predictions interactively for arbitrary text, which facilitates qualitative model evaluation for non-expert programmers. We show the potential of the library by compiling nine public NER datasets into a unified format and evaluating the cross-domain and cross- lingual performance across the datasets. The results from our initial experiments show that in-domain performance is generally competitive across datasets. However, cross-domain generalization is challenging even with a large pretrained LM, which has nevertheless capacity to learn domain-specific features if fine- tuned on a combined dataset. To facilitate future research, we also release all our LM checkpoints via the Hugging Face model hub.",
}

```
- TweetNER7
```

@inproceedings{ushio-etal-2022-tweet,
    title = "{N}amed {E}ntity {R}ecognition in {T}witter: {A} {D}ataset and {A}nalysis on {S}hort-{T}erm {T}emporal {S}hifts",
    author = "Ushio, Asahi  and
        Neves, Leonardo  and
        Silva, Vitor  and
        Barbieri, Francesco. and
        Camacho-Collados, Jose",
    booktitle = "The 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing",
    month = nov,
    year = "2022",
    address = "Online",
    publisher = "Association for Computational Linguistics",
}

```



---
license: apache-2.0
language: en
datasets:
- Jzuluaga/uwb_atcc
tags:
- text
- sequence-classification
- en-atc
- en
- generated_from_trainer
- bert
- bertraffic
metrics:
- Precision
- Recall
- Accuracy
- F1
widget:
- text: "csa two nine six startup approved mike current qnh one zero one eight time check one seven"
- text: "swiss four eight seven november runway three one cleared for takeoff wind one three zero degrees seven knots"
- text: "lufthansa five yankee victor runway one three clear to land wind zero seven zero degrees"
- text: "austrian seven one zulu hello to you reduce one six zero knots"
- text: "sky travel one nine two approaching holding point three one ready for departure"
- name: bert-base-speaker-role-atc-en-uwb-atcc
  results:
  - task:
        type: token-classification
        name: chunking
    dataset:
        type: Jzuluaga/uwb_atcc
        name: UWB-ATCC corpus (Air Traffic Control Communications)
        config: test
        split: test
    metrics:
    - type: F1
      value: 0.87
      name: TEST F1 (macro)
      verified: False
    - type: Accuracy
      value: 0.91
      name: TEST Accuracy
      verified: False
    - type: Precision
      value: 0.86
      name: TEST Precision (macro)
      verified: False
    - type: Recall
      value: 0.88
      name: TEST Recall (macro)
      verified: False   
    - type: Jaccard Error Rate
      value: 0.169
      name: TEST Jaccard Error Rate
      verified: False   
---

# bert-base-speaker-role-atc-en-uwb-atcc

This model allow to detect speaker roles based on text. Normally, this task is done on the acoustic level. However, we propose to perform this task on the text level.
We solve this challenge by performing speaker role with a BERT model. We fine-tune it on the sequence classification task. 

For instance:

- Utterance 1: **lufthansa six two nine charlie tango report when established**
- Utterance 2: **report when established lufthansa six two nine charlie tango**

Based on that, could you tell the speaker role? Is it Utterance 1 air traffic controller or pilot? 

Check the inference API (there are 5 examples)! 

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [UWB-ATCC corpus](https://huggingface.co/datasets/Jzuluaga/uwb_atcc). 

<a href="https://github.com/idiap/atco2-corpus">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>

It achieves the following results on the evaluation set:
- Loss: 0.6191
- Accuracy: 0.9103
- Precision: 0.9239
- Recall: 0.9161
- F1: 0.9200

**Paper**: [ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications](https://arxiv.org/abs/2211.04054)

Authors: Juan Zuluaga-Gomez, Karel Veselý, Igor Szöke, Petr Motlicek, Martin Kocour, Mickael Rigault, Khalid Choukri, Amrutha Prasad and others

Abstract: Personal assistants, automatic speech recognizers and dialogue understanding systems are becoming more critical in our interconnected digital world. A clear example is air traffic control (ATC) communications. ATC aims at guiding aircraft and controlling the airspace in a safe and optimal manner. These voice-based dialogues are carried between an air traffic controller (ATCO) and pilots via very-high frequency radio channels. In order to incorporate these novel technologies into ATC (low-resource domain), large-scale annotated datasets are required to develop the data-driven AI systems. Two examples are automatic speech recognition (ASR) and natural language understanding (NLU). In this paper, we introduce the ATCO2 corpus, a dataset that aims at fostering research on the challenging ATC field, which has lagged behind due to lack of annotated data. The ATCO2 corpus covers 1) data collection and pre-processing, 2) pseudo-annotations of speech data, and 3) extraction of ATC-related named entities. The ATCO2 corpus is split into three subsets. 1) ATCO2-test-set corpus contains 4 hours of ATC speech with manual transcripts and a subset with gold annotations for named-entity recognition (callsign, command, value). 2) The ATCO2-PL-set corpus consists of 5281 hours of unlabeled ATC data enriched with automatic transcripts from an in-domain speech recognizer, contextual information, speaker turn information, signal-to-noise ratio estimate and English language detection score per sample. Both available for purchase through ELDA at this http URL. 3) The ATCO2-test-set-1h corpus is a one-hour subset from the original test set corpus, that we are offering for free at this url: https://www.atco2.org/data. We expect the ATCO2 corpus will foster research on robust ASR and NLU not only in the field of ATC communications but also in the general research community. 

Code — GitHub repository: https://github.com/idiap/atco2-corpus

## Intended uses & limitations

This model was fine-tuned on air traffic control data. We don't expect that it keeps the same performance on some others datasets where BERT was pre-trained or fine-tuned.

## Training and evaluation data

See Table 7 (page 19) in our paper: [ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications](https://arxiv.org/abs/2211.04054). We described there the data used to fine-tune our sequence classification model. 

- We use the UWB-ATCC corpus to fine-tune this model. You can download the raw data here: https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0
- However, do not worry, we have prepared a script in our repository for preparing this databases:
  - Dataset preparation folder: https://github.com/idiap/atco2-corpus/tree/main/data/databases/uwb_atcc/
  - Prepare the data: https://github.com/idiap/atco2-corpus/blob/main/data/databases/uwb_atcc/data_prepare_uwb_atcc_corpus_other.sh

## Writing your own inference script


The snippet of code:

```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Jzuluaga/bert-base-speaker-role-atc-en-uwb-atcc")
model = AutoModelForSequenceClassification.from_pretrained("Jzuluaga/bert-base-speaker-role-atc-en-uwb-atcc")


##### Process text sample (from UWB-ATCC)
from transformers import pipeline

nlp = pipeline('text-classification', model=model, tokenizer=tokenizer)
nlp("lining up runway three one csa five bravo")

[{'label': 'pilot',
'score': 0.9998971223831177}]

```

# Cite us

If you use this code for your research, please cite our paper with:

```
@article{zuluaga2022bertraffic,
  title={BERTraffic: BERT-based Joint Speaker Role and Speaker Change Detection for Air Traffic Control Communications},
  author={Zuluaga-Gomez, Juan and Sarfjoo, Seyyed Saeed and Prasad, Amrutha and others},
  journal={IEEE Spoken Language Technology Workshop (SLT), Doha, Qatar},
  year={2022}
  }
```
and,
```
@article{zuluaga2022how,
    title={How Does Pre-trained Wav2Vec2. 0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications},
    author={Zuluaga-Gomez, Juan and Prasad, Amrutha and Nigmatulina, Iuliia and Sarfjoo, Saeed and others},
    journal={IEEE Spoken Language Technology Workshop (SLT), Doha, Qatar},
    year={2022}
  }
```
and, 
```
@article{zuluaga2022atco2,
  title={ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications},
  author={Zuluaga-Gomez, Juan and Vesel{\`y}, Karel and Sz{\"o}ke, Igor and Motlicek, Petr and others},
  journal={arXiv preprint arXiv:2211.04054},
  year={2022}
}
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     | 
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 3.36  | 500  | 0.2346          | 0.9207   | 0.9197    | 0.9413 | 0.9303 |
| 0.2212        | 6.71  | 1000 | 0.3161          | 0.9046   | 0.9260    | 0.9027 | 0.9142 |
| 0.2212        | 10.07 | 1500 | 0.4337          | 0.9065   | 0.9191    | 0.9144 | 0.9167 |
| 0.0651        | 13.42 | 2000 | 0.4743          | 0.9178   | 0.9249    | 0.9295 | 0.9272 |
| 0.0651        | 16.78 | 2500 | 0.5538          | 0.9103   | 0.9196    | 0.9211 | 0.9204 |
| 0.0296        | 20.13 | 3000 | 0.6191          | 0.9103   | 0.9239    | 0.9161 | 0.9200 |

### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2

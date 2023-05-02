---
license: apache-2.0
language: en
datasets:
- Jzuluaga/uwb_atcc
tags:
- text
- token-classification
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
- Jaccard Error Rate
widget:
- text: "lining up runway three one csa five bravo easy five three kilo romeo contact ruzyne ground one two one decimal nine good bye"
- text: "csa seven three two zero so change of taxi quality eight nine sierra we need to full length britair five nine zero bravo contact ruzyne ground one two one decimal nine good bye"
- text: "swiss four six one foxtrot line up runway three one and wait one two one nine csa four yankee alfa"
- text: "tower klm five five tango ils three one wizz air four papa uniform tower roger"
model-index:
- name: bert-base-token-classification-for-atc-en-uwb-atcc
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

# bert-base-token-classification-for-atc-en-uwb-atcc

This model allow to detect speaker roles and speaker changes based on text. Normally, this task is done on the acoustic level. However, we propose to perform this task on the text level.
We solve this challenge by performing speaker role and change detection with a BERT model. We fine-tune it on the chunking task (token-classification). 

For instance:

- Speaker 1: **lufthansa six two nine charlie tango report when established**
- Speaker 2: **report when established lufthansa six two nine charlie tango**

Based on that, could you tell the speaker role? Is it speaker 1 air traffic controller or pilot? 

Also, if you have a recording with 2 or more speakers, like this: 

- Recording with 2 or more segments: **report when established lufthansa six two nine charlie tango lufthansa six two nine charlie tango report when established**

could you tell when the first speaker ends and when the second starts? This is basically diarization plus speaker role detection.

Check the inference API (there are3 examples)! 


This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [UWB-ATCC corpus](https://huggingface.co/datasets/Jzuluaga/uwb_atcc). 

<a href="https://github.com/idiap/bert-text-diarization-atc">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>

It achieves the following results on the evaluation set:
- Loss: 0.0098
- Precision: 0.9760
- Recall: 0.9741
- F1: 0.9750
- Accuracy: 0.9965


Paper: [BERTraffic: BERT-based Joint Speaker Role and Speaker Change Detection for Air Traffic Control Communications](https://arxiv.org/abs/2110.05781).

Authors: Juan Zuluaga-Gomez, Seyyed Saeed Sarfjoo, Amrutha Prasad, Iuliia Nigmatulina, Petr Motlicek, Karel Ondrej, Oliver Ohneiser, Hartmut Helmke

Abstract: Automatic speech recognition (ASR) allows transcribing the communications between air traffic controllers (ATCOs) and aircraft pilots. The transcriptions are used later to extract ATC named entities, e.g., aircraft callsigns. One common challenge is speech activity detection (SAD) and speaker diarization (SD). In the failure condition, two or more segments remain in the same recording, jeopardizing the overall performance. We propose a system that combines SAD and a BERT model to perform speaker change detection and speaker role detection (SRD) by chunking ASR transcripts, i.e., SD with a defined number of speakers together with SRD. The proposed model is evaluated on real-life public ATC databases. Our BERT SD model baseline reaches up to 10% and 20% token-based Jaccard error rate (JER) in public and private ATC databases. We also achieved relative improvements of 32% and 7.7% in JERs and SD error rate (DER), respectively, compared to VBx, a well-known SD system. 

Code — GitHub repository: https://github.com/idiap/bert-text-diarization-atc


## Intended uses & limitations

This model was fine-tuned on air traffic control data. We don't expect that it keeps the same performance on some others datasets where BERT was pre-trained or fine-tuned.

## Training and evaluation data

See Table 3 (page 5) in our paper:[BERTraffic: BERT-based Joint Speaker Role and Speaker Change Detection for Air Traffic Control Communications](https://arxiv.org/abs/2110.05781).. We described there the data used to fine-tune or model for speaker role and speaker change detection. 

- We use the UWB-ATCC corpus to fine-tune this model. You can download the raw data here: https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0
- However, do not worry, we have prepared a script in our repository for preparing this databases:
  - Dataset preparation folder: https://github.com/idiap/bert-text-diarization-atc/tree/main/data/databases/uwb_atcc
  - Prepare the data: https://github.com/idiap/bert-text-diarization-atc/blob/main/data/databases/uwb_atcc/data_prepare_uwb_atcc_corpus.sh
  - Get the data in the format required by HuggingFace: https://github.com/idiap/bert-text-diarization-atc/blob/main/data/databases/uwb_atcc/exp_prepare_uwb_atcc_corpus.sh


## Writing your own inference script

The snippet of code:

```python
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jzuluaga/bert-base-token-classification-for-atc-en-uwb-atcc")
model = AutoModelForTokenClassification.from_pretrained("Jzuluaga/bert-base-token-classification-for-atc-en-uwb-atcc")


##### Process text sample (from UWB-ATCC)
from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
nlp("lining up runway three one csa five bravo b easy five three kilo romeo contact ruzyne ground one two one decimal nine good bye)


[{'entity_group': 'pilot',
'score': 0.99991554,
'word': 'lining up runway three one csa five bravo b', 'start': 0, 'end': 43
},
{'entity_group': 'atco',
'score': 0.99994576,
'word': 'easy five three kilo romeo contact ruzyne ground one two one decimal nine good bye', 'start': 44, 'end': 126
}]

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 10000

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.03  | 500   | 0.2282          | 0.6818    | 0.7001 | 0.6908 | 0.9246   |
| 0.3487        | 0.06  | 1000  | 0.1214          | 0.8163    | 0.8024 | 0.8093 | 0.9631   |
| 0.3487        | 0.1   | 1500  | 0.0933          | 0.8496    | 0.8544 | 0.8520 | 0.9722   |
| 0.1124        | 0.13  | 2000  | 0.0693          | 0.8845    | 0.8739 | 0.8791 | 0.9786   |
| 0.1124        | 0.16  | 2500  | 0.0540          | 0.8993    | 0.8911 | 0.8952 | 0.9817   |
| 0.0667        | 0.19  | 3000  | 0.0474          | 0.9058    | 0.8929 | 0.8993 | 0.9857   |
| 0.0667        | 0.23  | 3500  | 0.0418          | 0.9221    | 0.9245 | 0.9233 | 0.9865   |
| 0.0492        | 0.26  | 4000  | 0.0294          | 0.9369    | 0.9415 | 0.9392 | 0.9903   |
| 0.0492        | 0.29  | 4500  | 0.0263          | 0.9512    | 0.9446 | 0.9479 | 0.9911   |
| 0.0372        | 0.32  | 5000  | 0.0223          | 0.9495    | 0.9497 | 0.9496 | 0.9915   |
| 0.0372        | 0.35  | 5500  | 0.0212          | 0.9530    | 0.9514 | 0.9522 | 0.9923   |
| 0.0308        | 0.39  | 6000  | 0.0177          | 0.9585    | 0.9560 | 0.9572 | 0.9933   |
| 0.0308        | 0.42  | 6500  | 0.0169          | 0.9619    | 0.9613 | 0.9616 | 0.9936   |
| 0.0261        | 0.45  | 7000  | 0.0140          | 0.9689    | 0.9662 | 0.9676 | 0.9951   |
| 0.0261        | 0.48  | 7500  | 0.0130          | 0.9652    | 0.9629 | 0.9641 | 0.9945   |
| 0.0214        | 0.51  | 8000  | 0.0127          | 0.9676    | 0.9635 | 0.9656 | 0.9953   |
| 0.0214        | 0.55  | 8500  | 0.0109          | 0.9714    | 0.9708 | 0.9711 | 0.9959   |
| 0.0177        | 0.58  | 9000  | 0.0103          | 0.9740    | 0.9727 | 0.9734 | 0.9961   |
| 0.0177        | 0.61  | 9500  | 0.0101          | 0.9768    | 0.9744 | 0.9756 | 0.9963   |
| 0.0159        | 0.64  | 10000 | 0.0098          | 0.9760    | 0.9741 | 0.9750 | 0.9965   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2

---
license: apache-2.0
language: en
datasets:
- Jzuluaga/atco2_corpus_1h
tags:
- text
- token-classification
- en-atc
- en
- generated_from_trainer
- bert
- ner-for-atc
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
model-index:
- name: bert-base-ner-atc-en-atco2-1h
  results:
  - task:
        type: token-classification
        name: ner
    dataset:
        type: Jzuluaga/atco2_corpus_1h
        name: ATCO2 corpus (Air Traffic Control Communications)
        config: test
        split: test
    metrics:
    - type: F1
      value: 0.94
      name: TEST F1 (callsign)
      verified: False
    - type: F1
      value: 0.74
      name: TEST F1 (command)
      verified: False
    - type: F1
      value: 0.81
      name: TEST F1 (value)
      verified: False     
---

# bert-base-ner-atc-en-atco2-1h

This model allow to perform named-entity recognition (NER) on air traffic control communications data. We solve this challenge by performing token classification (NER) with a BERT model. 
We fine-tune a pretrained BERT model on the ner task. 

For instance, if you have the following transcripts/gold annotations:

- **Utterance**: lufthansa three two five cleared to land runway three four left

Could you tell what are the main entities in the communication? The desired output is shown below:

- **Named-entity module output**: [call] lufthansa three two five [/call] [cmd] cleared to land [/cmd] [val] runway three four left [/val]

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [atco2_corpus_1h](https://huggingface.co/datasets/Jzuluaga/atco2_corpus_1h). 

<a href="https://github.com/idiap/atco2-corpus">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>

It achieves the following results on the development set:
- Loss: 1.4282
- Precision: 0.6195
- Recall: 0.7071
- F1: 0.6604
- Accuracy: 0.8182

**Paper**: [ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications](https://arxiv.org/abs/2211.04054)

Authors: Juan Zuluaga-Gomez, Karel Veselý, Igor Szöke, Petr Motlicek, Martin Kocour, Mickael Rigault, Khalid Choukri, Amrutha Prasad and others

Abstract: Personal assistants, automatic speech recognizers and dialogue understanding systems are becoming more critical in our interconnected digital world. A clear example is air traffic control (ATC) communications. ATC aims at guiding aircraft and controlling the airspace in a safe and optimal manner. These voice-based dialogues are carried between an air traffic controller (ATCO) and pilots via very-high frequency radio channels. In order to incorporate these novel technologies into ATC (low-resource domain), large-scale annotated datasets are required to develop the data-driven AI systems. Two examples are automatic speech recognition (ASR) and natural language understanding (NLU). In this paper, we introduce the ATCO2 corpus, a dataset that aims at fostering research on the challenging ATC field, which has lagged behind due to lack of annotated data. The ATCO2 corpus covers 1) data collection and pre-processing, 2) pseudo-annotations of speech data, and 3) extraction of ATC-related named entities. The ATCO2 corpus is split into three subsets. 1) ATCO2-test-set corpus contains 4 hours of ATC speech with manual transcripts and a subset with gold annotations for named-entity recognition (callsign, command, value). 2) The ATCO2-PL-set corpus consists of 5281 hours of unlabeled ATC data enriched with automatic transcripts from an in-domain speech recognizer, contextual information, speaker turn information, signal-to-noise ratio estimate and English language detection score per sample. Both available for purchase through ELDA at this http URL. 3) The ATCO2-test-set-1h corpus is a one-hour subset from the original test set corpus, that we are offering for free at this url: https://www.atco2.org/data. We expect the ATCO2 corpus will foster research on robust ASR and NLU not only in the field of ATC communications but also in the general research community. 

Code — GitHub repository: https://github.com/idiap/atco2-corpus


## Intended uses & limitations

This model was fine-tuned on air traffic control data. We don't expect that it keeps the same performance on some others datasets where BERT was pre-trained or fine-tuned.

## Training and evaluation data

See Table 6 (page 18) in our paper: [ATCO2 corpus: A Large-Scale Dataset for Research on Automatic Speech Recognition and Natural Language Understanding of Air Traffic Control Communications](https://arxiv.org/abs/2211.04054). We described there the data used to fine-tune our NER model. 

- We use the ATCO2 corpus to fine-tune this model. You can download a free sample here: https://www.atco2.org/data
- However, do not worry, we have prepared a script in our repository for preparing this databases: 
  - Dataset preparation folder: https://github.com/idiap/atco2-corpus/tree/main/data/databases/atco2_test_set_1h/data_prepare_atco2_corpus_other.sh
  - Get the data in the format required by HuggingFace: speaker_role/data_preparation/prepare_spkid_atco2_corpus_test_set_1h.sh

## Writing your own inference script

The snippet of code:

```python
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jzuluaga/bert-base-ner-atc-en-atco2-1h")
model = AutoModelForTokenClassification.from_pretrained("Jzuluaga/bert-base-ner-atc-en-atco2-1h")


##### Process text sample
from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
nlp("lufthansa three two five cleared to land runway three four left")

# output:
[{'entity_group': 'callsign', 'score': 0.8753265, 
'word': 'lufthansa three two five', 
'start': 0, 'end': 24},
{'entity_group': 'command', 'score': 0.99988264, 
'word': 'cleared to land', 'start': 25, 'end': 40}, 
{'entity_group': 'value', 'score': 0.9999145, 
'word': 'runway three four left', 'start': 41, 'end': 63}]

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 125.0 | 500  | 0.8692          | 0.6396    | 0.7172 | 0.6762 | 0.8307   |
| 0.2158        | 250.0 | 1000 | 1.0074          | 0.5702    | 0.6970 | 0.6273 | 0.8245   |
| 0.2158        | 375.0 | 1500 | 1.3560          | 0.6577    | 0.7374 | 0.6952 | 0.8119   |
| 0.0184        | 500.0 | 2000 | 1.3393          | 0.6182    | 0.6869 | 0.6507 | 0.8056   |
| 0.0184        | 625.0 | 2500 | 1.3528          | 0.6087    | 0.7071 | 0.6542 | 0.8213   |
| 0.0175        | 750.0 | 3000 | 1.4282          | 0.6195    | 0.7071 | 0.6604 | 0.8182   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2

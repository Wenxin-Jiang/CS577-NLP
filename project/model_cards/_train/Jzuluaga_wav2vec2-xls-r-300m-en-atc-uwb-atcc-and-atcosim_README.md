---
license: apache-2.0
language: en
datasets:
- Jzuluaga/atcosim_corpus
- Jzuluaga/uwb_atcc
tags:
- audio
- automatic-speech-recognition
- en-atc
- en
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-300m-en-atc-uwb-atcc-atcosim
  results:
  - task:
        type: automatic-speech-recognition
        name: Speech Recognition
    dataset:
        type: Jzuluaga/uwb_atcc
        name: UWB-ATCC dataset (Air Traffic Control Communications)
        config: test
        split: test
    metrics:
    - type: wer
      value: 24.96
      name: TEST WER
      verified: False
    - type: wer
      value: 17.9
      name: TEST WER (+LM)
      verified: False
  - task:
        type: automatic-speech-recognition
        name: Speech Recognition
    dataset:
        type: Jzuluaga/atcosim_corpus
        name: ATCOSIM corpus (Air Traffic Control Communications)
        config: test
        split: test
    metrics:
    - type: wer
      value: 4.09
      name: TEST WER
      verified: False
    - type: wer
      value: 2.53
      name: TEST WER (+LM)
      verified: False
      
---

# wav2vec2-xls-r-300m-en-atc-uwb-atcc-and-atcosim

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on two corpus:
- [UWB-ATCC corpus](https://huggingface.co/datasets/Jzuluaga/uwb_atcc), and
- [ATCOSIM corpus](https://huggingface.co/datasets/Jzuluaga/atcosim_corpus). 

<a href="https://colab.research.google.com/github/idiap/w2v2-air-traffic/blob/main/src/eval_xlsr_atc_model.ipynb">
    <img alt="GitHub" src="https://colab.research.google.com/assets/colab-badge.svg\">
</a>
<a href="https://github.com/idiap/w2v2-air-traffic">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>


It achieves the following results on the evaluation set (two tests sets joined together: UWB-ATCC and ATCOSIM):
- Loss: 0.5595
- Wer: 0.1687

Paper: [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822).

Authors: Juan Zuluaga-Gomez, Amrutha Prasad, Iuliia Nigmatulina, Saeed Sarfjoo, Petr Motlicek, Matthias Kleinert, Hartmut Helmke, Oliver Ohneiser, Qingran Zhan

Abstract: Recent work on self-supervised pre-training focus</b> on leveraging large-scale unlabeled speech data to build robust end-to-end (E2E)acoustic models (AM) that can be later fine-tuned on downstream tasks e.g., automatic speech recognition (ASR). Yet, few works investigated the impact on performance when the data properties substantially differ between the pre-training and fine-tuning phases, termed domain shift. We target this scenario by analyzing the robustness of Wav2Vec 2.0 and XLS-R models on downstream ASR for a completely unseen domain, air traffic control (ATC) communications. We benchmark these two models on several open-source and challenging ATC databases with signal-to-noise ratio between 5 and 20 dB. Relative word error rate (WER) reductions between 20% to 40% are obtained in comparison to hybrid-based ASR baselines by only fine-tuning E2E acoustic models with a smaller fraction of labeled data. We analyze WERs on the low-resource scenario and gender bias carried by one ATC dataset.

Code — GitHub repository: https://github.com/idiap/w2v2-air-traffic

## Usage

You can use our Google Colab notebook to run and evaluate our model: https://github.com/idiap/w2v2-air-traffic/blob/master/src/eval_xlsr_atc_model.ipynb

## Intended uses & limitations

This model was fine-tuned on air traffic control data. We don't expect that it keeps the same performance on some others datasets, e.g., LibriSpeech or CommonVoice.


## Training and evaluation data

See Table 1 (page 3) in our paper: [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822). We described there the partitions of how to use our model. 

- We use the UWB-ATCC + ATCOSIM corpus to fine-tune this model. You can download the raw data here:
  - https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0 and,
  - https://www.spsc.tugraz.at/databases-and-tools/atcosim-air-traffic-control-simulation-speech-corpus.html
- However, do not worry, we have prepared the database in `Datasets format`:
  -  Here, [UWB-ATCC corpus on HuggingFace](https://huggingface.co/datasets/Jzuluaga/uwb_atcc).
  -  Here: [ATCOSIM CORPUS on HuggingFace](https://huggingface.co/datasets/Jzuluaga/atcosim_corpus). 
- If you want to prepare a database in HuggingFace format, you can follow the data loader script in: [data_loader_atc.py](https://huggingface.co/datasets/Jzuluaga/uwb_atcc/blob/main/atc_data_loader.py).

## Writing your own inference script

If you use language model, you need to install the KenLM bindings with:

```bash
conda activate your_environment
pip install https://github.com/kpu/kenlm/archive/master.zip
```

The snippet of code:

```python
from datasets import load_dataset, load_metric, Audio
import torch
from transformers import AutoModelForCTC, Wav2Vec2Processor, Wav2Vec2ProcessorWithLM
import torchaudio.functional as F

USE_LM = False
DATASET_ID = "Jzuluaga/uwb_atcc"
MODEL_ID = "Jzuluaga/wav2vec2-xls-r-300m-en-atc-uwb-atcc-and-atcosim"

# 1. Load the dataset
# we only load the 'test' partition, however, if you want to load the 'train' partition, you can change it accordingly
uwb_atcc_corpus_test = load_dataset(DATASET_ID, "test", split="test")

# 2. Load the model
model = AutoModelForCTC.from_pretrained(MODEL_ID)

# 3. Load the processors, we offer support with LM, which should yield better resutls
if USE_LM:
    processor = Wav2Vec2ProcessorWithLM.from_pretrained(MODEL_ID)
else:
    processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
# 4. Format the test sample
sample = next(iter(uwb_atcc_corpus_test))
file_sampling_rate = sample['audio']['sampling_rate']
# resample if neccessary
if file_sampling_rate != 16000:
    resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), file_sampling_rate, 16000).numpy()
else:
    resampled_audio = torch.tensor(sample["audio"]["array"]).numpy()
input_values = processor(resampled_audio, return_tensors="pt").input_values

# 5. Run the forward pass in the model
with torch.no_grad():
    logits = model(input_values).logits
    
# get the transcription with processor
if USE_LM:
    transcription = processor.batch_decode(logits.numpy()).text
else:
    pred_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(pred_ids)
# print the output
print(transcription)
```

# Cite us

If you use this code for your research, please cite our paper with:

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
@article{zuluaga2022bertraffic,
  title={BERTraffic: BERT-based Joint Speaker Role and Speaker Change Detection for Air Traffic Control Communications},
  author={Zuluaga-Gomez, Juan and Sarfjoo, Seyyed Saeed and Prasad, Amrutha and others},
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
- learning_rate: 0.0001
- train_batch_size: 24
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| No log        | 0.63  | 500   | 3.0458          | 1.0    |
| 2.9181        | 1.27  | 1000  | 1.1503          | 0.4723 |
| 2.9181        | 1.9   | 1500  | 0.8275          | 0.3500 |
| 0.7646        | 2.53  | 2000  | 0.6990          | 0.2845 |
| 0.7646        | 3.17  | 2500  | 0.5828          | 0.2509 |
| 0.5394        | 3.8   | 3000  | 0.5363          | 0.2487 |
| 0.5394        | 4.44  | 3500  | 0.5467          | 0.2171 |
| 0.4558        | 5.07  | 4000  | 0.5290          | 0.2090 |
| 0.4558        | 5.7   | 4500  | 0.4992          | 0.2046 |
| 0.3773        | 6.34  | 5000  | 0.4934          | 0.2052 |
| 0.3773        | 6.97  | 5500  | 0.4700          | 0.1983 |
| 0.3301        | 7.6   | 6000  | 0.4938          | 0.1874 |
| 0.3301        | 8.24  | 6500  | 0.5364          | 0.1893 |
| 0.2938        | 8.87  | 7000  | 0.5170          | 0.1830 |
| 0.2938        | 9.51  | 7500  | 0.5408          | 0.1815 |
| 0.2674        | 10.14 | 8000  | 0.5581          | 0.1733 |
| 0.2674        | 10.77 | 8500  | 0.5389          | 0.1719 |
| 0.24          | 11.41 | 9000  | 0.5344          | 0.1714 |
| 0.24          | 12.04 | 9500  | 0.5503          | 0.1686 |
| 0.211         | 12.67 | 10000 | 0.5595          | 0.1687 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.2

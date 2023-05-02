---
license: apache-2.0
language: en
datasets:
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
- name: wav2vec2-large-960h-lv60-self-en-atc-uwb-atcc
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
      value: 17.20
      name: TEST WER
      verified: False
    - type: wer
      value: 13.72
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
      value: 15.31
      name: TEST WER
      verified: False
    - type: wer
      value: 11.88
      name: TEST WER (+LM)
      verified: False   
---

# wav2vec2-large-960h-lv60-self-en-atc-uwb-atcc

This model is a fine-tuned version of [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) on the [UWB-ATCC corpus](https://huggingface.co/datasets/Jzuluaga/uwb_atcc). 

<a href="https://colab.research.google.com/github/idiap/w2v2-air-traffic/blob/main/src/eval_xlsr_atc_model.ipynb">
    <img alt="GitHub" src="https://colab.research.google.com/assets/colab-badge.svg\">
</a>
<a href="https://github.com/idiap/w2v2-air-traffic">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>

It achieves the following results on the evaluation set:
- Loss: 0.7287
- Wer: 0.1756

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

- We use the UWB-ATCC corpus to fine-tune this model. You can download the raw data here: https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-CCA1-0
- However, do not worry, we have prepared the database in `Datasets format`. Here, [UWB-ATCC corpus on HuggingFace](https://huggingface.co/datasets/Jzuluaga/uwb_atcc). You can scroll and check the train/test partitions, and even listen to some audios.
- If you want to prepare a database in HuggingFace format, you can follow the data loader script in: [data_loader_atc.py](https://huggingface.co/datasets/Jzuluaga/uwb_atcc/blob/main/atc_data_loader.py).
- 
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
MODEL_ID = "Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-uwb-atcc"

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
| No log        | 1.06  | 500   | 2.9016          | 0.9995 |
| 2.877         | 2.12  | 1000  | 0.9812          | 0.3485 |
| 2.877         | 3.18  | 1500  | 0.7842          | 0.2732 |
| 0.7834        | 4.25  | 2000  | 0.6962          | 0.2192 |
| 0.7834        | 5.31  | 2500  | 0.6527          | 0.2042 |
| 0.6084        | 6.37  | 3000  | 0.6220          | 0.1972 |
| 0.6084        | 7.43  | 3500  | 0.6442          | 0.1934 |
| 0.5147        | 8.49  | 4000  | 0.6793          | 0.1950 |
| 0.5147        | 9.55  | 4500  | 0.6432          | 0.1920 |
| 0.4566        | 10.62 | 5000  | 0.6605          | 0.1853 |
| 0.4566        | 11.68 | 5500  | 0.6393          | 0.1866 |
| 0.4155        | 12.74 | 6000  | 0.6918          | 0.1803 |
| 0.4155        | 13.8  | 6500  | 0.6514          | 0.1791 |
| 0.372         | 14.86 | 7000  | 0.7010          | 0.1851 |
| 0.372         | 15.92 | 7500  | 0.6824          | 0.1786 |
| 0.3368        | 16.99 | 8000  | 0.6895          | 0.1780 |
| 0.3368        | 18.05 | 8500  | 0.7150          | 0.1759 |
| 0.3244        | 19.11 | 9000  | 0.7141          | 0.1759 |
| 0.3244        | 20.17 | 9500  | 0.7225          | 0.1756 |
| 0.2981        | 21.23 | 10000 | 0.7287          | 0.1756 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.2

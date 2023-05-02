---
license: apache-2.0
language: en
datasets:
- Jzuluaga/atcosim_corpus
tags:
- audio
- automatic-speech-recognition
- en-atc
- en
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-large-960h-lv60-self-en-atc-atcosim
  results:
  - task:
        type: automatic-speech-recognition
        name: Speech Recognition
    dataset:
        type: Jzuluaga/atcosim_corpus
        name: ATCOSIM dataset (Air Traffic Control Communications)
        config: test
        split: test
    metrics:
    - type: wer
      value: 1.67
      name: TEST WER
      verified: False
---

# wav2vec2-large-960h-lv60-self-en-atc-atcosim

This model is a fine-tuned version of [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) on the [ATCOSIM corpus](https://huggingface.co/datasets/Jzuluaga/atcosim_corpus). 

<a href="https://colab.research.google.com/github/idiap/w2v2-air-traffic/blob/main/src/eval_xlsr_atc_model.ipynb">
    <img alt="GitHub" src="https://colab.research.google.com/assets/colab-badge.svg\">
</a>
<a href="https://github.com/idiap/w2v2-air-traffic">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green\">
</a>

It achieves the following results on the evaluation set:
- Loss: 0.0850
- Wer: 0.0167 (1.67% WER)

Paper: [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822).

Authors: Juan Zuluaga-Gomez, Amrutha Prasad, Iuliia Nigmatulina, Saeed Sarfjoo, Petr Motlicek, Matthias Kleinert, Hartmut Helmke, Oliver Ohneiser, Qingran Zhan

Abstract: Recent work on self-supervised pre-training focus</b> on leveraging large-scale unlabeled speech data to build robust end-to-end (E2E)acoustic models (AM) that can be later fine-tuned on downstream tasks e.g., automatic speech recognition (ASR). Yet, few works investigated the impact on performance when the data properties substantially differ between the pre-training and fine-tuning phases, termed domain shift. We target this scenario by analyzing the robustness of Wav2Vec 2.0 and XLS-R models on downstream ASR for a completely unseen domain, air traffic control (ATC) communications. We benchmark these two models on several open-source and challenging ATC databases with signal-to-noise ratio between 5 and 20 dB. Relative word error rate (WER) reductions between 20% to 40% are obtained in comparison to hybrid-based ASR baselines by only fine-tuning E2E acoustic models with a smaller fraction of labeled data. We analyze WERs on the low-resource scenario and gender bias carried by one ATC dataset.

Code — GitHub repository: https://github.com/idiap/w2v2-air-traffic

## Usage

You can use our Google Colab notebook to run and evaluate our model: https://github.com/idiap/w2v2-air-traffic/blob/master/src/eval_xlsr_atc_model.ipynb

(you need to change the `MODEL_ID` param to `MODEL_ID=Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-atcosim`)
## Intended uses & limitations

This model was fine-tuned on air traffic control data. We don't expect that it keeps the same performance on some others datasets, e.g., LibriSpeech or CommonVoice.

## Training and evaluation data

See Table 1 (page 3) in our paper: [How Does Pre-trained Wav2Vec 2.0 Perform on Domain Shifted ASR? An Extensive Benchmark on Air Traffic Control Communications](https://arxiv.org/abs/2203.16822). We described there the partitions of how to use our model. 

- We use the ATCOSIM dataset for fine-tuning this model. You can download the raw data here: https://www.spsc.tugraz.at/databases-and-tools/atcosim-air-traffic-control-simulation-speech-corpus.html

- However, do not worry, we have prepared the database in `Datasets format`. Here, [ATCOSIM CORPUS on HuggingFace](https://huggingface.co/datasets/Jzuluaga/atcosim_corpus). You can scroll and check the train/test partitions, and even listen to some audios.

- If you want to prepare a database in HuggingFace format, you can follow the data loader script in: [data_loader_atc.py](https://huggingface.co/datasets/Jzuluaga/atcosim_corpus/blob/main/atc_data_loader.py).

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
DATASET_ID = "Jzuluaga/atcosim_corpus"
MODEL_ID = "Jzuluaga/wav2vec2-large-960h-lv60-self-en-atc-atcosim"

# 1. Load the dataset
# we only load the 'test' partition, however, if you want to load the 'train' partition, you can change it accordingly
atcosim_corpus_test = load_dataset(DATASET_ID, "test", split="test")

# 2. Load the model
model = AutoModelForCTC.from_pretrained(MODEL_ID)

# 3. Load the processors, we offer support with LM, which should yield better resutls
if USE_LM:
    processor = Wav2Vec2ProcessorWithLM.from_pretrained(MODEL_ID)
else:
    processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)

# 4. Format the test sample
sample = next(iter(atcosim_corpus_test))
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
- learning_rate: 0.0005
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 96
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 20000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 1.4757        | 6.41   | 500   | 0.0614          | 0.0347 |
| 0.0624        | 12.82  | 1000  | 0.0525          | 0.0277 |
| 0.0388        | 19.23  | 1500  | 0.0693          | 0.0241 |
| 0.03          | 25.64  | 2000  | 0.0666          | 0.0244 |
| 0.0235        | 32.05  | 2500  | 0.0604          | 0.0260 |
| 0.0226        | 38.46  | 3000  | 0.0625          | 0.0230 |
| 0.0163        | 44.87  | 3500  | 0.0603          | 0.0195 |
| 0.0157        | 51.28  | 4000  | 0.0628          | 0.0209 |
| 0.0152        | 57.69  | 4500  | 0.0692          | 0.0238 |
| 0.0122        | 64.1   | 5000  | 0.0607          | 0.0210 |
| 0.011         | 70.51  | 5500  | 0.0608          | 0.0213 |
| 0.0114        | 76.92  | 6000  | 0.0681          | 0.0211 |
| 0.0106        | 83.33  | 6500  | 0.0613          | 0.0210 |
| 0.0081        | 89.74  | 7000  | 0.0654          | 0.0196 |
| 0.0078        | 96.15  | 7500  | 0.0612          | 0.0191 |
| 0.0082        | 102.56 | 8000  | 0.0758          | 0.0237 |
| 0.0078        | 108.97 | 8500  | 0.0664          | 0.0206 |
| 0.0075        | 115.38 | 9000  | 0.0658          | 0.0197 |
| 0.0052        | 121.79 | 9500  | 0.0669          | 0.0218 |
| 0.0054        | 128.21 | 10000 | 0.0695          | 0.0211 |
| 0.0053        | 134.62 | 10500 | 0.0726          | 0.0227 |
| 0.0046        | 141.03 | 11000 | 0.0702          | 0.0212 |
| 0.0043        | 147.44 | 11500 | 0.0846          | 0.0200 |
| 0.0041        | 153.85 | 12000 | 0.0764          | 0.0200 |
| 0.0032        | 160.26 | 12500 | 0.0785          | 0.0201 |
| 0.0028        | 166.67 | 13000 | 0.0839          | 0.0197 |
| 0.0035        | 173.08 | 13500 | 0.0785          | 0.0210 |
| 0.0027        | 179.49 | 14000 | 0.0730          | 0.0188 |
| 0.002         | 185.9  | 14500 | 0.0794          | 0.0193 |
| 0.002         | 192.31 | 15000 | 0.0859          | 0.0211 |
| 0.0019        | 198.72 | 15500 | 0.0727          | 0.0183 |
| 0.0017        | 205.13 | 16000 | 0.0784          | 0.0187 |
| 0.0016        | 211.54 | 16500 | 0.0801          | 0.0196 |
| 0.0014        | 217.95 | 17000 | 0.0821          | 0.0185 |
| 0.0011        | 224.36 | 17500 | 0.0822          | 0.0176 |
| 0.001         | 230.77 | 18000 | 0.0856          | 0.0171 |
| 0.001         | 237.18 | 18500 | 0.0792          | 0.0176 |
| 0.001         | 243.59 | 19000 | 0.0826          | 0.0173 |
| 0.0006        | 250.0  | 19500 | 0.0854          | 0.0170 |
| 0.0007        | 256.41 | 20000 | 0.0850          | 0.0167 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.2

---
language: en
datasets:
- superb
tags:
- speech
- audio
- wav2vec2
- audio-classification
widget:
- example_title: VoxCeleb Speaker id10003
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb1_00003.wav
- example_title: VoxCeleb Speaker id10004
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb_00004.wav
license: apache-2.0
---

# Wav2Vec2-Base for Speaker Identification

## Model description

This is a ported version of 
[S3PRL's Wav2Vec2 for the SUPERB Speaker Identification task](https://github.com/s3prl/s3prl/tree/master/s3prl/downstream/voxceleb1).

The base model is [wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base), which is pretrained on 16kHz 
sampled speech audio. When using the model make sure that your speech input is also sampled at 16Khz. 

For more information refer to [SUPERB: Speech processing Universal PERformance Benchmark](https://arxiv.org/abs/2105.01051)

## Task and dataset description

Speaker Identification (SI) classifies each utterance for its speaker identity as a multi-class
classification, where speakers are in the same predefined set for both training and testing. The widely
used [VoxCeleb1](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html) dataset is adopted

For the original model's training and evaluation instructions refer to the 
[S3PRL downstream task README](https://github.com/s3prl/s3prl/tree/master/s3prl/downstream#sid-speaker-identification).


## Usage examples

You can use the model via the Audio Classification pipeline:
```python
from datasets import load_dataset
from transformers import pipeline

dataset = load_dataset("anton-l/superb_demo", "si", split="test")

classifier = pipeline("audio-classification", model="superb/wav2vec2-base-superb-sid")
labels = classifier(dataset[0]["file"], top_k=5)
```

Or use the model directly:
```python
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2FeatureExtractor

def map_to_array(example):
    speech, _ = librosa.load(example["file"], sr=16000, mono=True)
    example["speech"] = speech
    return example

# load a demo dataset and read audio files
dataset = load_dataset("anton-l/superb_demo", "si", split="test")
dataset = dataset.map(map_to_array)

model = Wav2Vec2ForSequenceClassification.from_pretrained("superb/wav2vec2-base-superb-sid")
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("superb/wav2vec2-base-superb-sid")

# compute attention masks and normalize the waveform if needed
inputs = feature_extractor(dataset[:2]["speech"], sampling_rate=16000, padding=True, return_tensors="pt")

logits = model(**inputs).logits
predicted_ids = torch.argmax(logits, dim=-1)
labels = [model.config.id2label[_id] for _id in predicted_ids.tolist()]
```

## Eval results

The evaluation metric is accuracy.

|        | **s3prl** | **transformers** |
|--------|-----------|------------------|
|**test**| `0.7518`  | `0.7518`         |

### BibTeX entry and citation info

```bibtex
@article{yang2021superb,
  title={SUPERB: Speech processing Universal PERformance Benchmark},
  author={Yang, Shu-wen and Chi, Po-Han and Chuang, Yung-Sung and Lai, Cheng-I Jeff and Lakhotia, Kushal and Lin, Yist Y and Liu, Andy T and Shi, Jiatong and Chang, Xuankai and Lin, Guan-Ting and others},
  journal={arXiv preprint arXiv:2105.01051},
  year={2021}
}
```
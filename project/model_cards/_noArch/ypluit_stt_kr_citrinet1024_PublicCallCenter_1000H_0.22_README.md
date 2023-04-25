---
language:
- kr
license: cc-by-4.0
library_name: nemo
datasets:
- RealCallData
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- Citrinet1024
- NeMo
- pytorch
model-index:
- name: stt_kr_citrinet1024_PublicCallCenter_1000H_0.22
  results: []
---

## Model Overview

<DESCRIBE IN ONE LINE THE MODEL AND ITS USE>

## NVIDIA NeMo: Training

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest Pytorch version.
```
pip install nemo_toolkit['all']
``` 

## How to Use this Model

The model is available for use in the NeMo toolkit [1], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.


### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained("ypluit/stt_kr_citrinet1024_PublicCallCenter_1000H_0.22")
```


### Transcribing using Python
First, let's get a sample
```
get any korean telephone voice wave file
```
Then simply do:
```
asr_model.transcribe(['sample-kr.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py  pretrained_name="model"  audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000Hz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.


## Model Architecture

See nemo toolkit and reference papers.
## Training

Learned about 30 days on 2 A6000

### Datasets

Private call center real data (1100hour)

## Performance

< 0.13 CER

## Limitations

This model was trained with 650 hours of Korean telephone voice data for customer service in a call center. might be Poor performance for general-purpose dialogue and specific accents.

## References


[1] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

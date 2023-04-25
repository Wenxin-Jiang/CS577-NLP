---
language:
- de
license: cc-by-4.0
library_name: nemo
datasets:
- mozilla-foundation/common_voice_7_0
- Multilingual LibriSpeech (2000 hours)
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- Conformer
- Transformer
- NeMo
- pytorch
model-index:
- name: stt_de_conformer_transducer_large
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      type: common_voice_7_0
      name: mozilla-foundation/common_voice_7_0
      config: other
      split: test
      args:
        lageangu: de
    metrics:
    - type: wer
      value: 4.93
      name: WER
---


## Model Overview

<DESCRIBE IN ONE LINE THE MODEL AND ITS USE>

## NVIDIA NeMo: Training

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest Pytorch version.
```
pip install nemo_toolkit['all']
``` 

## How to Use this Model

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained("iqbalc/stt_de_conformer_transducer_large")
```

### Transcribing using Python
```
asr_model.transcribe(['filename.wav'])

```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py  pretrained_name="iqbalc/stt_de_conformer_transducer_large"  audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model for Automatic Speech Recognition which uses Transducer loss/decoding

## Training

The NeMo toolkit was used for training the models. These models are fine-tuned with this example script and this base config.

The tokenizers for these models were built using the text transcripts of the train set with this script.

### Datasets

All the models in this collection are trained on a composite dataset comprising of over two thousand hours of cleaned German speech:

1. MCV7.0 567 hours 
2. MLS 1524 hours 
3. VoxPopuli 214 hours

## Performance

Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

MCV7.0 test	= 4.93

## Limitations

The model might perform worse for accented speech


## References
[NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
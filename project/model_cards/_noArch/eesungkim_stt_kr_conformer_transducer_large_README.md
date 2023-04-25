---
language:
- kr
license: cc-by-4.0
library_name: nemo
datasets:
- Ksponspeech
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- transducer
- Conformer
- Transformer
- NeMo
- pytorch
model-index:
- name: stt_kr_conformer_transducer_large
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
asr_model = nemo_asr.models.ASRModel.from_pretrained("eesungkim/stt_kr_conformer_transducer_large")
```

### Transcribing using Python
First, let's get a sample
```
wget https://dldata-public.s3.us-east-2.amazonaws.com/sample-kor.wav
```
Then simply do:
```
asr_model.transcribe(['sample-kor.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py  pretrained_name="eesungkim/stt_kr_conformer_transducer_large"  audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model [2] for Automatic Speech Recognition which uses Transducer loss/decoding. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html).

## Training

The model was finetuned based on the pre-trained English Model for over several epochs. 

There are several transcribing and sub-word modeling methods for Korean speech recognition. This model uses sentencepiece subwords of Hangul characters based on phonetic transcription using Google Sentencepiece Tokenizer [3].

### Datasets

All the models in this collection are trained on [Ksponspeech](https://aihub.or.kr/aidata/105/download) dataset, which is an open-domain dialog corpus recorded by 2,000 native Korean speakers in a controlled and quiet environment. The standard split dataset consists of 965 hours of training set, 4 hours of development set, 3 hours of test-clean, and 4 hours of test-other.

## Performance

Version | Tokenizer | eval_clean CER | eval_other CER | eval_clean WER | eval_other WER
--- | --- | --- | --- |--- |---
v1.7.0rc | SentencePiece Char | 6.94% | 7.38% | 19.49% | 22.73%

## Limitations

Since this model was trained on publically available speech datasets, the performance of this model might degrade for speech which including technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

This model produces a spoken-form token sequence. If you want to have a written form, you can consider applying inverse text normalization.


## References

[1] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

[2] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)

[3] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)





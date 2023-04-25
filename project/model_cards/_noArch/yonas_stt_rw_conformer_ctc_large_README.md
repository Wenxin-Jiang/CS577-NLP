---
language:
- rw
license: cc-by-4.0
library_name: nemo
datasets:
- mozilla-foundation/common_voice_11_0
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- Kinyarwanda
- audio
- CTC
- Conformer
- Transformer
- NeMo
- pytorch
model-index:
- name: stt_rw_conformer_ctc_large
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

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained("yonas/stt_rw_conformer_ctc_large")
```

### Transcribing using Python
First, let's get a sample
```
wget https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav
```
Then simply do:
```
asr_model.transcribe(['2086-149220-0033.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py  pretrained_name="yonas/stt_rw_conformer_ctc_large"  audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

<ADD SOME INFORMATION ABOUT THE ARCHITECTURE>

## Training

<ADD INFORMATION ABOUT HOW THE MODEL WAS TRAINED - HOW MANY EPOCHS, AMOUNT OF COMPUTE ETC>

### Datasets

<LIST THE NAME AND SPLITS OF DATASETS USED TO TRAIN THIS MODEL (ALONG WITH LANGUAGE AND ANY ADDITIONAL INFORMATION)>

## Performance

<LIST THE SCORES OF THE MODEL - 
      OR
USE THE Hugging Face Evaluate LiBRARY TO UPLOAD METRICS>

## Limitations

<DECLARE ANY POTENTIAL LIMITATIONS OF THE MODEL>

Eg: 
Since this model was trained on publically available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.


## References

<ADD ANY REFERENCES HERE AS NEEDED>

[1] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)


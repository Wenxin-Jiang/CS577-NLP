---
language:
- es
library_name: nemo
datasets:
- Fisher
- VoxPopuli
- facebook/multilingual_librispeech
- mozilla-foundation/common_voice_7_0
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- Transducer
- Conformer
- Transformer
- pytorch
- NeMo
- hf-asr-leaderboard
license: cc-by-4.0
model-index:
- name: stt_es_conformer_transducer_large
  results:
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: common-voice-7-0-6
      type: mozilla-foundation/common_voice_7_0
      config: es
      split: dev
      args:
        language: es
    metrics:
    - name: Dev WER
      type: wer
      value: 4.6
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: common-voice-7-0-6
      type: mozilla-foundation/common_voice_7_0
      config: es
      split: test
      args:
        language: es
    metrics:
    - name: Test WER
      type: wer
      value: 5.2
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: spanish
      split: dev
      args:
        language: es
    metrics:
    - name: Dev WER
      type: wer
      value: 2.7
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: spanish
      split: test
      args:
        language: es
    metrics:
    - name: Test WER
      type: wer
      value: 3.2
---
# NVIDIA Conformer-Transducer Large (es)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-es-lightgrey#model-badge)](#datasets)


This model transcribes speech in lowercase Spanish alphabet including spaces, and was trained on a composite dataset comprising of 1340 hours of Spanish speech. It is a "large" variant of Conformer-Transducer, with around 120 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.

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
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_es_conformer_transducer_large")
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
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_es_conformer_transducer_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 Hz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses Transducer loss/decoding instead of CTC Loss. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_transducer/speech_to_text_rnnt_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_transducer_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of 1340 hours of Spanish speech:

- Mozilla Common Voice 7.0 (Spanish) - 289 hours after data cleaning
- Multilingual LibriSpeech (Spanish) - 801 hours after data cleaning
- Voxpopuli transcribed subset (Spanish) - 110 hours after data cleaning
- Fisher dataset (Spanish) - 140 hours after data cleaning

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | MCV 7.0 Dev | MCV 7.0 Test | MLS Dev | MLS Test | Voxpopuli Dev | Voxpopuli Test | Fisher Dev | Fisher Test| Train Dataset   |
|---------|-----------------------|-----------------|-------------|--------------|---------|----------|---------------|----------------|------------|-------------|-----------------|
| 1.8.0   | SentencePiece Unigram | 1024            | 4.6         | 5.2          | 2.7     | 3.2      | 4.7           | 6.0            | 14.7       | 14.8        | NeMo ASRSET 2.0 |

## Limitations
Since this model was trained on publicly available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## NVIDIA Riva: Deployment

[NVIDIA Riva](https://developer.nvidia.com/riva), is an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, on edge, and embedded. 
Additionally, Riva provides: 

* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and enterprise-grade support 

Although this model isn’t supported yet by Riva, the [list of supported models is here](https://huggingface.co/models?other=Riva).  
Check out [Riva live demo](https://developer.nvidia.com/riva#demos). 

## References
- [1] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
- [2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
- [3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

## Licence

License to use this model is covered by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). By downloading the public and release version of the model, you accept the terms and conditions of the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.

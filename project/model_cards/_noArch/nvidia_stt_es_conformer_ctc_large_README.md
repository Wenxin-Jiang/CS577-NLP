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
- CTC
- Conformer
- Transformer
- pytorch
- NeMo
- hf-asr-leaderboard
- Riva
license: cc-by-4.0
model-index:
- name: stt_es_conformer_ctc_large
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
      value: 5.0
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
      value: 5.5
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
      value: 3.6
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
      value: 3.6
---
# NVIDIA Conformer-CTC Large (es)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-es-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model transcribes speech in lowercase Spanish alphabet including spaces, and was trained on a composite dataset comprising of 1340 hours of Spanish speech. It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-ctc) for complete architecture details.
It is also compatible with NVIDIA Riva for [production-grade server deployments](#deployment-with-nvidia-riva). 


## Usage

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_es_conformer_ctc_large")
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
 pretrained_name="nvidia/stt_es_conformer_ctc_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 kHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-CTC model is a non-autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on the detail of this model here: [Conformer-CTC Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-ctc). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_ctc_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

The checkpoint of the language model used as the neural rescorer can be found [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_es_conformer_ctc_large/files). You may find more info on how to train and use language models for ASR models here: [ASR Language Modeling](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/asr_language_modeling.html)

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
| 1.8.0   | SentencePiece Unigram | 1024            | 6.3         | 6.9          | 4.3     | 4.2      | 6.1           | 7.5            | 18.3       | 18.5        | NeMo ASRSET 2.0 |

While deploying with [NVIDIA Riva](https://developer.nvidia.com/riva), you can combine this model with external language models to further improve WER. The WER(%) of the latest model with different language modeling techniques are reported in the following table.

| Language Modeling | Training Dataset                                                             | MCV 7.0 Dev | MCV 7.0 Test | MLS Dev | MLS Test | Voxpopuli Dev | Voxpopuli Test | Fisher Dev | Fisher Test| Comment                                                |
|-------------------|------------------------------------------------------------------------------|-------------|--------------|---------|----------|---------------|----------------|----------------|----------------|--------------------------------------------------------|
| N-gram LM         | Spanish News Crawl corpus (50M sentences) + NeMo ASRSET training transcripts | 5.0         | 5.5          | 3.6     | 3.6      | 5.5           | 6.7 | 17.4 | 17.5            | N=4, beam_width=128, n_gram_alpha=0.8, n_gram_beta=1.5 |

## Limitations
Since this model was trained on publicly available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## Deployment with NVIDIA Riva
For the best real-time accuracy, latency, and throughput, deploy the model with [NVIDIA Riva](https://developer.nvidia.com/riva), an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, at the edge, and embedded. 
Additionally, Riva provides: 
* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and Enterprise-grade support 
Check out [Riva live demo](https://developer.nvidia.com/riva#demos).

## References
- [1] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
- [2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
- [3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
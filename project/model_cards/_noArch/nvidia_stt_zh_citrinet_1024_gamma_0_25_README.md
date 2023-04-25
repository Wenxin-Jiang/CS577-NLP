---
language:
- zh
library_name: nemo
datasets:
- aishell_2
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- Citrinet
- pytorch
- NeMo
- hf-asr-leaderboard
- Riva
license: cc-by-4.0
model-index:
- name: stt_zh_citrinet_1024_gamma_0_25
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Dev iOS
      type: aishell_2
      config: ios
      split: dev
      args:
        language: zh
    metrics:
    - name: Dev CER
      type: cer
      value: 4.8
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Test iOS
      type: aishell_2
      config: ios
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.1
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Dev Android
      type: aishell_2
      config: android
      split: dev
      args:
        language: zh
    metrics:
    - name: Dev CER
      type: cer
      value: 5.2
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Test Android
      type: aishell_2
      config: android
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.5
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Dev Mic
      type: aishell_2
      config: mic
      split: dev
      args:
        language: zh
    metrics:
    - name: Dev CER
      type: cer
      value: 5.2
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Test Mic
      type: aishell_2
      config: mic
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.5
---

# NVIDIA Streaming Citrinet 1024 (zh)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Citrinet--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-140M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-zh-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model utilizes a character encoding scheme, and transcribes text in the standard character set that is provided in the Aishell-2 Mandard Corpus.
It is a non-autoregressive "large" variant of Citrinet, with around 140 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#citrinet) for complete architecture details.
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
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained("nvidia/stt_zh_citrinet_1024_gamma_0_25")
```

### Transcribing using Python
First, let's get a sample of spoken Mandarin Chinese.

Then simply do:
```
asr_model.transcribe(['<Path of audio file(s)>'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_zh_citrinet_1024_gamma_0_25" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 kHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Citrinet model is a non-autoregressive model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on the detail of this model here: [Citrinet Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#citrinet). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/citrinet/citrinet_1024.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of several thousand hours of English speech:

- AIShell 2

Note: older versions of the model may have trained on smaller set of datasets.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer | Vocabulary Size | Dev iOS | Test iOS | Dev Android | Test Android | Dev Mic | Test Mic | Train Dataset |
|---------|-----------|-----------------|---------|----------|-------------|--------------|---------|----------|---------------|
| 1.0.0   | Character | 5000+           | 4.8     | 5.1      | 5.2         | 5.5          | 5.2     | 5.5      | AIShell 2     |
|         |           |                 |         |          |             |              |         |          |               |
|         |           |                 |         |          |             |              |         |          |               |

While deploying with [NVIDIA Riva](https://developer.nvidia.com/riva), you can combine this model with external language models to further improve WER. The WER(%) of the latest model with different language modeling techniques are reported in the following table.

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

- [1] [Citrinet: Closing the Gap between Non-Autoregressive and Autoregressive End-to-End Models for Automatic Speech Recognition](https://arxiv.org/abs/2104.01721)

- [2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

- [3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
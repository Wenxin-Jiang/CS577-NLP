---
language:
- it
library_name: nemo
datasets:
- facebook/voxpopuli
- facebook/multilingual_librispeech
- mozilla-foundation/common_voice_11_0
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
- name: stt_it_conformer_ctc_large
  results:
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: common-voice-11-0
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: dev
      args:
        language: it
    metrics:
    - name: Dev WER
      type: wer
      value: 5.38
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: common-voice-11-0
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: test
      args:
        language: it
    metrics:
    - name: Test WER
      type: wer
      value: 5.92
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: italian
      split: dev
      args:
        language: it
    metrics:
    - name: Dev WER
      type: wer
      value: 13.16
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: italian
      split: test
      args:
        language: it
    metrics:
    - name: Test WER
      type: wer
      value: 10.62
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: VoxPopuli
      type: facebook/voxpopuli
      config: it
      split: dev
      args:
        language: it
    metrics:
    - name: Dev WER
      type: wer
      value: 13.43
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: VoxPopuli
      type: facebook/voxpopuli
      config: it
      split: test
      args:
        language: it
    metrics:
    - name: Test WER
      type: wer
      value: 16.75
---
# NVIDIA Conformer-CTC Large (it)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-it-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model transcribes speech in lowercase Italian alphabet including spaces, and was trained on a composite dataset comprising of 487 hours of Italian speech. It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
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
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_it_conformer_ctc_large")
```

### Transcribing using Python

Simply do:

```
asr_model.transcribe(['sample.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_it_conformer_ctc_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 kHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-CTC model is a non-autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on the detail of this model here: [Conformer-CTC Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-ctc). 

## Training

The NeMo toolkit [3] was used for training these models for over several hundred epochs. These models are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_ctc_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

The checkpoint of the language model used as the neural rescorer can be found [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_it_conformer_ctc_large/files). To train n-gram language model only the transcriptions from the training dataset was used. You may find more info on how to train and use language models for ASR models here: [ASR Language Modeling](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/asr_language_modeling.html)

### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of 487 hours of Italian speech:
- Mozilla Common Voice 11.0 (Italian) - 220 hours after data cleaning
- Multilingual LibriSpeech (Italian) - 214 hours after data cleaning
- VoxPopuli transcribed subset (Italian) - 53 hours after data cleaning

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | MCV 11.0 Dev | MCV 11.0 Test | MLS Dev | MLS Test | VoxPopuli Dev | VoxPopuli Test | Train Dataset      |
|---------|-----------------------|-----------------|--------------|---------------|---------|----------|---------------|----------------|--------------------|
| 1.13.0  | SentencePiece Unigram | 128             | 6.65         | 7.20          | 14.77   | 11.76    | 14.77         | 18.06          | NeMo ASRSET It 2.0 |

While deploying with [NVIDIA Riva](https://developer.nvidia.com/riva), you can combine this model with external language models to further improve WER. The WER(%) of the latest model with different language modeling techniques are reported in the following table.

| Language Modeling | MCV 11.0 Dev | MCV 11.0 Test | MLS Dev | MLS Test | VoxPopuli Dev | VoxPopuli Test | Comment                                                |
|-------------------|--------------|---------------|---------|----------|---------------|----------------|--------------------------------------------------------|
| N-gram LM         | 5.38         | 5.92          | 13.16   | 10.62    | 13.43         | 16.75          | N=5, beam_width=128, n_gram_alpha=2.0, n_gram_beta=2.0 |
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

## Licence

License to use this model is covered by the [CC-BY-4 License](https://creativecommons.org/licenses/by/4.0/legalcode) unless another License/Terms Of Use/EULA is clearly specified. By downloading the public and release version of the model, you accept the terms and conditions of the [CC-BY-4 License](https://creativecommons.org/licenses/by/4.0/legalcode).
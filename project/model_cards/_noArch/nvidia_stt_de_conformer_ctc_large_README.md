---
language:
- de
library_name: nemo
datasets:
- VoxPopuli-(DE)
- Multilingual-LibriSpeech
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
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
model-index:
- name: stt_de_conformer_ctc_large
  results:
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      config: de
      split: test
      args:
        language: de
    metrics:
    - name: Test WER
      type: wer
      value: 6.68
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: de
      split: test
      args:
        language: de
    metrics:
    - name: Test WER
      type: wer
      value: 4.63
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: VoxPopuli
      type: VoxPopuli
    metrics:
    - name: Test WER
      type: wer
      value: 10.51
---

# NVIDIA Conformer-CTC Large (de)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-de-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model transcribes speech in lowercase German alphabet including spaces, and is trained on several thousand hours of German speech data.
It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
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
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_de_conformer_ctc_large")
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
 pretrained_name="nvidia/stt_de_conformer_ctc_large" 
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

### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of several thousand hours of English speech:

- VoxPopuli (DE)
- Multilingual Librispeech (MLS DE) - 1500 hours subset
- Mozilla Common Voice (v7.0)

Note: older versions of the model may have trained on smaller set of datasets.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer | Vocabulary Size | MCV7.0 dev | MCV7.0 test | MLS dev | MLS test | Voxpopuli dev | Voxpopuli test |
|---------|-----------------------|-----------------|---------------|---------------|------------|-----------|------------|----------------|
| 1.5.0 | SentencePiece Unigram | 128 | 5.84 | 6.68 | 3.85 | 4.63 | 12.56 | 10.51 |



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
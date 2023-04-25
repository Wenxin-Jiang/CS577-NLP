---
language:
- en
library_name: nemo
datasets:
- librispeech_asr
- fisher_corpus
- Switchboard-1
- WSJ-0
- WSJ-1
- National-Singapore-Corpus-Part-1
- National-Singapore-Corpus-Part-6
- vctk
- VoxPopuli-(EN)
- Europarl-ASR-(EN)
- Multilingual-LibriSpeech-(2000-hours)
- mozilla-foundation/common_voice_8_0
- MLCommons/peoples_speech
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
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
model-index:
- name: stt_en_conformer_transducer_xlarge
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (clean)
      type: librispeech_asr
      config: clean
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 1.62
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: LibriSpeech (other)
      type: librispeech_asr
      config: other
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 3.01
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: english
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 5.32
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 7.0
      type: mozilla-foundation/common_voice_7_0
      config: en
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 5.13
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      config: en
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 6.46
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Wall Street Journal 92
      type: wsj_0
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 1.17
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Wall Street Journal 93
      type: wsj_1
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 2.05
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: National Singapore Corpus
      type: nsc_part_1
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 5.7
---

# NVIDIA Conformer-Transducer X-Large (en-US)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-600M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-en--US-lightgrey#model-badge)](#datasets)


This model transcribes speech in lower case English alphabet along with spaces and apostrophes.
It is an "extra-large" versions of Conformer-Transducer (around 600M parameters) model.  
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.

## NVIDIA NeMo: Training

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest Pytorch version.
```
pip install nemo_toolkit['all']
'''
'''
(if it causes an error): 
pip install nemo_toolkit[all]
``` 

## How to Use this Model

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_en_conformer_transducer_xlarge")
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
 pretrained_name="nvidia/stt_en_conformer_transducer_xlarge" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses Transducer loss/decoding instead of CTC Loss. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_transducer/speech_to_text_rnnt_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_transducer_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of several thousand hours of English speech:

- Librispeech 960 hours of English speech
- Fisher Corpus
- Switchboard-1 Dataset
- WSJ-0 and WSJ-1
- National Speech Corpus (Part 1, Part 6)
- VCTK
- VoxPopuli (EN)
- Europarl-ASR (EN)
- Multilingual Librispeech (MLS EN) - 2,000 hrs subset
- Mozilla Common Voice (v8.0)
- People's Speech  - 12,000 hrs subset

Note: older versions of the model may have trained on smaller set of datasets.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer | Vocabulary Size | LS test-other | LS test-clean | WSJ Eval92 | WSJ Dev93 | NSC Part 1 |  MLS Test | MLS Dev | MCV Test 8.0 | Train Dataset |
|---------|-----------------------|-----------------|---------------|---------------|------------|-----------|-----|-------|------|----|------|
| 1.10.0 | SentencePiece Unigram | 1024 | 3.01 | 1.62 | 1.17 | 2.05 | 5.70 | 5.32 | 4.59 | 6.46 | NeMo ASRSET 3.0 |

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
[1] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
[2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
[3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

## Licence

License to use this model is covered by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). By downloading the public and release version of the model, you accept the terms and conditions of the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
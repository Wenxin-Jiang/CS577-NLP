---
language: fr
library_name: nemo
datasets:
- multilingual_librispeech
- mozilla-foundation/common_voice_7_0
- VoxPopuli
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
- name: stt_fr_conformer_ctc_large
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: MCV 7.0
      type: mozilla-foundation/common_voice_7_0
      config: fr
      split: dev
      args:
        language: fr
    metrics:
    - name: Dev WER
      type: wer
      value: 8.35
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: MCV 7.0
      type: mozilla-foundation/common_voice_7_0
      config: fr
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 9.63
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual Librispeech
      type: multilingual_librispeech
      config: fr
      split: dev
      args:
        language: fr
    metrics:
    - name: Dev WER
      type: wer
      value: 5.88
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual Librispeech
      type: multilingual_librispeech
      config: fr
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 4.91
---

# NVIDIA Conformer-CTC Large (fr)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-fr-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model was trained on a composite dataset comprising of over 1500 hours of French speech.
It is  a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
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
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_fr_conformer_ctc_large")
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
 pretrained_name="nvidia/stt_fr_conformer_ctc_large" 
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

The checkpoint of the language model used for rescoring can be found [here]( https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_fr_conformer_ctc_large). You may find more info on how to train and use language models for ASR models here: [ASR Language Modeling](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/asr_language_modeling.html)

## Datasets
All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of over a thousand hours of French speech:

- MozillaCommonVoice 7.0 - 356 hours
- Multilingual LibriSpeech  - 1036 hours
- VoxPopuli - 182 hours

Both models use same dataset, excluding a preprocessing step to strip hyphen from data for secondary model's training.

## Performance
The performance of Automatic Speech Recognition models is measuring using Word Error Rate. Since this dataset is trained on multiple domains and a much larger corpus, it will generally perform better at transcribing audio in general.

The latest model obtains the following greedy scores on the following evaluation datasets

- 8.35 % on MCV7.0 dev
- 9.63 % on MCV7.0 test
- 5.88 % on MLS dev
- 4.91 % on MLS test

With 128 beam search and 4gram KenLM model:

- 7.95 % on MCV7.0 dev
- 9.16 % on MCV7.0 test
- 5.57 % on MLS dev
- 4.66 % on MLS test

Note that these evaluation datasets have been filtered and preprocessed to only contain French alphabet characters and are removed of punctuation outside of hyphenation and apostrophe.

## Limitations
Since this model was trained on publicly available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

Further, since portions of the training set contain text from both pre- and post- 1990 orthographic reform, regularity of punctuation may vary between the two styles. 
For downstream tasks requiring more consistency, finetuning or downstream processing may be required. If exact orthography is not necessary, then using secondary model is advised.


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


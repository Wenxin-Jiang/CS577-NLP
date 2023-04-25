---
language:
- uk
library_name: nemo
datasets:
- mozilla-foundation/common_voice_10_0
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- Citrinet
- Transformer
- pytorch
- NeMo
- hf-asr-leaderboard
- Riva
model-index:
- name: stt_uk_citrinet_1024_gamma_0_25
  results:
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 10.0
      config: uk
      split: test
      type: mozilla-foundation/common_voice_10_0
    metrics:
    - name: Test WER
      type: wer
      value: 5.02
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 10.0
      config: uk
      split: dev
      type: mozilla-foundation/common_voice_10_0
    metrics:
    - name: Test WER
      type: wer
      value: 4.65
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 9.0
      config: uk
      split: test
      type: mozilla-foundation/common_voice_9_0
    metrics:
    - name: Test WER
      type: wer
      value: 3.75
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 9.0
      config: uk
      split: dev
      type: mozilla-foundation/common_voice_9_0
    metrics:
    - name: Test WER
      type: wer
      value: 4.88
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 8.0
      config: uk
      split: test
      type: mozilla-foundation/common_voice_8_0
    metrics:
    - name: Test WER
      type: wer
      value: 3.52
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
  - dataset:
      args:
        language: uk
      name: Mozilla Common Voice 8.0
      config: uk
      split: dev
      type: mozilla-foundation/common_voice_8_0
    metrics:
    - name: Test WER
      type: wer
      value: 5.02
    task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
license: cc-by-4.0
---
# NVIDIA Streaming Citrinet 1024 (uk)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Citrinet--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-141M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-uk-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |

This model transcribes speech in lowercase Ukrainian alphabet including spaces and apostrophes, and is trained on 69 hours of Ukrainian speech data.
It is a non-autoregressive "large" variant of Streaming Citrinet, with around 141 million parameters. Model is fine-tuned from pre-trained Russian Citrinet-1024 model on Ukrainian speech data using Cross-Language Transfer Learning [4] approach.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-ctc) for complete architecture details.
It is also compatible with NVIDIA Riva for [production-grade server deployments](#deployment-with-nvidia-riva).

## Usage

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed the latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained("nvidia/stt_uk_citrinet_1024_gamma_0_25")
```

### Transcribing using Python
First, let's get a sample.

Then simply do:
```
asr_model.transcribe(['<Path of audio file(s)>'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_uk_citrinet_1024_gamma_0_25" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 kHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Streaming Citrinet-1024 model is a non-autoregressive, streaming variant of Citrinet model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on this model here: [Citrinet Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#citrinet).

## Training

The NeMo toolkit [3] was used for training the model for 1000 epochs. This model was trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/citrinet/citrinet_1024.yaml).

The tokenizer for this models was built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

For details on Cross-Lingual transfer learning see [4].


### Datasets

This model has been trained using validated Mozilla Common Voice Corpus 10.0 dataset (excluding dev and test data) comprising of 69 hours of Ukrainian speech. The Russian model from which this model is fine-tuned has been trained on the union of: (1) Mozilla Common Voice (V7 Ru), (2) Ru LibriSpeech (RuLS), (3) Sber GOLOS and (4) SOVA datasets.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version       | Tokenizer             | Vocabulary Size  | MCV-10 test | MCV-10 dev | MCV-9 test | MCV-9 dev | MCV-8 test | MCV-8 dev |
| :-----------: |:---------------------:| :--------------: | :---------: | :--------: | :--------: | :-------: | :--------: | :-------: |
| 1.0.0         | SentencePiece Unigram | 1024             | 5.02        | 4.65       | 3.75       | 4.88      | 3.52       | 5.02      |

## Limitations

Since this model was trained on publicly available speech datasets, the performance of this model might degrade for speech that includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## Deployment with NVIDIA Riva

For the best real-time accuracy, latency, and throughput, deploy the model with [NVIDIA Riva](https://developer.nvidia.com/riva), an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, at the edge, and embedded. 
Additionally, Riva provides: 
* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and Enterprise-grade support 
Check out [Riva live demo](https://developer.nvidia.com/riva#demos).

## References

[1] [Citrinet: Closing the Gap between Non-Autoregressive and Autoregressive End-to-End Models for Automatic Speech Recognition](https://arxiv.org/abs/2104.01721) <br />
[2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece) <br />
[3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo) <br />
[4] [Cross-Language Transfer Learning](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=qmmIGnwAAAAJ&sortby=pubdate&citation_for_view=qmmIGnwAAAAJ:PVjk1bu6vJQC)
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
thumbnail: null
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
license: cc-by-4.0
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
model-index:
- name: stt_en_citrinet_1024_gamma_0_25
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
      value: 3.4
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
      value: 7.6
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
      value: 2.5
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
      value: 4.0
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
      value: 6.2
---
# NVIDIA Streaming Citrinet 1024 (en-US)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Citrinet--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-145M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-en--US-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model transcribes speech in lowercase English alphabet including spaces and apostrophes, and is trained on several thousand hours of English speech data.
It is a non-autoregressive "large" variant of Streaming Citrinet, with around 140 million parameters.
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
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_en_citrinet_1024_gamma_0_25")
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
 pretrained_name="nvidia/stt_en_citrinet_1024_gamma_0_25" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 kHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Streaming Citrinet-1024 model is a non-autoregressive, streaming variant of Citrinet model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on this model here: [Citrinet Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#citrinet). 

## Training

The NeMo toolkit [3] was used for training the model for over several hundred epochs. This model was trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/citrinet/citrinet_1024.yaml).

The tokenizer for this models was built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).


### Datasets

All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of several thousand hours of English speech:

- Librispeech 960 hours of English speech
- Fisher Corpus
- Switchboard-1 Dataset
- WSJ-0 and WSJ-1
- National Speech Corpus (Part 1, Part 6)

Note: older versions of the model may have trained on smaller set of datasets.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer | Vocabulary Size | LS test-other | LS test-clean | WSJ Eval92 | WSJ Dev93 | NSC Part 1 |Train Dataset |
|---------|-----------------------|-----------------|---------------|---------------|------------|-----------|-----|---------|
| 1.0.0 | SentencePiece Unigram | 1024 | 7.6 | 3.4 | 2.5 | 4.0 | 6.2 | NeMo ASRSET 1.0 |

While deploying with [NVIDIA Riva](https://developer.nvidia.com/riva), you can combine this model with external language models to further improve WER. The WER(%) of the latest model with different language modeling techniques are reported in the following table.

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
[1] [Citrinet: Closing the Gap between Non-Autoregressive and Autoregressive End-to-End Models for Automatic Speech Recognition](https://arxiv.org/abs/2104.01721)
[2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)
[3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
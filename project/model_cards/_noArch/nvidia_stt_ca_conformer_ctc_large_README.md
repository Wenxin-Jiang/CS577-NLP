---
language:
- ca
library_name: nemo
datasets:
- mozilla-foundation/common_voice_9_0
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
- name: stt_ca_conformer_ctc_large
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 9.0
      type: mozilla-foundation/common_voice_9_0
      config: ca
      split: test
      args:
        language: ca
    metrics:
    - name: Test WER
      type: wer
      value: 4.27
---

# NVIDIA Conformer-CTC Large (Catalan)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-ca-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |


This model transcribes speech into lowercase Catalan alphabet including spaces, dashes and apostrophes, and is trained on around 1023 hours of Catalan speech data.
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
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_ca_conformer_ctc_large")
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
 pretrained_name="nvidia/stt_ca_conformer_ctc_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16 kHz mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-CTC model is a non-autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. You may find more info on the detail of this model here: [Conformer-CTC Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-ctc). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_ctc_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

The vocabulary we use contains 44 characters:
```python
[' ', "'", '-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '·', 'à', 'á', 'ç', 'è', 'é', 'í', 'ï', 'ñ', 'ò', 'ó', 'ú', 'ü', 'ı', '–', '—']
```

Full config can be found inside the .nemo files.

The checkpoint of the language model used as the neural rescorer can be found [here](https://ngc.nvidia.com/catalog/models/nvidia:nemo:asrlm_en_transformer_large_ls). You may find more info on how to train and use language models for ASR models here: [ASR Language Modeling](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/asr_language_modeling.html)

### Datasets

All the models in this collection are trained on MCV-9.0 Catalan dataset, which contains around 1203 hours training, 28 hours of development and 27 hours of testing speech audios.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | Dev WER| Test WER| Train Dataset   |
|---------|-----------------------|-----------------|-----|------|-----------------|
| 1.11.0  | SentencePiece Unigram | 128             |4.70 | 4.27 | MCV-9.0 Train set      |

You may use language models (LMs) and beam search to improve the accuracy of the models, as reported in the follwoing table.

| Language Model | Test WER | Test WER w/ Oracle LM | Train Dataset    | Settings                                              |
|----------------|----------|-----------------------|------------------|-------------------------------------------------------|
| N-gram LM      |     3.77 |        1.54           |MCV-9.0 Train set |N=6, beam_width=128, ngram_alpha=1.5, ngram_beta=2.0   |


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
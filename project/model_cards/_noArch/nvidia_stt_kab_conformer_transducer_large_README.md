---
language:
- kab
library_name: nemo
datasets:
- mozilla-foundation/common_voice_10_0
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
- name: stt_kab_conformer_transducer_large
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0
      type: mozilla-foundation/common_voice_10_0
      config: kab
      split: test
      args:
        language: kab
    metrics:
    - name: Test WER
      type: wer
      value: 18.86
---

# NVIDIA Conformer-Transducer Large (Kabyle)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-kab-lightgrey#model-badge)](#datasets)


This model transcribes speech into lowercase Latin alphabet including space and apostrophe and is trained on around 131 hours of Kabyle speech data.
It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.


## Usage

The model is available for use in the NeMo toolkit [3] and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

To train, fine-tune or play with the model, you need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed the latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_kab_conformer_transducer_large")
```

### Transcribing using Python
Simply do:
```
asr_model.transcribe(['<your_audio>.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_kab_conformer_transducer_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16 kHz mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of the Conformer model [1] for Automatic Speech Recognition which uses Transducer loss/decoding. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html).

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_transducer/speech_to_text_rnnt_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_transducer_bpe.yaml).

The vocabulary we use contains 39 characters including space:
```python
['a', 'b', 'c', 'č', 'd', 'ḍ', 'e', 'ɛ', 'f', 'g', 'ǧ', 'ɣ', 'h', 'ḥ', 'i', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'ř', 'ṛ', 's', 'ṣ', 't', 'ṭ', 'u', 'w', 'x', 'y', 'z', 'ẓ', ' ', 'o', 'p', 'γ', 'v']
```
Rare symbols with diacritics were replaced during preprocessing.

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).
For vocabulary of size 128 we restrict the maximum subtoken length to 4 symbols to avoid populating vocabulary with specific frequent words from the dataset. This does not affect the model performance and potentially helps to adapt to other domain without retraining tokenizer.

Full config can be found inside the .nemo files.

### Datasets

All the models in this collection are trained on the MCV-10.0 Kabyle dataset, which contains around 131 hours of training data, 14.74 hours of development, and 15.67 hours of testing speech audio.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | Dev WER| Test WER| Train Dataset   |
|---------|-----------------------|-----------------|--------|---------|-----------------|
| 1.12.0  | SentencePiece BPE, maxlen=4 | 128             |18.12    | 18.86    | MCV-10.0 Train set|


## Limitations

Since this model was trained on publicly available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## Deployment with NVIDIA Riva

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
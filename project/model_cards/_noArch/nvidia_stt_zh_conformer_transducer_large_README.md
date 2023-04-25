---
language:
- zh
library_name: nemo
datasets:
- AISHELL-2
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
- name: stt_zh_conformer_transducer_large
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: AISHELL-2 IOS
      type: aishell2_ios
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.3
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: AISHELL-2 Android
      type: aishell2_android
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.7
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: AISHELL-2 Mic
      type: aishell2_mic
      split: test
      args:
        language: zh
    metrics:
    - name: Test CER
      type: cer
      value: 5.6
---

# NVIDIA Conformer-Transducer Large (zh-ZH)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-zh--ZH-lightgrey#model-badge)](#datasets)


This model transcribes speech in Mandarin alphabet.
It is a large version of Conformer-Transducer (around 120M parameters) model.  
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.

## NVIDIA NeMo: Training

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest Pytorch version.
```
pip install nemo_toolkit['all']
``` 

## How to Use this Model

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_zh_conformer_transducer_large")
```

### Transcribing using Python
You may transcribe an audio file like this:

```
asr_model.transcribe([PATH_TO_THE_AUDIO])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_zh_conformer_transducer_large" 
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

### Datasets

All the models in this collection are trained on AISHELL2 [4] comprising of Mandarin speech:

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer | Vocabulary Size | AISHELL2 Test IOS | AISHELL2 Test Android | AISHELL2 Test Mic | Train Dataset |
|---------|-----------|-----------------|-------------------|-----------------------|-------------------|---------------|
| 1.10.0  | Characters| 5026            | 5.3               | 5.7                    | 5.6              |     AISHELL-2 |

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
[4] [AISHELL-2: Transforming Mandarin ASR Research Into Industrial Scale](https://arxiv.org/abs/1808.10583)

## Licence

License to use this model is covered by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). By downloading the public and release version of the model, you accept the terms and conditions of the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
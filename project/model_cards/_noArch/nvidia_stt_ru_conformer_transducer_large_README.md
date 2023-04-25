---
language:
- ru
library_name: nemo
datasets:
- mozilla-foundation/common_voice_10_0
- SberDevices/Golos
- Russian-LibriSpeech
- SOVA-Dataset
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
- name: stt_ru_conformer_transducer_large
  results:
  - task:
      type: Automatic Speech Recognition
      name: speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0
      type: mozilla-foundation/common_voice_10_0
      config: ru
      split: test
      args:
        language: ru
    metrics:
    - name: Test WER
      type: wer
      value: 3.96
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0
      type: mozilla-foundation/common_voice_10_0
      config: ru
      split: dev
      args:
        language: ru
    metrics:
    - name: Dev WER
      type: wer
      value: 3.49
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Sberdevices Golos (crowd)
      type: SberDevices/Golos
      config: crowd
      split: test
      args:
        language: ru
    metrics:
    - name: Test WER
      type: wer
      value: 2.65
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Sberdevices Golos (farfield)
      type: SberDevices/Golos
      config: farfield
      split: test
      args:
        language: ru
    metrics:
    - name: Test WER
      type: wer
      value: 7.56
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Russian LibriSpeech
      type: RuLS
      config: ru
      split: test
      args:
        language: ru
    metrics:
    - name: Test WER
      type: wer
      value: 11.95
---
# NVIDIA Conformer-Transducer Large (Russian)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-ru-lightgrey#model-badge)](#datasets)

This model transcribes speech into lowercase Cyrillic alphabet including space, and is trained on around 1636 hours of Russian speech data.
It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.

## Usage

The model is available for use in the NeMo toolkit [3], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_ru_conformer_transducer_large")
```

### Transcribing using Python
Simply do:
```
asr_model.transcribe(['<your_audio>.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_ru_conformer_transducer_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16 kHz mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses Transducer loss/decoding. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html).

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_transducer/speech_to_text_rnnt_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_transducer_bpe.yaml).

The vocabulary we use contains 33 characters:
```python
[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
```

Rare symbols with diacritics were replaced during preprocessing.

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

### Datasets
All the models in this collection are trained on a composite dataset (NeMo ASRSET) comprising of more than a thousand hours of Russian speech:

- Mozilla Common Voice 10.0 (Russian) - train subset [28 hours]
- Golos - crowd [1070 hours] and fairfield [111 hours] subsets
- Russian LibriSpeech (RuLS) [92 hours]
- SOVA - RuAudiobooksDevices [260 hours] and RuDevices [75 hours] subsets

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | MCV 10.0 dev | MCV 10.0 test | GOLOS-crowd test | GOLOS-farfield test | RuLS test | Train Dataset |
|---------|-----------------------|-----------------|--------------|---------------|------------------|---------------------|-----------|---------------|
| 1.13.0  | SentencePiece Unigram | 1024            | 3.5          | 4.0           | 2.7              | 7.6                 | 12.0      | NeMo ASRSET   |

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
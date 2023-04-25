---
language:
- hr
library_name: nemo
datasets:
- ParlaSpeech-HR-v1.0
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
---

# NVIDIA Conformer-Transducer Large (Croatian)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Conformer--Transducer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-120M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-hr-lightgrey#model-badge)](#datasets) |


This model transcribes speech in lowercase Croatian alphabet including spaces, and is trained on around 1665 hours of Croatian speech data.
It is a "large" variant of Conformer-Transducer, with around 120 million parameters.
See the [model architecture](#model-architecture) section and [NeMo documentation](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer) for complete architecture details.
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
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained("nvidia/stt_hr_conformer_transducer_large")
```

### Transcribing using Python
Simply do:
```
asr_model.transcribe(['<your_audio>.wav'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/stt_hr_conformer_transducer_large" 
 audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16 kHz single-channel audio as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

Conformer-Transducer model is an autoregressive variant of Conformer model [1] for Automatic Speech Recognition which uses Transducer loss/decoding. You may find more info on the detail of this model here: [Conformer-Transducer Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#conformer-transducer). 

## Training

The NeMo toolkit [3] was used for training the models for over several hundred epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_ctc/speech_to_text_rnnt_bpe.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/conformer/conformer_transducer_bpe.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

The vocabulary we use contains 27 characters:
```python
[' ', 'a', 'b', 'c', 'č', 'ć', 'd', 'đ', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']
```

Full config can be found inside the `.nemo` files.

### Datasets

All the models in this collection are trained on ParlaSpeech-HR v1.0 Croatian dataset, which contains around 1665 hours of training data, 2.2 hours of development and 2.3 hours of test data after data cleaning.

## Performance

The list of the available models in this collection is shown in the following table. Performances of the ASR models are reported in terms of Word Error Rate (WER%) with greedy decoding.

| Version | Tokenizer             | Vocabulary Size | Dev WER | Test WER | Train Dataset       |
|---------|-----------------------|-----------------|---------|----------|---------------------|
| 1.11.0  | SentencePiece Unigram | 128             | 4.56    | 4.69     | ParlaSpeech-HR v1.0 |

You may use language models (LMs) and beam search to improve the accuracy of the models.

## Limitations

Since the model is trained just on ParlaSpeech-HR v1.0 dataset, the performance of this model might degrade for speech which includes terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## References

- [1] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)

- [2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

- [3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
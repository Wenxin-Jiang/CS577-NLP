---
language:
- en
thumbnail: null
tags:
- automatic-speech-recognition
- CTC
- Attention
- Transformer
- pytorch
- speechbrain
- hf-asr-leaderboard
license: apache-2.0
datasets:
- librispeech
metrics:
- wer
- cer
model-index:
- name: Transformer+TransformerLM by SpeechBrain
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
      value: 2.49
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
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
      value: 6.03
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Small conformer (13M parameters) for LibriSpeech (with Transformer LM)

This repository provides all the necessary tools to perform automatic speech
recognition from an end-to-end system pretrained on LibriSpeech (EN) within
SpeechBrain. For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). 
The performance of the model is the following:

| Release | Test clean WER | Test other WER | GPUs |
|:-------------:|:--------------:|:--------------:|:--------:|
| 24-03-22 | 2.49 | 6.03 | 1xV100 32GB |

## Pipeline description

This ASR system is composed of 3 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units and trained with
the train transcriptions of LibriSpeech.
- Neural language model (Transformer LM) trained on the full 10M words dataset.
- Acoustic model made of a small conformer encoder and a joint decoder with CTC +
transformer. Hence, the decoding also incorporates the CTC probabilities.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Transcribing your own audio files (in English)

```python
from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-conformersmall-transformerlm-librispeech", savedir="pretrained_models/asr-conformersmall-transformerlm-librispeech")
asr_model.transcribe_file("speechbrain/asr-conformersmall-transformerlm-librispeech/example.wav")

```
### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

## Parallel Inference on a Batch
Please, [see this Colab notebook](https://colab.research.google.com/drive/1hX5ZI9S4jHIjahFCZnhwwQmFoGAi3tmu?usp=sharing) to figure out how to transcribe in parallel a batch of input sentences using a pre-trained model.

### Training
The model was trained with SpeechBrain (Commit hash: 'f73fcc35').
To train it from scratch follow these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```bash
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Run Training:
```bash
cd recipes/LibriSpeech/ASR/transformer
python train.py hparams/conformer_small.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1I4qntoodHCcj1JNbDrfwFHYcLyu1S5-l?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/


# **Citing SpeechBrain**
Please, cite SpeechBrain if you use it for your research or business.


```bibtex
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}
```

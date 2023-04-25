---
license: bsd-3-clause
language: en
tags:
- pytorch
- audio
- text-to-speech
- maui
---

# Maui TTS base model (Tacotron2 + Hifi-gan)

We use a recurrent sequence-to-sequence Mel-spectrogram prediction network based on Google's Tacotron2 as a baseline. It achieves good performance, has been tested in multiple different contexts and gives a very realistic rendering of a speaker's characteristics. On the vocoder side we replaced Google's original Wavenet synthesizer with the recent Hifi-Gan vocoder for improved realistic speech prosody and faster training.

### How to use
Usage based on Maui python library

```python

# IMPORTS
import json
import os
from omegaconf import OmegaConf

from maui.utils.tacotron2 import text2seq
from maui.utils.hifigan import AttrDict
from maui.models.hifigan import Generator
from maui.models.tacotron2 import Tacotron2

# PATHS
MODEL_DIR = "models"
TACO_CONF = os.path.join(MODEL_DIR, "maui-tacotron2.yaml")
OBAMA_CKPT = os.path.join(MODEL_DIR, "obama", "checkpoint_9000")
HIFIGAN_CKPT = os.path.join(MODEL_DIR, "hifigan", "UNIVERSAL_V1", "g_02500000")
HIFIGAN_CONF = os.path.join(MODEL_DIR,"hifigan", "UNIVERSAL_V1","config.json")

# DEVICE FOR INFERENCE
device = torch.device('cuda')
#device = torch.device('cpu')

# MODEL SETUP
taco_cfg = OmegaConf.load(TACO_CONF)
taco = Tacotron2(taco_cfg.model).to(device).share_memory()
taco = taco.setup_inference(OBAMA_CKPT, device=device)
with open(HIFIGAN_CONF, 'r') as f:
    data = f.read()
hifigan_cfg = AttrDict(json.loads(data))
hifigan = Generator(hifigan_cfg).to(device).share_memory()
hifigan = hifigan.setup_inference(HIFIGAN_CKPT, device=device)

# TEXT NORMALIZATION
text = "This is the sentence that will be spoken in the voice of Pr. Obama"
sequence = text2seq(text, device=device)

# INFERENCE
_, mel_outputs_postnet, _, _ = taco.inference(sequence)
audio = hifigan.inference(mel_outputs_postnet, device=device)

```

## Training data

To train these models, we need parallel corpora of speech and corresponding transcripts of the speaker we are modeling. The training data can be extracted from audiobooks. In this case ["A promised land"](https://www.amazon.com/A-Promised-Land-Obama-Audiobook/dp/B08HGH9JMF) purchased on Audible.

## Training procedure

### Ground Truth: 
The ground truth for the transcripts is obtained by sending the full Webex meetings to a third-party transcription service.
Text Normalization: We are modeling a speaker's voice so we need to normalize the text transcript in a way that makes the pronunciation of every word explicit. We need audio and its corresponding text representation to match as much as possible. For instance written numbers like '2020' should normalize to 'twenty twenty', 'Mr.' to 'Mister', etc. 
### Speech Segmentation:
The first step is to segment the speech into sentence-like snippets of audio of no more than 10 s. so the data can fit on our GPUs and segments represent a rather natural input length. For this task, we used the energy-based WebRTC Voice Activity Detection (VAD) because of its speed, flexibility through the 'aggressiveness' parameter and robustness to noise.
### Speech and Text Alignments
Once we have sentence-like audio segments of speech extracted by the VAD, we need to map these to the corresponding text transcript. The challenge at stake here is that we have a global transcript for the whole meeting giving by the third-party but need a segment-based transcript. One way we solved this is by using Voicea's transcription service for each audio segment. Since the transcription is not 100% accurate we further string-matched it with the global third-party ground-truth to correct potential mistakes in the segment-based automatic transcription.
### Mel spectrogram
Our model operates at an intermediary representation of audio, the Mel-spectrogram, which can be easily computed offline using Fast Fourier Transform-based algorithms.
For each sentence-like utterance we now have an audio waveform, its Mel-spectrogram representation and an accurate normalized text transcription. We are ready to train!

### BibTeX entry and citation info

```bibtex
@article{Sanh2019DistilBERTAD,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.01108}
}
```
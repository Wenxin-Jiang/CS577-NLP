---
language:
- en
library_name: nemo
datasets:
- ljspeech
thumbnail: null
tags:
- text-to-speech
- speech
- audio
- Transformer
- pytorch
- NeMo
- Riva
license: cc-by-4.0
---
# NVIDIA FastPitch (en-US)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-FastPitch--Transformer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-45M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-en--US-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |

FastPitch [1] is a fully-parallel transformer architecture with prosody control over pitch and individual phoneme duration. Additionally, it uses an unsupervised speech-text aligner [2]. See the [model architecture](#model-architecture) section for complete architecture details.

It is also compatible with NVIDIA Riva for [production-grade server deployments](#deployment-with-nvidia-riva). 


## Usage

The model is available for use in the NeMo toolkit [3] and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed the latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

Note: This model generates only spectrograms and a vocoder is needed to convert the spectrograms to waveforms.
In this example HiFiGAN is used.

```python
# Load FastPitch
from nemo.collections.tts.models import FastPitchModel
spec_generator = FastPitchModel.from_pretrained("nvidia/tts_en_fastpitch")

# Load vocoder
from nemo.collections.tts.models import HifiGanModel
model = HifiGanModel.from_pretrained(model_name="nvidia/tts_hifigan")
```

### Generate audio

```python
import soundfile as sf
parsed = spec_generator.parse("You can type your sentence here to get nemo to produce speech.")
spectrogram = spec_generator.generate_spectrogram(tokens=parsed)
audio = model.convert_spectrogram_to_audio(spec=spectrogram)
```

### Save the generated audio file

```python
# Save the audio to disk in a file called speech.wav
sf.write("speech.wav", audio.to('cpu').detach().numpy()[0], 22050)
```


### Input

This model accepts batches of text.

### Output

This model generates mel spectrograms.

## Model Architecture

FastPitch is a fully-parallel text-to-speech model based on FastSpeech, conditioned on fundamental frequency contours. The model predicts pitch contours during inference. By altering these predictions, the generated speech can be more expressive, better match the semantic of the utterance, and in the end more engaging to the listener. FastPitch is based on a fully-parallel Transformer architecture, with a much higher real-time factor than Tacotron2 for the mel-spectrogram synthesis of a typical utterance. It uses an unsupervised speech-text aligner.


## Training

The NeMo toolkit [3] was used for training the models for 1000 epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/tts/fastpitch.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/tts/conf/fastpitch_align_v1.05.yaml).


### Datasets

This model is trained on LJSpeech sampled at 22050Hz, and has been tested on generating female English voices with an American accent.

## Performance

No performance information is available at this time.

## Limitations
This checkpoint only works well with vocoders that were trained on 22050Hz data. Otherwise, the generated audio may be scratchy or choppy-sounding.

## Deployment with NVIDIA Riva
For the best real-time accuracy, latency, and throughput, deploy the model with [NVIDIA Riva](https://developer.nvidia.com/riva), an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, at the edge, and embedded. 
Additionally, Riva provides: 
* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and Enterprise-grade support 
Check out [Riva live demo](https://developer.nvidia.com/riva#demos).
## References
- [1] [FastPitch: Parallel Text-to-speech with Pitch Prediction](https://arxiv.org/abs/2006.06873)
- [2] [One TTS Alignment To Rule Them All](https://arxiv.org/abs/2108.10447)
- [3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
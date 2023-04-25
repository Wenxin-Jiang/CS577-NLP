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
- Vocoder
- GAN
- pytorch
- NeMo
- Riva
license: cc-by-4.0
---
# NVIDIA Hifigan Vocoder (en-US)
<style>
img {
 display: inline;
}
</style>
| [![Model architecture](https://img.shields.io/badge/Model_Arch-HiFiGAN--GAN-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-85M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-en--US-lightgrey#model-badge)](#datasets)
| [![Riva Compatible](https://img.shields.io/badge/NVIDIA%20Riva-compatible-brightgreen#model-badge)](#deployment-with-nvidia-riva) |

HiFiGAN [1] is a generative adversarial network (GAN) model that generates audio from mel spectrograms. The generator uses transposed convolutions to upsample mel spectrograms to audio.
 
## Usage

The model is available for use in the NeMo toolkit [2] and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.
To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed the latest PyTorch version.

```
pip install nemo_toolkit['all']
```

### Automatically instantiate the model

NOTE: In order to generate audio, you also need a spectrogram generator from NeMo. This example uses the FastPitch model.

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
sf.write("speech.wav", audio.to('cpu').numpy(), 22050)
```

### Input

This model accepts batches of mel spectrograms.

### Output

This model outputs audio at 22050Hz.

## Model Architecture

HiFi-GAN [1] consists of one generator and two discriminators: multi-scale and multi-period discriminators. The generator and discriminators are trained adversarially, along with two additional losses for
improving training stability and model performance.

## Training

The NeMo toolkit [3] was used for training the models for several epochs. These model are trained with this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/tts/hifigan.py) and this [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/tts/conf/hifigan/hifigan.yaml).

### Datasets

This model is trained on LJSpeech sampled at 22050Hz, and has been tested on generating female English voices with an American accent.

## Performance

No performance information is available at this time.

## Limitations

If the spectrogram generator model (example FastPitch) is trained/finetuned on new speaker's data it is recommended to finetune HiFi-GAN also. HiFi-GAN shows improvement using synthesized mel spectrograms, so the first step is to generate mel spectrograms with our finetuned FastPitch model to use as input to finetune HiFiGAN.

## Deployment with NVIDIA Riva

For the best real-time accuracy, latency, and throughput, deploy the model with [NVIDIA Riva](https://developer.nvidia.com/riva), an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, at the edge, and embedded. 
Additionally, Riva provides: 
* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and Enterprise-grade support 
Check out [Riva live demo](https://developer.nvidia.com/riva#demos).

## References

- [1] [HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis](https://arxiv.org/abs/2010.05646)
- [2] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)
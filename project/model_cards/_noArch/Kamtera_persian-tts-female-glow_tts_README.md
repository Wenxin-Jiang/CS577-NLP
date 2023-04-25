---
library_name: TTS
task: text-to-speech
tags:
- Persian
- TTS
- Farsi
- Coqui
- CoquiTTS
- pytorch
- audio
- text-to-speech
language: fa
datasets:
- persian-tts-dataset-famale
widget:
- text: ".زندگی فقط یک بار است؛ از آن به خوبی استفاده کن"
  example_title: "Hello, this is a test run."
---

# **persian-tts-female-glow_tts**

- persian-tts-female glow_tts model for text to speech purposes.
- Persian  فارسی
- Single-speaker female voice
- Trained on [persian-tts-dataset-famale](https://www.kaggle.com/datasets/magnoliasis/persian-tts-dataset-famale)
- [GitHub Repo](https://github.com/karim23657/Persian-tts-coqui)
# **Uses**

Install dependencies:
```python
!pip install TTS
!sudo apt-get -y install espeak-ng
```

Generate audio from text:

##### using cli:
```python
!tts --text "زندگی فقط یک بار است؛ از آن به خوبی استفاده کن" \
     --model_path "/coqui_training/run-July-31-2022_10+54AM-0000000/checkpoint_24000.pth" \
     --config_path "/coqui_training/run-July-31-2022_10+54AM-0000000/config.json" \
     --out_path "speech1.wav"
```
##### python api:

```python

from TTS.config import load_config
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

basepath="/train_output/run-December-24-2022_09+28AM-0000000"
config=basepath+"/config.json" 
model=basepath+"/best_model.pth"

model_path =model # Absolute path to the model checkpoint.pth
config_path =config # Absolute path to the model config.json

text=".زندگی فقط یک بار است؛ از آن به خوبی استفاده کن"

synthesizer = Synthesizer(
    model_path, config_path
)
wavs = synthesizer.tts(text)
synthesizer.save_wav(wavs, 'sp.wav')
```
Display audio:


```python
import IPython
IPython.display.Audio('sp.wav')
```


- **Hours used:** 10
- **Cloud Provider:** kaggle



# **How to Get Started with the Model**

Use the training code on this repo https://github.com/karim23657/Persian-tts-coqui .

<details>
<summary> Click to expand </summary>

More information needed

</details>

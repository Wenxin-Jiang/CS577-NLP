---
language: fa
datasets:
- common_voice_6_1
tags:
- audio
- automatic-speech-recognition
license: mit
widget:
- example_title: Common Voice Sample 1
  src: https://datasets-server.huggingface.co/assets/common_voice/--/fa/train/0/audio/audio.mp3
- example_title: Common Voice Sample 2
  src: https://datasets-server.huggingface.co/assets/common_voice/--/fa/train/1/audio/audio.mp3
model-index:
- name: Sharif-wav2vec2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice Corpus 6.1 (clean)
      type: common_voice_6_1
      config: clean
      split: test
      args: 
        language: fa
    metrics:
    - name: Test WER
      type: wer
      value: 6.0
---

# Sharif-wav2vec2

This is a fine-tuned version of Sharif Wav2vec2 for Farsi. The base model went through a fine-tuning process in which 108 hours of Commonvoice's Farsi samples with a sampling rate equal to 16kHz. Afterward, we trained a 5gram using [kenlm](https://github.com/kpu/kenlm) toolkit and used it in the processor which increased our accuracy on online ASR.

## Usage 

When using the model, ensure that your speech input is sampled at 16Khz. Prior to the usage, you may need to install the below dependencies:

```shell
pip install pyctcdecode
pip install pypi-kenlm
```

For testing, you can use the hosted inference API at the hugging face (There are provided examples from common-voice). It may take a while to transcribe the given voice; Or you can use the bellow code for a local run:

```python
import tensorflow
import torchaudio
import torch
import numpy as np

from transformers import AutoProcessor, AutoModelForCTC

processor = AutoProcessor.from_pretrained("SLPL/Sharif-wav2vec2")
model = AutoModelForCTC.from_pretrained("SLPL/Sharif-wav2vec2")

speech_array, sampling_rate = torchaudio.load("path/to/your.wav")
speech_array = speech_array.squeeze().numpy()

features = processor(
    speech_array,
    sampling_rate=processor.feature_extractor.sampling_rate,
    return_tensors="pt",
    padding=True)

with torch.no_grad():
    logits = model(
        features.input_values,
        attention_mask=features.attention_mask).logits
    prediction = processor.batch_decode(logits.numpy()).text

print(prediction[0])
# تست
```

## Evaluation

For the evaluation, you can use the code below. Ensure your dataset to be in following form in order to avoid any further conflict:

| path | reference|
|:----:|:--------:|
| path/to/audio_file.wav | "TRANSCRIPTION" |

also, make sure you have installed `pip install jiwer` prior to running.

```python
import tensorflow
import torchaudio
import torch
import librosa
from datasets import load_dataset,load_metric
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from transformers import Wav2Vec2ProcessorWithLM

model = Wav2Vec2ForCTC.from_pretrained("SLPL/Sharif-wav2vec2") 
processor = Wav2Vec2ProcessorWithLM.from_pretrained("SLPL/Sharif-wav2vec2") 

def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    speech_array = speech_array.squeeze().numpy()
    speech_array = librosa.resample(
        np.asarray(speech_array),
        sampling_rate,
        processor.feature_extractor.sampling_rate)
    batch["speech"] = speech_array
    return batch

def predict(batch):
    features = processor(
        batch["speech"], 
        sampling_rate=processor.feature_extractor.sampling_rate, 
        return_tensors="pt", 
        padding=True
    )

    with torch.no_grad():
        logits = model(
            features.input_values,
            attention_mask=features.attention_mask).logits
    batch["prediction"] = processor.batch_decode(logits.numpy()).text
    return batch
    
dataset = load_dataset(
    "csv",
    data_files={"test":"dataset.eval.csv"},
    delimiter=",")["test"]
dataset = dataset.map(speech_file_to_array_fn)

result = dataset.map(predict, batched=True, batch_size=4)
wer = load_metric("wer")

print("WER: {:.2f}".format(wer.compute(
    predictions=result["prediction"],
    references=result["reference"])))
```

*Result (WER) on common-voice 6.1*:

| cleaned | other |
|:---:|:---:|
| 0.06 | 0.16 |


## Citation
If you want to cite this model you can use this:

```bibtex
?
```

### Contributions

Thanks to [@sarasadeghii](https://github.com/Sarasadeghii) and [@sadrasabouri](https://github.com/sadrasabouri) for adding this dataset.

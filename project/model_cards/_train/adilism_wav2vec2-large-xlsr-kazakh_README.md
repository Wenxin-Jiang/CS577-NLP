---
language: kk
datasets:
- kazakh_speech_corpus
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Wav2Vec2-XLSR-53 Kazakh by adilism
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Kazakh Speech Corpus v1.1
      type: kazakh_speech_corpus
      args: kk
    metrics:
       - name: Test WER
         type: wer
         value: 19.65
---

# Wav2Vec2-Large-XLSR-53-Kazakh

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) for Kazakh ASR using the [Kazakh Speech Corpus v1.1](https://issai.nu.edu.kz/kz-speech-corpus/?version=1.1)

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

from utils import get_test_dataset

test_dataset = get_test_dataset("ISSAI_KSC_335RS_v1.1")

processor = Wav2Vec2Processor.from_pretrained("wav2vec2-large-xlsr-kazakh")
model = Wav2Vec2ForCTC.from_pretrained("wav2vec2-large-xlsr-kazakh")


# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = torchaudio.transforms.Resample(sampling_rate, 16_000)(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:2])
```


## Evaluation

The model can be evaluated as follows on the test set of [Kazakh Speech Corpus v1.1](https://issai.nu.edu.kz/kz-speech-corpus/?version=1.1). To evaluate, download the [archive](https://www.openslr.org/resources/102/ISSAI_KSC_335RS_v1.1_flac.tar.gz), untar and pass the path to data to `get_test_dataset` as below:

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

from utils import get_test_dataset

test_dataset = get_test_dataset("ISSAI_KSC_335RS_v1.1")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("adilism/wav2vec2-large-xlsr-kazakh")
model = Wav2Vec2ForCTC.from_pretrained("adilism/wav2vec2-large-xlsr-kazakh")
model.to("cuda")


# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = torchaudio.transforms.Resample(sampling_rate, 16_000)(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

def evaluate(batch):
    inputs = processor(batch["text"], sampling_rate=16_000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 19.65%


## Training

The Kazakh Speech Corpus v1.1 `train` dataset was used for training.
---
language: Guj
datasets:
- google
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Guj by Jaimin
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Google
      type: voice
      args: guj
    metrics:
       - name: Test WER
         type: wer
         value: 28.92
---

# wav2vec2-base-gujarati-demo

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) in Guj
When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

common_voice_train,common_voice_test = load_dataset('csv', data_files={'train': 'train.csv','test': 'test.csv'},error_bad_lines=False,encoding='utf-8',split=['train', 'test']).

processor = Wav2Vec2Processor.from_pretrained("jaimin/wav2vec2-base-gujarati-demo")
model = Wav2Vec2ForCTC.from_pretrained("jaimin/wav2vec2-base-gujarati-demo")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = common_voice_test.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
     logits = model(inputs.input_values).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][0].lower())
```


## Evaluation

The model can be evaluated as follows on the {language} test data of Common Voice.


```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

common_voice_validation = load_dataset('csv', data_files={'test': 'validation.csv'},error_bad_lines=False,encoding='utf-8',split='test')
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("jaimin/wav2vec2-base-gujarati-demo")
model = Wav2Vec2ForCTC.from_pretrained("Amrrs/wav2vec2-base-gujarati-demo")
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“]'
resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = common_voice_validation.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda")).logits
    
    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

result = common_voice_validation.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 28.92 %


## Training

The Google datasets were used for training.

The script used for training can be found [here](https://colab.research.google.com/drive/1-Klkgr4f-C9SanHfVC5RhP0ELUH6TYlN?usp=sharing)

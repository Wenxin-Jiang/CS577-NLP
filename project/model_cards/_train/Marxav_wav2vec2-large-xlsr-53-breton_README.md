---
language: br
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Breton by Marxav
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice br
      type: common_voice
      args: br
    metrics:
       - name: Test WER
         type: wer
         value: 43.43
---
# wav2vec2-large-xlsr-53-breton
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

lang = "br"
test_dataset = load_dataset("common_voice", lang, split="test[:2%]") 

processor = Wav2Vec2Processor.from_pretrained("Marxav/wav2vec2-large-xlsr-53-breton") 
model = Wav2Vec2ForCTC.from_pretrained("Marxav/wav2vec2-large-xlsr-53-breton")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

chars_to_ignore_regex = '[\\,\,\?\.\!\;\:\"\“\%\”\�\(\)\/\«\»\½\…]'

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
   speech_array, sampling_rate = torchaudio.load(batch["path"])
   batch["speech"] = resampler(speech_array).squeeze().numpy()
   batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
   batch["sentence"] = re.sub("ʼ", "'", batch["sentence"])
   batch["sentence"] = re.sub("’", "'", batch["sentence"])
   batch["sentence"] = re.sub('‘', "'", batch["sentence"])
   return batch

nb_samples = 2
test_dataset = test_dataset.map(speech_file_to_array_fn)

inputs = processor(test_dataset["speech"][:nb_samples], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
   logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:nb_samples])
```
The above code leads to the following prediction for the first two samples:
* Prediction: ["neller ket dont a-benn eus netra la vez ser merc'hed evel sich", 'an eil hag egile']
* Reference: ["N'haller ket dont a-benn eus netra pa vezer nec'het evel-se.", 'An eil hag egile.']

The model can be evaluated as follows on the {language} test data of Common Voice.
```python
import re
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

lang = 'br'
test_dataset = load_dataset("common_voice", lang, split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained('Marxav/wav2vec2-large-xlsr-53-breton')
model = Wav2Vec2ForCTC.from_pretrained('Marxav/wav2vec2-large-xlsr-53-breton')
model.to("cuda")

chars_to_ignore_regex = '[\\,\,\?\.\!\;\:\"\“\%\”\�\(\)\/\«\»\½\…]'

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
  batch["sentence"] = re.sub("ʼ", "'", batch["sentence"])
  batch["sentence"] = re.sub("’", "'", batch["sentence"])
  batch["sentence"] = re.sub('‘', "'", batch["sentence"])
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  batch["speech"] = resampler(speech_array).squeeze().numpy()
  return batch

test_dataset = test_dataset.map(remove_special_characters)

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def evaluate(batch):
  inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

  with torch.no_grad():
    logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)
  batch["pred_strings"] = processor.batch_decode(pred_ids)
  return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 43.43%
## Training
The Common Voice `train`, `validation` datasets were used for training.
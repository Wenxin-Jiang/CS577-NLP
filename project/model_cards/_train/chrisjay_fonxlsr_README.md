---
language: fon
datasets:
- fon_dataset 
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
- hf-asr-leaderboard
license: apache-2.0
model-index:
- name: Fon XLSR Wav2Vec2 Large 53
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: fon
      type: fon_dataset
      args: fon
    metrics:
       - name: Test WER
         type: wer
         value: 14.97
---
# Wav2Vec2-Large-XLSR-53-Fon

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on [Fon (or Fongbe)](https://en.wikipedia.org/wiki/Fon_language) using the [Fon Dataset](https://github.com/laleye/pyFongbe/tree/master/data).

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import json
import random
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


#Load test_dataset from saved files in folder
from datasets import load_dataset, load_metric

#for test
for root, dirs, files in os.walk(test/):
  test_dataset= load_dataset("json", data_files=[os.path.join(root,i) for i in files],split="train")

#Remove unnecessary chars
chars_to_ignore_regex = '[\\,\\?\\.\\!\\-\\;\\:\\"\\“\\%\\‘\\”]'
def remove_special_characters(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
    return batch

test_dataset = test_dataset.map(remove_special_characters)

processor = Wav2Vec2Processor.from_pretrained("chrisjay/wav2vec2-large-xlsr-53-fon") 
model = Wav2Vec2ForCTC.from_pretrained("chrisjay/wav2vec2-large-xlsr-53-fon") 

#No need for resampling because audio dataset already at 16kHz
#resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  batch["speech"]=speech_array.squeeze().numpy()
  return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
  tlogits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:2])
```


## Evaluation

The model can be evaluated as follows on our unique Fon test data. 

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

for root, dirs, files in os.walk(test/):
  test_dataset = load_dataset("json", data_files=[os.path.join(root,i) for i in files],split="train")

chars_to_ignore_regex = '[\\,\\?\\.\\!\\-\\;\\:\\"\\“\\%\\‘\\”]'
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
    return batch

test_dataset = test_dataset.map(remove_special_characters)
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("chrisjay/wav2vec2-large-xlsr-53-fon")
model = Wav2Vec2ForCTC.from_pretrained("chrisjay/wav2vec2-large-xlsr-53-fon")
model.to("cuda")

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = speech_array[0].numpy()
    batch["sampling_rate"] = sampling_rate
    batch["target_text"] = batch["sentence"]
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

#Evaluation on test dataset
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

**Test Result**: 14.97 % 

## Training

The [Fon dataset](https://github.com/laleye/pyFongbe/tree/master/data) was split into `train`(8235 samples), `validation`(1107 samples), and `test`(1061 samples).

The script used for training can be found [here](https://colab.research.google.com/drive/11l6qhJCYnPTG1TQZ8f3EvKB9z12TQi4g?usp=sharing)


# Collaborators on this project

  - Chris C. Emezue  ([Twitter](https://twitter.com/ChrisEmezue))|(chris.emezue@gmail.com)
  - Bonaventure F.P. Dossou (HuggingFace Username: [bonadossou](https://huggingface.co/bonadossou))|([Twitter](https://twitter.com/bonadossou))|(femipancrace.dossou@gmail.com)
      
## This is a joint project continuing our research on [OkwuGbé: End-to-End Speech Recognition for Fon and Igbo](https://arxiv.org/abs/2103.07762)
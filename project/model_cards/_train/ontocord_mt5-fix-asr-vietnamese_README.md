---
language: vi
datasets:
- common_voice
- FOSD: https://data.mendeley.com/datasets/k9sxg2twv4/4
metrics:
- wer
tags:
- language-modeling
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: MT5 Fix Asr Vietnamese by Ontocord
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice vi
      type: common_voice
      args: vi
    metrics:
       - name: Test WER
         type: wer
         value: 25.207182
---

# Ontocord/mt5-fix-asr-vietnamese
Fine-tuned mt5 to correct output of an ASR model trained on [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) which was trained on Vietnamese using the [Common Voice](https://huggingface.co/datasets/common_voice), and [FOSD](https://data.mendeley.com/datasets/k9sxg2twv4/4).

## Usage
The model can be used directly by submitting vietnamese asr text, but is is best to use with the ontocord/wav2vec2-large-xlsr-vietnamese model.

```
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, pipelines

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_dataset = load_dataset("common_voice", "vi", split="test[:2%]") 
processor = Wav2Vec2Processor.from_pretrained("ontocord/wav2vec2-large-xlsr-53-vietnamese") 
model = Wav2Vec2ForCTC.from_pretrained("ontocord/wav2vec2-large-xlsr-53-vietnamese").to(device) 
mt5 = pipelines.pipeline("text2text-generation","ontocord/mt5-fix-asr-vietnamese", device=0 if device == "cuda" else -1)
resampler = torchaudio.transforms.Resample(48_000, 16_000)
# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
	speech_array, sampling_rate = torchaudio.load(batch["path"])
	batch["speech"] = resampler(speech_array).squeeze().numpy()
	return batch
test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)
with torch.no_grad():
	logits = model(inputs.input_values.to(device), attention_mask=inputs.attention_mask.to(device)).logits
predicted_ids = torch.argmax(logits, dim=-1)
print("Prediction:", [aHash['generated_text'] for aHash in mt5(processor.batch_decode(predicted_ids), max_length=100)])
print("Reference:", test_dataset["sentence"][:2])
```

## Evaluation
The model can be evaluated as follows on the Vietnamese test data of Common Voice.
```
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, pipelines
import re
test_dataset = load_dataset("common_voice", "vi", split="test")
wer = load_metric("wer")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = Wav2Vec2Processor.from_pretrained("ontocord/wav2vec2-large-xlsr-vietnamese")
model = Wav2Vec2ForCTC.from_pretrained("ontocord/wav2vec2-large-xlsr-vietnamese").to(device)
mt5 = pipelines.pipeline("text2text-generation","ontocord/mt5-fix-asr-vietnamese", device=0 if device == "cuda" else -1)
chars_to_ignore_regex = '[\\\+\@\ǀ\,\?\.\!\-\;\:\"\“\%\‘\”\�]'
resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  batch["speech"] = resampler(speech_array).squeeze().numpy()
  return batch
test_dataset = test_dataset.map(speech_file_to_array_fn)

# you may also want to use the  decode_string from https://huggingface.co/Nhut/wav2vec2-large-xlsr-vietnamese
def evaluate(batch):
  inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)
  with torch.no_grad():
    logits = model(inputs.input_values.to(device), attention_mask=inputs.attention_mask.to(device)).logits
    pred_ids = torch.argmax(logits, dim=-1)
    max_length = int(pred_ids.size()[1])
    txt = [aHash['generated_text'].strip() for aHash in mt5(processor.batch_decode(pred_ids), max_length=max_length)]
    batch["pred_strings"] = txt
  return batch
result = test_dataset.map(evaluate, batched=True, batch_size=8)
print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```
**Test Result**: 25.207182
## Training
The Common Voice train, validation, and FPT datasets were used for training.
The script used for training can be found here # TODO
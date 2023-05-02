---
language: vi
datasets:
- common_voice
- FOSD: https://data.mendeley.com/datasets/k9sxg2twv4/4
- VIVOS: https://ailab.hcmus.edu.vn/vivos
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Vietnamese by Nhut
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
         value: 49.59
---
# Wav2Vec2-Large-XLSR-53-Vietnamese
Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Vietnamese using the [Common Voice](https://huggingface.co/datasets/common_voice), [FOSD](https://data.mendeley.com/datasets/k9sxg2twv4/4) and [VIVOS](https://ailab.hcmus.edu.vn/vivos).
When using this model, make sure that your speech input is sampled at 16kHz.
## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
ENCODER = {
    "ia ": "iê ",
    "ìa ": "iề ",
    "ía ": "iế ",
    "ỉa ": "iể ",
    "ĩa ": "iễ ",
    "ịa ": "iệ ",
    "ya ": "yê ",
    "ỳa ": "yề ",
    "ýa ": "yế ",
    "ỷa ": "yể ",
    "ỹa ": "yễ ",
    "ỵa ": "yệ ",
    "ua ": "uô ",
    "ùa ": "uồ ",
    "úa ": "uố ",
    "ủa ": "uổ ",
    "ũa ": "uỗ ",
    "ụa ": "uộ ",
    "ưa ": "ươ ",
    "ừa ": "ườ ",
    "ứa ": "ướ ",
    "ửa ": "ưở ",
    "ữa ": "ưỡ ",
    "ựa ": "ượ ",
    "ke": "ce",
    "kè": "cè",
    "ké": "cé",
    "kẻ": "cẻ",
    "kẽ": "cẽ",
    "kẹ": "cẹ",
    "kê": "cê",
    "kề": "cề",
    "kế": "cế",
    "kể": "cể",
    "kễ": "cễ",
    "kệ": "cệ",
    "ki": "ci",
    "kì": "cì",
    "kí": "cí",
    "kỉ": "cỉ",
    "kĩ": "cĩ",
    "kị": "cị",
    "ky": "cy",
    "kỳ": "cỳ",
    "ký": "cý",
    "kỷ": "cỷ",
    "kỹ": "cỹ",
    "kỵ": "cỵ",
    "ghe": "ge",
    "ghè": "gè",
    "ghé": "gé",
    "ghẻ": "gẻ",
    "ghẽ": "gẽ",
    "ghẹ": "gẹ",
    "ghê": "gê",
    "ghề": "gề",
    "ghế": "gế",
    "ghể": "gể",
    "ghễ": "gễ",
    "ghệ": "gệ",
    "ngh": "\x80",
    "uyê": "\x96",
    "uyề": "\x97",
    "uyế": "\x98",
    "uyể": "\x99",
    "uyễ": "\x9a",
    "uyệ": "\x9b",
    "ng": "\x81",
    "ch": "\x82",
    "gh": "\x83",
    "nh": "\x84",
    "gi": "\x85",
    "ph": "\x86",
    "kh": "\x87",
    "th": "\x88",
    "tr": "\x89",
    "uy": "\x8a",
    "uỳ": "\x8b",
    "uý": "\x8c",
    "uỷ": "\x8d",
    "uỹ": "\x8e",
    "uỵ": "\x8f",
    "iê": "\x90",
    "iề": "\x91",
    "iế": "\x92",
    "iể": "\x93",
    "iễ": "\x94",
    "iệ": "\x95",
    "uô": "\x9c",
    "uồ": "\x9d",
    "uố": "\x9e",
    "uổ": "\x9f",
    "uỗ": "\xa0",
    "uộ": "\xa1",
    "ươ": "\xa2",
    "ườ": "\xa3",
    "ướ": "\xa4",
    "ưở": "\xa5",
    "ưỡ": "\xa6",
    "ượ": "\xa7",
}
  
def decode_string(x):
  for k, v in list(reversed(list(ENCODER.items()))):
    x = x.replace(v, k)
  return x
test_dataset = load_dataset("common_voice", "vi", split="test[:2%]") 
processor = Wav2Vec2Processor.from_pretrained("Nhut/wav2vec2-large-xlsr-vietnamese")
model = Wav2Vec2ForCTC.from_pretrained("Nhut/wav2vec2-large-xlsr-vietnamese")
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
  logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits
predicted_ids = torch.argmax(logits, dim=-1)
print("Prediction:", [decode_string(x) for x in processor.batch_decode(predicted_ids)])
print("Reference:", test_dataset["sentence"][:2])
```
## Evaluation
The model can be evaluated as follows on the Vietnamese test data of Common Voice.
```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

ENCODER = {
    "ia ": "iê ",
    "ìa ": "iề ",
    "ía ": "iế ",
    "ỉa ": "iể ",
    "ĩa ": "iễ ",
    "ịa ": "iệ ",
    "ya ": "yê ",
    "ỳa ": "yề ",
    "ýa ": "yế ",
    "ỷa ": "yể ",
    "ỹa ": "yễ ",
    "ỵa ": "yệ ",
    "ua ": "uô ",
    "ùa ": "uồ ",
    "úa ": "uố ",
    "ủa ": "uổ ",
    "ũa ": "uỗ ",
    "ụa ": "uộ ",
    "ưa ": "ươ ",
    "ừa ": "ườ ",
    "ứa ": "ướ ",
    "ửa ": "ưở ",
    "ữa ": "ưỡ ",
    "ựa ": "ượ ",
    "ke": "ce",
    "kè": "cè",
    "ké": "cé",
    "kẻ": "cẻ",
    "kẽ": "cẽ",
    "kẹ": "cẹ",
    "kê": "cê",
    "kề": "cề",
    "kế": "cế",
    "kể": "cể",
    "kễ": "cễ",
    "kệ": "cệ",
    "ki": "ci",
    "kì": "cì",
    "kí": "cí",
    "kỉ": "cỉ",
    "kĩ": "cĩ",
    "kị": "cị",
    "ky": "cy",
    "kỳ": "cỳ",
    "ký": "cý",
    "kỷ": "cỷ",
    "kỹ": "cỹ",
    "kỵ": "cỵ",
    "ghe": "ge",
    "ghè": "gè",
    "ghé": "gé",
    "ghẻ": "gẻ",
    "ghẽ": "gẽ",
    "ghẹ": "gẹ",
    "ghê": "gê",
    "ghề": "gề",
    "ghế": "gế",
    "ghể": "gể",
    "ghễ": "gễ",
    "ghệ": "gệ",
    "ngh": "\x80",
    "uyê": "\x96",
    "uyề": "\x97",
    "uyế": "\x98",
    "uyể": "\x99",
    "uyễ": "\x9a",
    "uyệ": "\x9b",
    "ng": "\x81",
    "ch": "\x82",
    "gh": "\x83",
    "nh": "\x84",
    "gi": "\x85",
    "ph": "\x86",
    "kh": "\x87",
    "th": "\x88",
    "tr": "\x89",
    "uy": "\x8a",
    "uỳ": "\x8b",
    "uý": "\x8c",
    "uỷ": "\x8d",
    "uỹ": "\x8e",
    "uỵ": "\x8f",
    "iê": "\x90",
    "iề": "\x91",
    "iế": "\x92",
    "iể": "\x93",
    "iễ": "\x94",
    "iệ": "\x95",
    "uô": "\x9c",
    "uồ": "\x9d",
    "uố": "\x9e",
    "uổ": "\x9f",
    "uỗ": "\xa0",
    "uộ": "\xa1",
    "ươ": "\xa2",
    "ườ": "\xa3",
    "ướ": "\xa4",
    "ưở": "\xa5",
    "ưỡ": "\xa6",
    "ượ": "\xa7",
}

def decode_string(x):
  for k, v in list(reversed(list(ENCODER.items()))):
    x = x.replace(v, k)
  return x

test_dataset = load_dataset("common_voice", "vi", split="test")
wer = load_metric("wer")
processor = Wav2Vec2Processor.from_pretrained("Nhut/wav2vec2-large-xlsr-vietnamese")
model = Wav2Vec2ForCTC.from_pretrained("Nhut/wav2vec2-large-xlsr-vietnamese")
model.to("cuda")

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
# Preprocessing the datasets.
# We need to read the aduio files as arrays
def evaluate(batch):
  inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)
  with torch.no_grad():
    logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits
  pred_ids = torch.argmax(logits, dim=-1)
  batch["pred_strings"] = processor.batch_decode(pred_ids)
  # decode_string: We replace the encoded letter with the initial letters
  batch["pred_strings"] = [decode_string(x) for x in batch["pred_strings"]]
  return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)
print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```
**Test Result**: 49.59 % 
## Training
The Common Voice `train`, `validation` and FOSD datasets and VIVOS datasets were used for training as well.
The script used for training can be found [here](https://colab.research.google.com/drive/11pP4uVJj4SYZTzGjlCUtOHywlhYqs0cPx)
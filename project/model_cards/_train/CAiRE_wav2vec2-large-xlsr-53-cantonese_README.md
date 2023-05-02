---
language:
- yue
datasets:
- common_voice 
metrics:
- cer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Wav2Vec2-Large-XLSR-53-Cantonese
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice zh-HK
      type: common_voice
      args: zh-HK
    metrics:
       - name: Test CER
         type: cer
         value: [18.55%]
---

# Wav2Vec2-Large-XLSR-53-Cantonese

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Cantonese using the [Common Voice Corpus 8.0](https://commonvoice.mozilla.org/en/datasets).
When using this model, make sure that your speech input is sampled at 16kHz.

The Common Voice's validated `train` and `dev` were used for training.

The script used for training can be found at [https://github.com/holylovenia/wav2vec2-pretraining](https://github.com/holylovenia/wav2vec2-pretraining).

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "zh-HK", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("CAiRE/wav2vec2-large-xlsr-53-cantonese")
model = Wav2Vec2ForCTC.from_pretrained("CAiRE/wav2vec2-large-xlsr-53-cantonese")


# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  resampler = torchaudio.transforms.Resample(sampling_rate, 16_000)
  batch["speech"] = resampler(speech_array).squeeze().numpy()
  return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset[:2]["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
  logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset[:2]["sentence"])
```


## Evaluation

The model can be evaluated as follows on the zh-HK test data of Common Voice.

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "zh-HK", split="test")
wer = load_metric("cer")

processor = Wav2Vec2Processor.from_pretrained("CAiRE/wav2vec2-large-xlsr-53-cantonese")
model = Wav2Vec2ForCTC.from_pretrained("CAiRE/wav2vec2-large-xlsr-53-cantonese") 
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\'\”\�]'


# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  resampler = torchaudio.transforms.Resample(sampling_rate, 16_000)
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
  return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("CER: {:2f}".format(100 * cer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: CER: 18.55 %

## Citation

If you use our code/model, please cite us:

```
@inproceedings{lovenia2022ascend,
  title={ASCEND: A Spontaneous Chinese-English Dataset for Code-switching in Multi-turn Conversation},
  author={Lovenia, Holy and Cahyawijaya, Samuel and Winata, Genta Indra and Xu, Peng and Yan, Xu and Liu, Zihan and Frieske, Rita and Yu, Tiezheng and Dai, Wenliang and Barezi, Elham J and others},
  booktitle={Proceedings of the 13th Language Resources and Evaluation Conference (LREC)},
  year={2022}
}
```
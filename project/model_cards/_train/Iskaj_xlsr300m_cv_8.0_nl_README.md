---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- mozilla-foundation/common_voice_7_0
- nl
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R-300M - Dutch
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8 NL
      type: mozilla-foundation/common_voice_8_0
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 46.94
    - name: Test CER
      type: cer
      value: 21.65
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: ???
    - name: Test CER
      type: cer
      value: ???
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 42.56
---

# xlsr300m_cv_8.0_nl


#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Iskaj/xlsr300m_cv_8.0_nl --dataset mozilla-foundation/common_voice_8_0 --config nl --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id Iskaj/xlsr300m_cv_8.0_nl --dataset speech-recognition-community-v2/dev_data --config nl --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

### Inference

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio.functional as F

model_id = "Iskaj/xlsr300m_cv_8.0_nl"

sample_iter = iter(load_dataset("mozilla-foundation/common_voice_8_0", "nl", split="test", streaming=True, use_auth_token=True))

sample = next(sample_iter)
resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), 48_000, 16_000).numpy()

model = AutoModelForCTC.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

inputs = processor(resampled_audio, sampling_rate=16_000, return_tensors="pt")
with torch.no_grad():
  logits = model(**inputs).logits
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = processor.batch_decode(predicted_ids)

transcription[0].lower()
#'het kontine schip lag aangemeert in de aven'
```

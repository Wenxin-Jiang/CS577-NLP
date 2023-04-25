---
language:
- or
license: apache-2.0
tags:
- automatic-speech-recognition
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_7_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-or
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_7_0
      name: Common Voice 7
      args: or
    metrics:
    - type: wer
      value: 47.186
      name: Test WER
    - name: Test CER
      type: cer
      value: 11.82
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-or

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6618
- Wer: 0.5166

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.12
- num_epochs: 240

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 6.0493        | 23.53  | 400  | 2.9728          | 1.0    |
| 0.5306        | 47.06  | 800  | 1.2895          | 0.6138 |
| 0.1253        | 70.59  | 1200 | 1.6854          | 0.5703 |
| 0.0763        | 94.12  | 1600 | 1.9433          | 0.5870 |
| 0.0552        | 117.65 | 2000 | 1.4393          | 0.5575 |
| 0.0382        | 141.18 | 2400 | 1.4665          | 0.5537 |
| 0.0286        | 164.71 | 2800 | 1.5441          | 0.5320 |
| 0.0212        | 188.24 | 3200 | 1.6502          | 0.5115 |
| 0.0168        | 211.76 | 3600 | 1.6411          | 0.5332 |
| 0.0129        | 235.29 | 4000 | 1.6618          | 0.5166 |


### Framework versions

- Transformers 4.16.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3

#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_7_0` with split `test`

```bash
python eval.py --model_id anuragshas/wav2vec2-large-xls-r-300m-or --dataset mozilla-foundation/common_voice_7_0 --config or --split test
```


### Inference With LM

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio.functional as F
model_id = "anuragshas/wav2vec2-large-xls-r-300m-or"
sample_iter = iter(load_dataset("mozilla-foundation/common_voice_7_0", "or", split="test", streaming=True, use_auth_token=True))
sample = next(sample_iter)
resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), 48_000, 16_000).numpy()
model = AutoModelForCTC.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)
input_values = processor(resampled_audio, return_tensors="pt").input_values
with torch.no_grad():
    logits = model(input_values).logits
transcription = processor.batch_decode(logits.numpy()).text
# => "ପରରାଏ ବାଲା ଗସ୍ତି ଫାଣ୍ଡି ଗୋପାଳ ପରଠାରୁ ଦେଢ଼କଶ ଦୂର"
```

### Eval results on Common Voice 7 "test" (WER):

| Without LM | With LM (run `./eval.py`) |
|---|---|
| 51.92 | 47.186 |

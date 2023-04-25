---
language:
- mr
license: apache-2.0
tags:
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-mr
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_8_0
      name: Common Voice 8
      args: mr
    metrics:
    - type: wer
      value: 32.811
      name: Test WER
    - name: Test CER
      type: cer
      value: 7.692
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-mr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5479
- Wer: 0.5740

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 3.7378        | 18.18  | 400  | 3.5047          | 1.0    |
| 3.1707        | 36.36  | 800  | 2.6166          | 0.9912 |
| 1.4942        | 54.55  | 1200 | 0.5778          | 0.6927 |
| 1.2058        | 72.73  | 1600 | 0.5168          | 0.6362 |
| 1.0558        | 90.91  | 2000 | 0.5105          | 0.6069 |
| 0.9488        | 109.09 | 2400 | 0.5151          | 0.6089 |
| 0.8588        | 127.27 | 2800 | 0.5157          | 0.5989 |
| 0.7991        | 145.45 | 3200 | 0.5179          | 0.5740 |
| 0.7545        | 163.64 | 3600 | 0.5348          | 0.5740 |
| 0.7144        | 181.82 | 4000 | 0.5518          | 0.5724 |
| 0.7041        | 200.0  | 4400 | 0.5479          | 0.5740 |


### Framework versions

- Transformers 4.16.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.1
- Tokenizers 0.11.0

#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id anuragshas/wav2vec2-large-xls-r-300m-mr --dataset mozilla-foundation/common_voice_8_0 --config mr --split test
```


### Inference With LM

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio.functional as F
model_id = "anuragshas/wav2vec2-large-xls-r-300m-mr"
sample_iter = iter(load_dataset("mozilla-foundation/common_voice_8_0", "mr", split="test", streaming=True, use_auth_token=True))
sample = next(sample_iter)
resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), 48_000, 16_000).numpy()
model = AutoModelForCTC.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)
input_values = processor(resampled_audio, return_tensors="pt").input_values
with torch.no_grad():
    logits = model(input_values).logits
transcription = processor.batch_decode(logits.numpy()).text
# => "या पानास लेखाचे स्वरूप यायला हावे"
```

### Eval results on Common Voice 8 "test" (WER):

| Without LM | With LM (run `./eval.py`) |
|---|---|
| 49.177 | 32.811 |

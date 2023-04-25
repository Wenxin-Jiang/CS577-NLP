---
language:
- pa
license: apache-2.0
tags:
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_7_0
metrics:
- wer
model-index:
- name: XLS-R-300M - Punjabi
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_7_0
      name: Common Voice 7
      args: pa-IN
    metrics:
    - type: wer
      value: 45.611
      name: Test WER
    - name: Test CER
      type: cer
      value: 15.584
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLS-R-300M - Punjabi

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2548
- Wer: 0.5677

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
- num_epochs: 120
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 6.4804        | 16.65  | 400  | 1.8461          | 1.0    |
| 0.474         | 33.33  | 800  | 1.1018          | 0.6624 |
| 0.1389        | 49.98  | 1200 | 1.1918          | 0.6103 |
| 0.0919        | 66.65  | 1600 | 1.1889          | 0.6058 |
| 0.0657        | 83.33  | 2000 | 1.2266          | 0.5931 |
| 0.0479        | 99.98  | 2400 | 1.2512          | 0.5902 |
| 0.0355        | 116.65 | 2800 | 1.2548          | 0.5677 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3


#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_7_0` with split `test`

```bash
python eval.py --model_id anuragshas/wav2vec2-large-xls-r-300m-pa-in --dataset mozilla-foundation/common_voice_7_0 --config pa-IN --split test
```


### Inference With LM

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio.functional as F
model_id = "anuragshas/wav2vec2-large-xls-r-300m-pa-in"
sample_iter = iter(load_dataset("mozilla-foundation/common_voice_7_0", "pa-IN", split="test", streaming=True, use_auth_token=True))
sample = next(sample_iter)
resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), 48_000, 16_000).numpy()
model = AutoModelForCTC.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)
input_values = processor(resampled_audio, return_tensors="pt").input_values
with torch.no_grad():
    logits = model(input_values).logits
transcription = processor.batch_decode(logits.numpy()).text
# => "ਉਨ੍ਹਾਂ ਨੇ ਸਾਰੇ ਤੇਅਰਵੇ ਵੱਖਰੀ ਕਿਸਮ ਦੇ ਕੀਤੇ ਹਨ"
```

### Eval results on Common Voice 7 "test" (WER):

| Without LM | With LM (run `./eval.py`) |
|---|---|
| 51.968 | 45.611 |

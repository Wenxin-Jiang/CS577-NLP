---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
  name: wav2vec2-xls-r-300m-romanian
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
## This model achieves WER on common-voice ro test split of WER: 12.457178%
# wav2vec2-xls-r-300m-romanian

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on an common voice ro and RSS dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0836
- eval_wer: 0.0705
- eval_runtime: 160.4549
- eval_samples_per_second: 11.081
- eval_steps_per_second: 1.39
- epoch: 14.38
- step: 2703

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 15
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3


Used the following code for evaluation:
```
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "ro", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("Dumiiii/wav2vec2-xls-r-300m-romanian")
model = Wav2Vec2ForCTC.from_pretrained("Dumiiii/wav2vec2-xls-r-300m-romanian")
model.to("cuda")

chars_to_ignore_regex = '['+string.punctuation+']'
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
  return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

Credits for evaluation: https://huggingface.co/anton-l
---
language:
- mt
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- mt
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-1b-cv8-mt
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: mt
    metrics:
    - name: Test WER
      type: wer
      value: 17.57
    - name: Test CER
      type: cer
      value: 3.86
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: mt
    metrics:
    - name: Test WER
      type: wer
      value: null
    - name: Test CER
      type: cer
      value: null
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-1b-cv8-mt

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2210
- Wer: 0.1974

## Model description

Note: another version of this model is available with a KenLM 3gram model. This model performs better than this model. See https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-1b-cv8-mt-lm

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following config and hyperparameters were used during training:

model = Wav2Vec2ForCTC.from_pretrained(
    "facebook/wav2vec2-xls-r-1b", 
    attention_dropout=0.05,
    hidden_dropout=0.05,
    feat_proj_dropout=0.05,
    mask_time_prob=0.55,
    mask_feature_prob=0.10,
    layerdrop=0.05,
    ctc_zero_infinity=True,
    ctc_loss_reduction="mean", 
    pad_token_id=processor.tokenizer.pad_token_id,
    vocab_size=len(processor.tokenizer),
)

from transformers import TrainingArguments

training_args = TrainingArguments(
  output_dir=repo_name,
  group_by_length=True,
  per_device_train_batch_size=32,
  gradient_accumulation_steps=2,
  evaluation_strategy="steps",
  num_train_epochs=50,
  gradient_checkpointing=True,
  fp16=True,
  save_steps=400,
  eval_steps=400,
  logging_steps=400,
  learning_rate=5.5e-05, 
  warmup_steps=500,
  save_total_limit=2,
  push_to_hub=True, 
  report_to="tensorboard")

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.4564        | 13.33 | 400  | 0.3783          | 0.3981 |
| 0.7931        | 26.66 | 800  | 0.2377          | 0.2298 |
| 0.5364        | 39.98 | 1200 | 0.2210          | 0.1974 |

Note that the test WER of 19.74 is different than the above reported 17.57. This was due to a bug which was found while processing files with an older version of the datasets library. The right library is listed below.

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

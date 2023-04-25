---
language:
- mr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- openslr
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
- openslr
- shivam/marathi_samanantar_processed
- shivam/marathi_pib_processed
- opus100
- tatoeba
- tapaco
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
      value: 31.05
      name: Test WER
    - name: Test CER
      type: cer
      value: 6.82
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MR and OPENSLR - SLR64 - MR datasets.
It achieves the following results on the evaluation set:
- Loss: 0.494580
- Wer: 0.401524

### Eval results on Common Voice 8 "test" (WER):

| Without LM | With LM |
|---|---|
| 40.513437625350984 | 31.04693140794224 |

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
- num_epochs: 200.0
- mixed_precision_training: Native AMP

### Training results

| Step  | Training Loss  | Validation Loss  | Wer  |
|---|---|---|---|
 | 400  | 3.794000  | 3.532227  | 1.000000  | 
 | 800  | 3.362400  | 3.359044  | 1.000000  | 
 | 1200  | 2.293900  | 1.011279  | 0.829924  | 
 | 1600  | 1.233000  | 0.502743  | 0.593662  | 
 | 2000  | 0.962600  | 0.412519  | 0.496992  | 
 | 2400  | 0.831800  | 0.402903  | 0.493783  | 
 | 2800  | 0.737000  | 0.389773  | 0.469314  | 
 | 3200  | 0.677100  | 0.373987  | 0.436021  | 
 | 3600  | 0.634400  | 0.383823  | 0.432010  | 
 | 4000  | 0.586000  | 0.375610  | 0.419575  | 
 | 4400  | 0.561000  | 0.387891  | 0.418371  | 
 | 4800  | 0.518500  | 0.386357  | 0.417569  | 
 | 5200  | 0.515300  | 0.415069  | 0.430004  | 
 | 5600  | 0.478100  | 0.399211  | 0.408744  | 
 | 6000  | 0.468100  | 0.424542  | 0.402327  | 
 | 6400  | 0.439400  | 0.430979  | 0.410750  | 
 | 6800  | 0.429600  | 0.427700  | 0.409146  | 
 | 7200  | 0.400300  | 0.451111  | 0.419976  | 
 | 7600  | 0.395100  | 0.463446  | 0.405134  | 
 | 8000  | 0.381800  | 0.454752  | 0.407942  | 
 | 8400  | 0.371500  | 0.461547  | 0.404733  | 
 | 8800  | 0.362500  | 0.461543  | 0.411151  | 
 | 9200  | 0.338200  | 0.468299  | 0.417168  | 
 | 9600  | 0.338800  | 0.480989  | 0.412355  | 
 | 10000  | 0.317600  | 0.475700  | 0.410750  | 
 | 10400  | 0.315100  | 0.478920  | 0.403530  | 
 | 10800  | 0.296200  | 0.480600  | 0.398315  | 
 | 11200  | 0.299000  | 0.477083  | 0.393502  | 
 | 11600  | 0.290000  | 0.465646  | 0.393903  | 
 | 12000  | 0.290900  | 0.490041  | 0.405937  | 
 | 12400  | 0.275600  | 0.489354  | 0.399519  | 
 | 12800  | 0.272600  | 0.494580  | 0.395909  |
 | 13200 | 	0.265900 | 	0.497918 | 	0.397112 | 
 | 13600 | 	0.266300 | 	0.498627 | 	0.397513 | 
 | 14000 | 	0.259600 | 	0.504610 | 	0.401524 | 

#### Evaluation Commands
To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id smangrul/xls-r-mr-model --dataset mozilla-foundation/common_voice_8_0 --config mr --split test
```

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.3.dev0
- Tokenizers 0.11.0

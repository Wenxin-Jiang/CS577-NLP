---
language: no
license: cc-by-4.0
tags:
- seq2seq
datasets:
- Norwegian Nynorsk/Bokmål
---
# 🇳🇴 Norwegian T5 Base model Trained on the NCC🇳🇴  

This is a Norwegian T5-base model trained on the Norwegian Colossal Corpus (NCC) on a TPU v3-8. It needs to be finetuned on a specific task before being used for anything.

Currently the model is training. It is expected that it should be finished by the end of August 2021.

 The following setting were used in training:
```bash
./run_t5_mlm_flax_streaming.py \
    --output_dir="./" \
    --model_type="t5" \
    --config_name="./" \
    --tokenizer_name="./" \
    --dataset_name="pere/norwegian_colossal_corpus_v2_short100k" \
    --max_seq_length="512" \
    --weight_decay="0.01" \
    --per_device_train_batch_size="32" \
    --per_device_eval_batch_size="32" \
    --learning_rate="8e-3" \
    --warmup_steps="5000" \
    --overwrite_output_dir \
    --cache_dir /mnt/disks/flaxdisk/cache/ \
    --num_train_epochs="5" \
    --adam_beta1="0.9" \
    --adam_beta2="0.98" \
    --logging_steps="500" \
    --num_train_steps="1000000" \
    --num_eval_samples="5000" \
    --save_steps="5000" \
    --eval_steps="5000" \
    --preprocessing_num_workers 96 \
    --adafactor \
    --push_to_hub
 ```

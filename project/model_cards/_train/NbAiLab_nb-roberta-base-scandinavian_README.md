---
language: no
license: cc-by-4.0
tags:
- norwegian
- roberta
pipeline_tag: fill-mask
widget:
- text: På biblioteket kan du <mask> en bok.
- text: Dette er et <mask> eksempel.
- text: Av og til kan en språkmodell gi et <mask> resultat. 
- text: Som ansat får du <mask> for at bidrage til borgernes adgang til dansk kulturarv, til forskning og til samfundets demokratiske udvikling.
---

# This is just a Test Model. Do NOT use for anything! 

Continued pretrained from the nb-roberta-base.

The domain specific pretraining is done on the 102GB (Scandinavian corpus)[https://huggingface.co/datasets/NbAiLab/scandinavian].

## Train for 180k steps for 128 sequences:
```bash
./run_mlm_flax_stream.py \
    --output_dir="./" \
    --model_type="roberta" \
    --config_name="./" \
    --tokenizer_name="./" \
    --model_name_or_path="./" \
    --dataset_name="NbAiLab/scandinavian" \
    --max_seq_length="128" \
    --weight_decay="0.01" \
    --per_device_train_batch_size="128" \
    --per_device_eval_batch_size="128" \
    --learning_rate="6e-5" \
    --warmup_steps="5000" \
    --overwrite_output_dir \
    --cache_dir /mnt/disks/flaxdisk/cache/ \
    --num_train_steps="180000" \
    --adam_beta1="0.9" \
    --adam_beta2="0.98" \
    --logging_steps="10000" \
    --save_steps="10000" \
    --eval_steps="10000" \
    --preprocessing_num_workers 96 \
    --auth_token True \
    --adafactor \
    --push_to_hub
```
## Train for 20k steps for 512 sequences:
```bash
./run_mlm_flax_stream.py \
    --output_dir="./" \
    --model_type="roberta" \
    --config_name="./" \
    --tokenizer_name="./" \
    --model_name_or_path="./" \
    --dataset_name="NbAiLab/scandinavian" \
    --max_seq_length="512" \
    --weight_decay="0.01" \
    --per_device_train_batch_size="48" \
    --per_device_eval_batch_size="48" \
    --learning_rate="3e-5" \
    --warmup_steps="5000" \
    --overwrite_output_dir \
    --cache_dir /mnt/disks/flaxdisk/cache/ \
    --num_train_steps="20000" \
    --adam_beta1="0.9" \
    --adam_beta2="0.98" \
    --logging_steps="20000" \
    --save_steps="10000" \
    --eval_steps="10000" \
    --preprocessing_num_workers 96 \
    --auth_token True \
    --adafactor \
    --push_to_hub
```



Approximate additional training time: 1 week.
  
 

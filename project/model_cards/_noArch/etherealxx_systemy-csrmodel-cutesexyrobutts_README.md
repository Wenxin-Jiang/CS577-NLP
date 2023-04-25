---
language:
- en
license: unknown
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---
A reupload of Systemy model finetuned with Cutesexyrobutts' arts

Source: gofile(.)io/d/D1L69E

Image examples: https://imgur.com/VPNUae8

Prompt and settings examples: https://huggingface.co/etherealxx/systemy-csrmodel-cutesexyrobutts/blob/main/Prompt%20and%20settings%20example.PNG

Dreambooth settings used:

```
export LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH

export MODEL_NAME="/home/systemy/NAI"
export OUTPUT_DIR="/mnt/d/jigsaw"

accelerate launch train_dreambooth.py \
  --pretrained_model_name_or_path="$MODEL_NAME" \
  --pretrained_vae_name_or_path="stabilityai/sd-vae-ft-mse" \
  --output_dir="/mnt/d/acuteoutput" \
  --seed=3434554 \
  --resolution=512 \
  --train_batch_size=1 \
  --train_text_encoder \
  --mixed_precision="fp16" \
  --use_8bit_adam \
  --gradient_accumulation_steps=1 \
  --learning_rate=1e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --sample_batch_size=6 \
  --max_train_steps=100000 \
  --save_interval=1500 \
  --save_sample_prompt="image of SystemyTrigger girl" \
  --concepts_list="concepts_list.json" \
  --pad_tokens
```
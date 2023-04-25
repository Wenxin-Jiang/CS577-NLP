---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
- safetensors
inference: true
---

## Description

![Image](https://lh3.googleusercontent.com/pNDBY_yT1avLs6ycAVA9g61bOlb3C3RHbPBLvw4xM8o1sIp1GtyqR8HCMnoJ5xqSrlQ=w2400)

Maxwell the Cat Diffusion is a latent text-to-image diffusion model based on the original CompVis Stable Diffusion v1.5 and then fine-tuned on 5 images based on the 'Maxwell the Cat' meme originating from the modded Half Life 2 video.

To use this gorgeous object in your generations, add `maxwell the cat` to the prompts.

## Dreambooth hyperparameters

```sh
export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export INSTANCE_DIR="/home/kabachuha/kml/datasets/objects/maxwell"
export CLASS_DIR="/home/kabachuha/kml/datasets/objects/maxwell_class"
export OUTPUT_DIR="/home/kabachuha/kml/maxwell/"

accelerate launch train_dreambooth.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --class_data_dir=$CLASS_DIR \
  --output_dir=$OUTPUT_DIR \
  --with_prior_preservation --prior_loss_weight=1.0 \
  --instance_prompt="maxwell the cat" \
  --class_prompt="3d model of a black cat, lowpoly" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=1e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=200 \
  --max_train_steps=800 \
  --mixed_precision 'no' \
  --train_text_encoder \
  --checkpointing_steps 1200
```

The dataset link https://drive.google.com/drive/folders/1nd8NHrwuu_VKHaU8iBFw95w1iqfmhNTo?usp=share_link

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

You can't use the model to deliberately produce nor share illegal or harmful outputs or content
The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)

Please read the full license https://huggingface.co/stabilityai/stable-diffusion-2

## Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

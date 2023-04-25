---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

Description

Anything Elynia Diffusion is a latent text-to-image diffusion model based on Anything 3.0 and then fine-tuned on the main character of 'Battle for Wesnoth' add-ons using Dreambooth. This model has been created to explore the possibilities and limitations of Dreambooth training and to study how it learns when low-resolution pixelart videogame sprites are added to the dataset in addition to realistic artwork.

To use this style in your generations, add `1girl, elynia` to the prompts.

Dreambooth hyperparameters

```sh
export MODEL_NAME="/home/{USER}/kml/models1/"
export INSTANCE_DIR="/home/{USER}/kml/datasets/objects/elyniaA"
export CLASS_DIR="/home/{USER}/kml/datasets/objects/elyniaX"
export OUTPUT_DIR="/home/{USER}/kml/models2/"

accelerate launch train_dreambooth.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --class_data_dir=$CLASS_DIR \
  --output_dir=$OUTPUT_DIR \
  --with_prior_preservation --prior_loss_weight=1.0 \
  --instance_prompt="1girl, elynia" \
  --class_prompt="1girl, faerie girl, very long hair, pink hair, yellow eyes, detailed green dress, brown skirt, detached long sleeves, translucent green blue diamond-shaped butterfly wings" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=1e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=200 \
  --max_train_steps=800 \
  --mixed_precision 'no' \
  --train_text_encoder
```

Model Description

License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

You can't use the model to deliberately produce nor share illegal or harmful outputs or content The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)

Please read the full license https://huggingface.co/stabilityai/stable-diffusion-2

Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

Acknowledgements

This project would not have been possible without the incredible work by the CompVis Researchers, Wesnoth devs, artists and user made content makers.

The dataset for training currently resides here https://drive.google.com/drive/folders/1-sa5eQ9ZgoW0hGu-jYhzIJs0qPpzeFLg?usp=share_link.
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

Description

![Image](https://lh4.googleusercontent.com/JlBPrfK9WA0WmdEMw4iOj4CxweBqeaTCc8SsvLfk8X-PhHUBOIKT-lMvp2XmnWa6qlg=w2400)

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run gigafractal2-diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/gigafractal2-diffusion)


Gigafractal2 Diffusion is a latent text-to-image diffusion model based on the original StabilityAI Stable Diffusion v2.0 and then fine-tuned on 40 images origanally made with another diffusion model named 'Disco Diffusion' using Dreambooth. This model has been created to explore the possibilities and limitations of Dreambooth training with training steps increased much more than usual and to overcome biases in the model created by the text incoder's token associations. The purpose of this model is to provide the biomorphic fractalism effect present in Disco Diffusion, but without the bias to 'Disco parties' and especially 'discoballs' for which [the model by snek](was known for).

To use this style in your generations, add `gigafractal artstyle` to the prompts.

Dreambooth hyperparameters

```
export MODEL_NAME="stabilityai/stable-diffusion-2"
export INSTANCE_DIR="/home/{USERNAME}/kml/datasets/styles/dscdif"
export CLASS_DIR="/home/{USERNAME}/kml/datasets/styles/dscdif2"
export OUTPUT_DIR="/home/{USERNAME}/kml/models1"

accelerate launch train_dreambooth.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --class_data_dir=$CLASS_DIR \
  --output_dir=$OUTPUT_DIR \
  --with_prior_preservation --prior_loss_weight=1.0 \
  --instance_prompt="gigafractal artstyle" \
  --class_prompt="biomorphic" \
  --resolution=768 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=1e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=200 \
  --max_train_steps=2040 \
  --mixed_precision 'no' \
  --train_text_encoder
```

The regularization dataset of 200 AI-generated images had been produced in AUTOMATIC1111's webui with the following prompt which may have had a positive effect on the resulting quality.

```
a computer generated image of a spiral like object, digital art, polycount, generative art, (fractalism:0.7), lovecraftian, intricate, detailed matte painting, high detail, ornate, cgsociety, psychedelic art, gothic art, artstation hq, colorful, complex, biopunk, 8k, maxmialist Negative prompt: bad quality, text, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, flat, out of focus Steps: 20, Sampler: Euler a, CFG scale: 12.5, Seed: 2042420948, Size: 768x768, Model hash: a9263745
```

Model Description

The model originally used for fine-tuning is Stable Diffusion V2-0, see their infopage https://huggingface.co/stabilityai/stable-diffusion-2.

The current model has been fine-tuned with a learning rate of 1.0e-6 for 2040 steps using Dreambooth on Disco Diffusion produced images.

License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

You can't use the model to deliberately produce nor share illegal or harmful outputs or content
The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)

Please read the full license https://huggingface.co/stabilityai/stable-diffusion-2

Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

Acknowledgements

Inspired by snek's work on https://huggingface.co/SDAddictsAnon/Snek/blob/main/arrow_disco_artstyle.ckpt.

This project would not have been possible without the incredible work by the CompVis Researchers, Disco Diffusion, Deforum devs and all the artists who made the content for training even if they were an AI.

The dataset for training currently resides here https://drive.google.com/drive/folders/1v-uW2ESlQRFe17tnWZ7_CtjadD9swfIG?usp=share_link. The author is grateful to snek for the provided dataset.

You can see some examples of Gigafractal2 Diffusion produced images at https://drive.google.com/drive/folders/1z6iXjd4SveZ5s3vbjc3mI_bPOASVVTst?usp=share_link.
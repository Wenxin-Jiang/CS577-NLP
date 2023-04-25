---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1667942059199-6305d083df993a789e61126d.jpeg"
tags:
- stable-diffusion
- text-to-image
---
## Model description
<b>isoCities</b> v1

This model trained based on Stable Diffusion 1.5 model to create isometric cities, venues, etc more precisely.
Trained isometric city model merged with SD 1.5 with Automatic1111's checkpoint merger tool (Couldn't remember exactly the merging ratio and the interpolation method)

Use "<b>an illustration of an isometric city, digital art, highly detailed</b>" in your prompts.

[CKPT download link](https://huggingface.co/Astroboy/isoCities/blob/main/isometric_city%2BSD1.5.ckpt)

## Intended uses & limitations
Do not use for commercial purposes.

## Training procedure
Trained on a WSL2 Ubuntu machine with DreamBooth.

### Training hyperparameters
The following hyperparameters were used during training:
  --with_prior_preservation --prior_loss_weight=1.0 \
  --instance_prompt="an illustration of an isometric city, digital art, highly detailed" \
  --class_prompt="isometric city" \
  --resolution=512 \
  --train_batch_size=1 \
  --mixed_precision="fp16" \
  --gradient_accumulation_steps=1 --gradient_checkpointing \
  --use_8bit_adam \
  --learning_rate=5e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=50 \
  --max_train_steps=1500

### Training results
Sample images
![00021.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667942059199-6305d083df993a789e61126d.jpeg)
![00022.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667942060129-6305d083df993a789e61126d.jpeg)
![00023.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667942059810-6305d083df993a789e61126d.jpeg)
![00024.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667942060647-6305d083df993a789e61126d.jpeg)
![00025.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667942059778-6305d083df993a789e61126d.jpeg)


## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: a portrait of [V]
---
### training params
```json
{
    "pretrained_model_name_or_path": "runwayml/stable-diffusion-v1-5",
    "instance_data_dir": "./6de17b72-f0d4-42d5-a98b-c563a5bdbe93/instance_data",
    "class_data_dir": "./class_data/a-portrait-of-a-person",
    "output_dir": "./6de17b72-f0d4-42d5-a98b-c563a5bdbe93/",
    "train_text_encoder": true,
    "with_prior_preservation": true,
    "prior_loss_weight": 1.0,
    "instance_prompt": "a portrait of [V]",
    "class_prompt": "a portrait of a person",
    "resolution": 512,
    "train_batch_size": 1,
    "gradient_accumulation_steps": 2,
    "gradient_checkpointing": true,
    "use_8bit_adam": true,
    "learning_rate": 1e-06,
    "lr_scheduler": "constant",
    "lr_warmup_steps": 0,
    "num_class_images": 200,
    "max_train_steps": 1050,
    "mixed_precision": "fp16"
}
```

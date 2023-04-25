---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: me
---
### training params
```json
{
    "pretrained_model_name_or_path": "runwayml/stable-diffusion-v1-5",
    "instance_data_dir": "./b3d0ef12-11d6-43df-8a96-ebcb5ca71ea1/instance_data",
    "class_data_dir": "./class_data/person",
    "output_dir": "./b3d0ef12-11d6-43df-8a96-ebcb5ca71ea1/",
    "train_text_encoder": true,
    "with_prior_preservation": true,
    "prior_loss_weight": 1.0,
    "instance_prompt": "me",
    "class_prompt": "person",
    "resolution": 512,
    "train_batch_size": 1,
    "gradient_accumulation_steps": 1,
    "gradient_checkpointing": true,
    "use_8bit_adam": true,
    "learning_rate": 1e-06,
    "lr_scheduler": "polynomial",
    "lr_warmup_steps": 0,
    "num_class_images": 500,
    "max_train_steps": 1050,
    "mixed_precision": "fp16"
}
```

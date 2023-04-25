---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: [V]
---
### training params
```json
{
    "pretrained_model_name_or_path": "runwayml/stable-diffusion-v1-5",
    "instance_data_dir": "./1a765cc4-702d-4d60-bdf9-df352c214b7b/instance_data",
    "class_data_dir": "./class_data/a-portrait-of-a-person",
    "output_dir": "./1a765cc4-702d-4d60-bdf9-df352c214b7b/",
    "train_text_encoder": true,
    "with_prior_preservation": false,
    "prior_loss_weight": 1.0,
    "instance_prompt": "[V]",
    "class_prompt": "a portrait of a person",
    "resolution": 512,
    "train_batch_size": 1,
    "gradient_accumulation_steps": 2,
    "gradient_checkpointing": true,
    "use_8bit_adam": true,
    "learning_rate": 2e-06,
    "lr_scheduler": "polynomial",
    "lr_warmup_steps": 0,
    "num_class_images": 200,
    "max_train_steps": 1190,
    "mixed_precision": "fp16"
}
```

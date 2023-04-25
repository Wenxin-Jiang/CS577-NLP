---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: sd-tzvc
---
### training params
```json
{
    "pretrained_model_name_or_path": "multimodalart/sd-fine-tunable",
    "instance_data_dir": "./3647bbc5-4fbe-4a94-95ec-5aec23a04e73/instance_data",
    "class_data_dir": "./class_data/person",
    "output_dir": "./3647bbc5-4fbe-4a94-95ec-5aec23a04e73/",
    "train_text_encoder": true,
    "with_prior_preservation": false,
    "prior_loss_weight": 1.0,
    "instance_prompt": "sd-tzvc",
    "class_prompt": "person",
    "resolution": 512,
    "train_batch_size": 1,
    "gradient_accumulation_steps": 1,
    "gradient_checkpointing": true,
    "use_8bit_adam": true,
    "learning_rate": 2e-06,
    "lr_scheduler": "polynomial",
    "lr_warmup_steps": 0,
    "num_class_images": 500,
    "max_train_steps": 1050,
    "mixed_precision": "fp16"
}
```

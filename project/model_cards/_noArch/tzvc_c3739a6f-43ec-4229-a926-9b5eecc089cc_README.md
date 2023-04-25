---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: sdcid
---
### training params
```json
{
    "pretrained_model_name_or_path": "multimodalart/sd-fine-tunable",
    "instance_data_dir": "./c3739a6f-43ec-4229-a926-9b5eecc089cc/instance_data",
    "class_data_dir": "./class_data/class",
    "output_dir": "./c3739a6f-43ec-4229-a926-9b5eecc089cc/",
    "train_text_encoder": true,
    "with_prior_preservation": true,
    "prior_loss_weight": 1.0,
    "instance_prompt": "sdcid",
    "class_prompt": "",
    "resolution": 512,
    "train_batch_size": 1,
    "gradient_accumulation_steps": 1,
    "gradient_checkpointing": true,
    "use_8bit_adam": true,
    "learning_rate": 2e-06,
    "lr_scheduler": "polynomial",
    "lr_warmup_steps": 0,
    "num_class_images": 200,
    "max_train_steps": 1050,
    "mixed_precision": "fp16"
}
```

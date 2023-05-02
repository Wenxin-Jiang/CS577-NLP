---
license: apache-2.0
tags:
- image-classification
datasets:
- Face-Mask18K 
---

# Distilled Data-efficient Image Transformer for Face Mask Detection

Distilled data-efficient Image Transformer (DeiT) model pre-trained and fine-tuned on Self Currated Custom Face-Mask18K Dataset (18k images, 2 classes) at resolution 224x224. It was first introduced in the paper Training data-efficient image transformers & distillation through attention by Touvron et al.  

## Model description

This model is a distilled Vision Transformer (ViT). It uses a distillation token, besides the class token, to effectively learn from a teacher (CNN) during both pre-training and fine-tuning. The distillation token is learned through backpropagation, by interacting with the class ([CLS]) and patch tokens through the self-attention layers.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. 

## Training Metrics
    epoch                    =          2.0
    total_flos               = 2078245655GF
    train_loss               =       0.0438
    train_runtime            =   1:37:16.87
    train_samples_per_second =        9.887
    train_steps_per_second   =        0.309

---

## Evaluation Metrics
    epoch                   =        2.0
    eval_accuracy           =     0.9922
    eval_loss               =     0.0271
    eval_runtime            = 0:03:17.36
    eval_samples_per_second =      18.22
    eval_steps_per_second   =       2.28
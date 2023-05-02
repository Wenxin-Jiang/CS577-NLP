---
license: apache-2.0
tags:
- image-classification
datasets:
- Face-Mask18K 
---

# ConvNeXt for Face Mask Detection

ConvNeXt model pre-trained and fine-tuned on Self Currated Custom Face-Mask18K Dataset (18k images, 2 classes) at resolution 224x224. It was introduced in the paper A ConvNet for the 2020s by Zhuang Liu, Hanzi Mao et al.  

## Training Metrics
    epoch                    =         3.54
    total_flos               = 1195651761GF
    train_loss               =       0.0079
    train_runtime            =   1:08:20.25
    train_samples_per_second =       14.075
    train_steps_per_second   =         0.22

---

## Evaluation Metrics
    epoch                   =       3.54
    eval_accuracy           =     0.9961
    eval_loss               =     0.0151
    eval_runtime            = 0:01:23.47
    eval_samples_per_second =     43.079
    eval_steps_per_second   =      5.391
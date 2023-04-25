---
license: apache-2.0
tags:
- image-classification
datasets:
- Face-Mask18K 
---

# Vision Transformer (ViT) for Face Mask Detection

Vision Transformer (ViT) model pre-trained and fine-tuned on Self Currated Custom Face-Mask18K Dataset (18k images, 2 classes) at resolution 224x224. It was first introduced in the paper Training data-efficient image transformers & distillation through attention by Touvron et al. 
Vision Transformer (ViT) model pre-trained and fine-tuned on Self Currated Custom Face-Mask18K Dataset (18k images, 2 classes) at resolution 224x224. It was introduced in the paper An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale by Dosovitskiy et al.

## Model description

The Vision Transformer (ViT) is a transformer encoder model (BERT-like) pretrained on a large collection of images in a supervised fashion, namely ImageNet-21k, at a resolution of 224x224 pixels.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. One also adds a [CLS] token to the beginning of a sequence to use it for classification tasks. One also adds absolute position embeddings before feeding the sequence to the layers of the Transformer encoder.

Note that this model does not provide any fine-tuned heads, as these were zero'd by Google researchers. However, the model does include the pre-trained pooler, which can be used for downstream tasks (such as image classification).

By pre-training the model, it learns an inner representation of images that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled images for instance, you can train a standard classifier by placing a linear layer on top of the pre-trained encoder. One typically places a linear layer on top of the [CLS] token, as the last hidden state of this token can be seen as a representation of an entire image.

## Training Metrics
    epoch                    =        0.89
    total_flos               = 923776502GF
    train_loss               =       0.057
    train_runtime            =  0:40:10.40
    train_samples_per_second =      23.943
    train_steps_per_second   =       1.497
---

## Evaluation Metrics
    epoch                   =       0.89
    eval_accuracy           =     0.9894
    eval_loss               =     0.0395
    eval_runtime            = 0:00:36.81
    eval_samples_per_second =     97.685
    eval_steps_per_second   =     12.224
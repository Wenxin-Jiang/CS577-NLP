---
license: apache-2.0
tags:
- image-classification
datasets:
- Face-Mask18K 
---

# BEiT for Face Mask Detection

BEiT model pre-trained and fine-tuned on Self Currated Custom Face-Mask18K Dataset (18k images, 2 classes) at resolution 224x224. It was introduced in the paper BEIT: BERT Pre-Training of Image Transformers by Hangbo Bao, Li Dong and Furu Wei.  

## Model description

The BEiT model is a Vision Transformer (ViT), which is a transformer encoder model (BERT-like). In contrast to the original ViT model, BEiT is pretrained on a large collection of images in a self-supervised fashion, namely ImageNet-21k, at a resolution of 224x224 pixels. The pre-training objective for the model is to predict visual tokens from the encoder of OpenAI's DALL-E's VQ-VAE, based on masked patches. Next, the model was fine-tuned in a supervised fashion on ImageNet (also referred to as ILSVRC2012), a dataset comprising 1 million images and 1,000 classes, also at resolution 224x224.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. Contrary to the original ViT models, BEiT models do use relative position embeddings (similar to T5) instead of absolute position embeddings, and perform classification of images by mean-pooling the final hidden states of the patches, instead of placing a linear layer on top of the final hidden state of the [CLS] token.

By pre-training the model, it learns an inner representation of images that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled images for instance, you can train a standard classifier by placing a linear layer on top of the pre-trained encoder. One typically places a linear layer on top of the [CLS] token, as the last hidden state of this token can be seen as a representation of an entire image. Alternatively, one can mean-pool the final hidden states of the patch embeddings, and place a linear layer on top of that.

## Training Metrics
    epoch                    =        0.55
    total_flos               = 576468516GF
    train_loss               =       0.151
    train_runtime            =  0:58:16.56
    train_samples_per_second =      16.505
    train_steps_per_second   =       1.032

---

## Evaluation Metrics
    epoch                   =       0.55
    eval_accuracy           =      0.975
    eval_loss               =     0.0803
    eval_runtime            = 0:03:13.02
    eval_samples_per_second =     18.629
    eval_steps_per_second   =      2.331
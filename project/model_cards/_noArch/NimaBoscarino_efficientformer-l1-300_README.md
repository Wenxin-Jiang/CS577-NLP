---
language:
- en
license: apache-2.0
library_name: timm
tags:
- mobile
- vison
- image-classification
datasets:
- imagenet-1k
metrics:
- accuracy
---

# EfficientFormer-L1

## Table of Contents
- [EfficientFormer-L1](#-model_id--defaultmymodelname-true)
  - [Table of Contents](#table-of-contents)
  - [Model Details](#model-details)
  - [How to Get Started with the Model](#how-to-get-started-with-the-model)
  - [Uses](#uses)
      - [Direct Use](#direct-use)
      - [Downstream Use](#downstream-use)
      - [Misuse and Out-of-scope Use](#misuse-and-out-of-scope-use)
  - [Limitations and Biases](#limitations-and-biases)
  - [Training](#training)
      - [Training Data](#training-data)
      - [Training Procedure](#training-procedure)
  - [Evaluation Results](#evaluation-results)
  - [Environmental Impact](#environmental-impact)
  - [Citation Information](#citation-information)


<model_details>

## Model Details

<!-- Give an overview of your model, the relevant research paper, who trained it, etc.  -->

EfficientFormer-L1, developed by [Snap Research](https://github.com/snap-research), is one of three EfficientFormer models. The EfficientFormer models were released as part of  an effort to prove that properly designed transformers can reach extremely low latency on mobile devices while maintaining high performance.

This checkpoint of EfficientFormer-L1 was trained for 300 epochs.

- Developed by: Yanyu Li, Geng Yuan, Yang Wen, Eric Hu, Georgios Evangelidis, Sergey Tulyakov, Yanzhi Wang, Jian Ren
- Language(s): English
- License: This model is licensed under the apache-2.0 license
- Resources for more information:
  - [Research Paper](https://arxiv.org/abs/2206.01191)
  - [GitHub Repo](https://github.com/snap-research/EfficientFormer/)

</model_details>

<how_to_start>

## How to Get Started with the Model 

Use the code below to get started with the model.

```python
# A nice code snippet here that describes how to use the model...
```
</how_to_start>

<uses>

## Uses

#### Direct Use

This model can be used for image classification and semantic segmentation. On mobile devices (the model was tested on iPhone 12), the CoreML checkpoints will perform these tasks with low latency.

<Limitations_and_Biases>

## Limitations and Biases

Though most designs in EfficientFormer are general-purposed, e.g., dimension- consistent design and 4D block with CONV-BN fusion, the actual speed of EfficientFormer may vary on other platforms. For instance, if GeLU is not well supported while HardSwish is efficiently implemented on specific hardware and compiler, the operator may need to be modified accordingly. The proposed latency-driven slimming is simple and fast. However, better results may be achieved if search cost is not a concern and an enumeration-based brute search is performed.

Since the model was trained on Imagenet-1K, the [biases embedded in that dataset](https://huggingface.co/datasets/imagenet-1k#considerations-for-using-the-data) will be reflected in the EfficientFormer models.

</Limitations_and_Biases>

<Training>

## Training

#### Training Data

This model was trained on ImageNet-1K.
 
See the [data card](https://huggingface.co/datasets/imagenet-1k) for additional information.

#### Training Procedure

* Parameters: 12.3 M
* GMACs: 1.3
* Train. Epochs: 300

Trained on a cluster with NVIDIA A100 and V100 GPUs.

</Training>

<Eval_Results>

## Evaluation Results

Top-1 Accuracy: 79.2% on ImageNet 10K
Latency: 1.6 ms

</Eval_Results>

<Cite>

## Citation Information

```bibtex
@article{li2022efficientformer,
  title={EfficientFormer: Vision Transformers at MobileNet Speed},
  author={Li, Yanyu and Yuan, Geng and Wen, Yang and Hu, Eric and Evangelidis, Georgios and Tulyakov, Sergey and Wang, Yanzhi and Ren, Jian},
  journal={arXiv preprint arXiv:2206.01191},
  year={2022}
}
```
</Cite>
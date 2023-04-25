---
license: apache-2.0
library_name: keras
tags:
- vision
- image-classification
---

# Intro
This is the model for our paper ["Melanoma Detection using Adversarial Training and Deep Transfer Learning"](https://arxiv.org/abs/2004.06824). Code is available [here](https://github.com/hasibzunair/adversarial-lesions).

## Model description
The model is trained on the ISIC 2016 Task 3 dataset. The architecture and algorithm is described in this [paper](https://arxiv.org/abs/2004.06824).

## Intended uses & limitations
You can use the raw model for melanoma detection from skin lesion images.

## How to use
See Spaces [demo](https://huggingface.co/spaces/hasibzunair/melanoma-detection-demo). For more code examples, we refer to this [GitHub](https://github.com/hasibzunair/adversarial-lesions#deploy) deploy section.

## Limitations and bias
The model is trained on a specific dataset with just over a thousand samples. It may or may not work for other kinds of skin lesion images. Further, there is no out-of-distribution detection method to filter out non skin lesion images. If you give an image of a dog, the model will still classify it as benign for malignant! 

## Training data
See [dataset details](https://github.com/hasibzunair/adversarial-lesions#preparing-training-and-test-datasets).

## Training procedure
See [training details](https://github.com/hasibzunair/adversarial-lesions#training-both-stages). 

## Evaluation results
For results in benchmarks, we refer to Figures 5, 6 and Table 1 of the original paper [here](https://arxiv.org/abs/2004.06824).


## Citation
```bibtex
@article{zunair2020melanoma,
  title={Melanoma detection using adversarial training and deep transfer learning},
  author={Zunair, Hasib and Hamza, A Ben},
  journal={Physics in Medicine \& Biology},
  year={2020},
  publisher={IOP Publishing}
}
```
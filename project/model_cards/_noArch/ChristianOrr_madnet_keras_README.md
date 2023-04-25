---
license: apache-2.0
tags:
- vision
- deep-stereo
- depth-estimation
- Tensorflow2
- Keras
datasets:
- flyingthings-3d
- kitti
---

# MADNet Keras

MADNet is a deep stereo depth estimation model. Its key defining features are:
 1. It has a light-weight architecture which means it has low latency.
 2. It supports self-supervised training, so it can be conveniently adapted in the field with no training data. 
 3. It's a stereo depth model, which means it's capable of high accuracy.
 
 The MADNet weights in this repository were trained using a Tensorflow 2 / Keras implementation of the original code. The model was created using the Keras Functional API, which enables the following features:
 1. Good optimization. 
 2. High level Keras methods (.fit, .predict and .evaluate).
 3. Little boilerplate code.
 4. Decent support from external packages (like Weights and Biases). 
 5. Callbacks.
 
 The weights provided were either trained on the 2012 / 2015 kitti stereo dataset or flyingthings-3d dataset. The weights of the pretrained models from the original paper (tf1_conversion_kitti.h5 and tf1_conversion_synthetic.h5) are provided in tensorflow 2 format. The TF1 weights help speed up fine-tuning, but its recommended to use either synthetic.h5 (trained on flyingthings-3d) or kitti.h5 (trained on 2012 and 2015 kitti stereo datasets).

**Abstract**:

Deep convolutional neural networks trained end-to-end are the undisputed state-of-the-art methods to regress dense disparity maps directly from stereo pairs. However, such methods suffer from notable accuracy drops when exposed to scenarios significantly different from those seen in the training phase (e.g.real vs synthetic images, indoor vs outdoor, etc). As it is unlikely to be able to gather enough samples to achieve effective training/ tuning in any target domain, we propose to perform unsupervised and continuous online adaptation of a deep stereo network in order to preserve its accuracy independently of the sensed environment. However, such a strategy can be extremely demanding regarding computational resources and thus not enabling real-time performance. Therefore, we address this side effect by introducing a new lightweight, yet effective, deep stereo architecture Modularly ADaptive Network (MADNet) and by developing Modular ADaptation (MAD), an algorithm to train independently only sub-portions of our model. By deploying MADNet together with MAD we propose the first ever realtime self-adaptive deep stereo system.

## Usage Instructions
See the accompanying codes readme for details on how to perform training and inferencing with the model: [madnet-deep-stereo-with-keras](https://github.com/ChristianOrr/madnet-deep-stereo-with-keras).

## Training 
### TF1 Kitti and TF1 Synthetic
Training details for the TF1 weights are available in the supplementary material (at the end) of this paper: [Real-time self-adaptive deep stereo](https://arxiv.org/abs/1810.05424)

### Synthetic
The synthetic model was finetuned using the tf1 synthetic weights. It was trained on the flyingthings-3d dataset with the following parameters:
- Steps: 1.5 million
- Learning Rate: 0.0001
- Decay Rate: 0.999
- Minimum Learning Rate Cap: 0.000001
- Batch Size: 1
- Optimizer: Adam
- Image Height: 480
- Image Width: 640

### Kitti
The kitti model was finetuned using the synthetic weights. Tensorboard events file is available in the logs directory. It was trained on the 2012 and 2015 kitti stereo dataset with the following parameters:
- Steps: 0.5 million
- Learning Rate: 0.0001
- Decay Rate: 0.999
- Minimum Learning Rate Cap: 0.0000001
- Batch Size: 1
- Optimizer: Adam
- Image Height: 480
- Image Width: 640

## BibTeX entry and citation info

```bibtex
@InProceedings{Tonioni_2019_CVPR,
    author = {Tonioni, Alessio and Tosi, Fabio and Poggi, Matteo and Mattoccia, Stefano and Di Stefano, Luigi},
    title = {Real-time self-adaptive deep stereo},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2019}    
}
```

```bibtex
@article{Poggi2021continual,
    author={Poggi, Matteo and Tonioni, Alessio and Tosi, Fabio
            and Mattoccia, Stefano and Di Stefano, Luigi},
    title={Continual Adaptation for Deep Stereo},
    journal={IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
    year={2021}
}
```

```bibtex
@InProceedings{MIFDB16,
  author    = "N. Mayer and E. Ilg and P. Hausser and P. Fischer and D. Cremers and A. Dosovitskiy and T. Brox",
  title     = "A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation",
  booktitle = "IEEE International Conference on Computer Vision and Pattern Recognition (CVPR)",
  year      = "2016",
  note      = "arXiv:1512.02134",
  url       = "http://lmb.informatik.uni-freiburg.de/Publications/2016/MIFDB16"
}
```

```bibtex
@INPROCEEDINGS{Geiger2012CVPR,
  author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},
  title = {Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2012}
}
```

```bibtex
@INPROCEEDINGS{Menze2015CVPR,
  author = {Moritz Menze and Andreas Geiger},
  title = {Object Scene Flow for Autonomous Vehicles},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2015}
}
```
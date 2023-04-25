---
tags:
- image-classification
- fastai
library_name: fastai
datasets:
- Oxford-IIIT Pet Dataset
- ImageNet
---

## Pet breeds classification model

Finetuned model on The Oxford-IIIT Pet Dataset. It was introduced in
[this paper](https://www.robots.ox.ac.uk/~vgg/publications/2012/parkhi12a/) and first released in
[this webpage](https://www.robots.ox.ac.uk/~vgg/data/pets/).

The pretrained model was trained on the ImageNet dataset, a dataset that has 100,000+ images across 200 different classes. It was introduced in [this paper](https://image-net.org/static_files/papers/imagenet_cvpr09.pdf) and available [in this webpage](https://image-net.org/download.php)

Disclaimer: The model was fine-tuned after [Chapter 5](https://github.com/fastai/fastbook/blob/master/05_pet_breeds.ipynb) of [Deep Learning for Coders with Fastai and Pytorch: AI Applications Without a PhD (2020)](https://github.com/fastai/fastbook) written by Jeremy Howard and Sylvain Gugger.

## Model description

The model was finetuned using the `cnn_learner` method of the fastai library suing a Resnet 34 backbone pretrained on the ImageNet dataset. The fastai library uses PyTorch for the undelying operations. `cnn_learner` automatically gets a pretrained model from a given architecture with a custom head that is suitable for the target data.

Resnet34 is a 34 layer convolutional neural network. It takes residuals from each layer and uses them in the subsequent connected layers. Advantages of a resnet arquitecture ([Neurohive, 2019](https://neurohive.io/en/popular-networks/resnet/)):
- Are easy to optimize, but the “plain” networks (that simply stack layers) shows higher training error when the depth increases.
- Can easily gain accuracy from greatly increased depth, producing results which are better than previous networks.

 Please refer to the original paper '[Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)' written by Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun.

Specifically, the model was obtained:

```
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(2)
```

## How to use

Download the model this way:
```python
from huggingface_hub import hf_hub_download
from fastai.learner import load_learner

model = load_learner(
    hf_hub_download('espejelomar/fastai-pet-breeds-classification', filename="model.pkl")
    )
```

Then you can use your downloaded fastai model in any way you want. For example, if the input is a PIL Image, with the following code you can obtain the resulting outputs for each class:

```python
_, _, preds = self.model.predict(np.array(inputs))
```

## Training data

The Resnet34 model was pretrained on [ImageNet](https://image-net.org/static_files/papers/imagenet_cvpr09.pdf), a dataset that has 100,000+ images across 200 different classes, and fine-tuned on [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Preprocessing

For more detailed information on the preprocessing procedure, refer to the [Chapter 5](https://github.com/fastai/fastbook/blob/master/05_pet_breeds.ipynb) of [Deep Learning for Coders with Fastai and Pytorch: AI Applications Without a PhD (2020)](https://github.com/fastai/fastbook).

Two main strategies are followed to presizing the images:

- Resize images to relatively "large" dimensions—that is, dimensions significantly larger than the target training dimensions.
- Compose all of the common augmentation operations (including a resize to the final target size) into one, and perform the combined operation on the GPU only once at the end of processing, rather than performing the operations individually and interpolating multiple times.

"The first step, the resize, creates images large enough that they have spare margin to allow further augmentation transforms on their inner regions without creating empty zones. This transformation works by resizing to a square, using a large crop size. On the training set, the crop area is chosen randomly, and the size of the crop is selected to cover the entire width or height of the image, whichever is smaller.

In the second step, the GPU is used for all data augmentation, and all of the potentially destructive operations are done together, with a single interpolation at the end." ([Howard and Gugger, 2020](https://github.com/fastai/fastbook))

Specifically, the following code is used for preprocessing:

```python
#hide_input
#id interpolations
#caption A comparison of fastai's data augmentation strategy (left) and the traditional approach (right).
dblock1 = DataBlock(blocks=(ImageBlock(), CategoryBlock()),
                   get_y=parent_label,
                   item_tfms=Resize(460))
# Place an image in the 'images/grizzly.jpg' subfolder where this notebook is located before running this
dls1 = dblock1.dataloaders([(Path.cwd()/'images'/'grizzly.jpg')]*100, bs=8)
dls1.train.get_idxs = lambda: Inf.ones
x,y = dls1.valid.one_batch()
_,axs = subplots(1, 2)

x1 = TensorImage(x.clone())
x1 = x1.affine_coord(sz=224)
x1 = x1.rotate(draw=30, p=1.)
x1 = x1.zoom(draw=1.2, p=1.)
x1 = x1.warp(draw_x=-0.2, draw_y=0.2, p=1.)

tfms = setup_aug_tfms([Rotate(draw=30, p=1, size=224), Zoom(draw=1.2, p=1., size=224),
                       Warp(draw_x=-0.2, draw_y=0.2, p=1., size=224)])
x = Pipeline(tfms)(x)
#x.affine_coord(coord_tfm=coord_tfm, sz=size, mode=mode, pad_mode=pad_mode)
TensorImage(x[0]).show(ctx=axs[0])
TensorImage(x1[0]).show(ctx=axs[1]);
```

### BibTeX entry and citation info

```bibtex
@book{howard2020deep,
  author    = {Howard, J. and Gugger, S.},
  title     = {Deep Learning for Coders with Fastai and Pytorch: AI Applications Without a PhD},
  isbn      = {9781492045526},
  year      = {2020},
  url       = {https://books.google.no/books?id=xd6LxgEACAAJ},
  publisher = {O'Reilly Media, Incorporated},
}
```

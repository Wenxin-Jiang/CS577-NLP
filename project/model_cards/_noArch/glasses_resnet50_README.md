---
license: apache-2.0
tags:
- image-classification
datasets:
- imagenet
---
# resnet50
Implementation of ResNet proposed in [Deep Residual Learning for Image
Recognition](https://arxiv.org/abs/1512.03385)

 ``` python
 ResNet.resnet18()
 ResNet.resnet26()
 ResNet.resnet34()
 ResNet.resnet50()
 ResNet.resnet101()
 ResNet.resnet152()
 ResNet.resnet200()

 Variants (d) proposed in `Bag of Tricks for Image Classification with Convolutional Neural Networks <https://arxiv.org/pdf/1812.01187.pdf`_

 ResNet.resnet26d()
 ResNet.resnet34d()
 ResNet.resnet50d()
 # You can construct your own one by chaning `stem` and `block`
 resnet101d = ResNet.resnet101(stem=ResNetStemC, block=partial(ResNetBottleneckBlock, shortcut=ResNetShorcutD))
 ```

 Examples:

  ``` python
  # change activation
  ResNet.resnet18(activation = nn.SELU)
  # change number of classes (default is 1000 )
  ResNet.resnet18(n_classes=100)
  # pass a different block
  ResNet.resnet18(block=SENetBasicBlock)
  # change the steam
  model = ResNet.resnet18(stem=ResNetStemC)
  change shortcut
  model = ResNet.resnet18(block=partial(ResNetBasicBlock, shortcut=ResNetShorcutD))
  # store each feature
  x = torch.rand((1, 3, 224, 224))
  # get features
  model = ResNet.resnet18()
  # first call .features, this will activate the forward hooks and tells the model you'll like to get the features
  model.encoder.features
  model(torch.randn((1,3,224,224)))
  # get the features from the encoder
  features = model.encoder.features
  print([x.shape for x in features])
  #[torch.Size([1, 64, 112, 112]), torch.Size([1, 64, 56, 56]), torch.Size([1, 128, 28, 28]), torch.Size([1, 256, 14, 14])]
  ```

 
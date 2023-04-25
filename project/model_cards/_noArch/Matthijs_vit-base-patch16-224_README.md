---
license: apache-2.0
tags:
- vision
- image-classification
datasets:
- imagenet
- imagenet-21k
---

# Vision Transformer (base-sized model) 

Vision Transformer (ViT) model pre-trained on ImageNet-21k (14 million images, 21,843 classes) at resolution 224x224, and fine-tuned on ImageNet 2012 (1 million images, 1,000 classes) at resolution 224x224. It was introduced in the paper [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) by Dosovitskiy et al. and first released in [this repository](https://github.com/google-research/vision_transformer). However, the weights were converted from the [timm repository](https://github.com/rwightman/pytorch-image-models) by Ross Wightman, who already converted the weights from JAX to PyTorch. Credits go to him. 

This repo contains a Core ML version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224).

## Usage instructions

Create a `VNCoreMLRequest` that loads the ViT model:

```swift
import CoreML
import Vision

lazy var classificationRequest: VNCoreMLRequest = {
  do {
    let config = MLModelConfiguration()
    config.computeUnits = .all
    let coreMLModel = try ViT(configuration: config)
    let visionModel = try VNCoreMLModel(for: coreMLModel.model)

    let request = VNCoreMLRequest(model: visionModel, completionHandler: { [weak self] request, error in
      if let results = request.results as? [VNClassificationObservation] {
        /* do something with the results */
      }
    })

    request.imageCropAndScaleOption = .centerCrop
    return request
  } catch {
    fatalError("Failed to create VNCoreMLModel: \(error)")
  }
}()
```

Perform the request:

```swift
func classify(image: UIImage) {
  guard let ciImage = CIImage(image: image) else {
    print("Unable to create CIImage")
    return
  }

  DispatchQueue.global(qos: .userInitiated).async {
    let handler = VNImageRequestHandler(ciImage: ciImage, orientation: .up)
    do {
      try handler.perform([self.classificationRequest])
    } catch {
      print("Failed to perform classification: \(error)")
    }
  }
}
```

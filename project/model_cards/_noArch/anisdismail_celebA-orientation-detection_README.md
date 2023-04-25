---
language:
- en 
license: cc-by-nc-4.0  
tags:
- image-classification 
- pytorch  
datasets:
- nielsr/CelebA-faces 

model-index:
- name: celebA_orientation_detection_model
  results:
  - task: 
      type: image_classification # Required. Example: automatic-speech-recognition
      name: Image Classification # Optional. Example: Speech Recognition
    dataset:
      type: nielsr/CelebA-faces   
      name: CelebA-faces   
      
    metrics:
      - type: f1score    # Required. Example: wer
        value: 0.97  # Required. Example: 20.90
        name: Val F1 Score    # Optional. Example: Test WER
---
## Detecting the Orientation of CelebA pictures using Deep Learning
This model has been trained on a modified version of the CelebA-faces dataset, which was made from flipping 20,000 images upside down and keeping 20,000 images intact.<br> 
The model relies on Resnet-18 as a backbone and is connected to one output node to classify whether the images are flipped upside down (1) or not (0).
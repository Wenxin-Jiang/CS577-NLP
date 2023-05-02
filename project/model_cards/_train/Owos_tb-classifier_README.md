---
license: apache-2.0
tags:
- vision
- image-classification

datasets:
- https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

widget:
- src: https://huggingface.co/Owos/tb-classifier/blob/main/tb-negative.png
  example_title: Negative
- src: https://huggingface.co/Owos/tb-classifier/blob/main/tb-positive.png
  example_title: Positive
 
metrics:
- Accuracy
- Precision
- Recall







---

# Tuberculosis Classifier
[Github repo is here](https://github.com/owos/tb_project) </br>
[HuggingFace Space](https://huggingface.co/spaces/Owos/tb_prediction_space)
# Model description
This is a computer vision model that was built with TensorFlow to classify if a given x-ray scan is positive for Tuberculosis or not.

# Intended uses & limitations
The model was built to help support low-resourced and short-staffed primary healthcare centers in Nigeria. Particularly, the aim to was created a computer-aided diagnosing tool for Radiologists in these centers.
The model has not undergone clinical testing  and usage is at ueser's own risk.The model has however been tested on real life data images that are positive for tuberculosis

# How to use
Download the pre-trained model and use it to make inference.
A space has been created for testing [here](space.com)

# Training data
The entire dataset consist of 3500 negative images and 700 positive TB images. </br>
The data was splitted in 80% for training and 20% for validation.

# Training procedure
Transfer-learning was employed using InceptionV3 as the pre-trained model. Training was done for 20 epochs and the classes were weighted during training in order to neutralize the imbalanced class in the dataset. The training was done on Kaggle using the GPUs provided. More details of the experiments can be found [here](https://www.kaggle.com/code/abrahamowodunni/tb-project)

# Evaluation results
The result of the evaluation are as follows: - loss: 0.0923 - binary_accuracy: 0.9857 - precision: 0.9259 - recall: 0.9843
More information can be found in the plot below.
[Evaluation results of the TB model](https://github.com/owos/tb_project/blob/main/README.md)


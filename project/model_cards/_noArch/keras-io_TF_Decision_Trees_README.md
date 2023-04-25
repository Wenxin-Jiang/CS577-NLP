---
thumbnail:

tags:
- tabular-classification
- keras
- tensorflow

library_name: keras


license: apache-2.0

metrics:
- accuracy

model-index:
- name: TF_Decision_Trees
  results:
  - task: 
      type: structured-data-classification
    dataset:
      type: census
      name: Census-Income Data Set
    metrics:
    - type: accuracy
      value: 96.57
    - type: validation loss
      value: 0.227394    
 
---

# TensorFlow's Gradient Boosted Trees Model for structured data classification

Use TF's Gradient Boosted Trees model in binary classification of structured data <br />

* Build a decision forests model by specifying the input feature usage.
* Implement a custom Binary Target encoder as a Keras Preprocessing layer to encode the categorical features with respect to their target value co-occurrences, and then use the encoded features to build a decision forests model.<br />
 
The model is implemented using Tensorflow 7.0 or higher. The US Census Income Dataset containing approximately 300k instances with 41 numerical and categorical variables was used to train it. This is a binary classification problem to determine whether a person makes over 50k a year.<br /> 

Author: Khalid Salama   
Adapted implementation: Tannia Dubon
Find the colab notebook at https://github.com/tdubon/TF-GB-Forest/blob/c0cf4c7e3e29d819b996cfe4eecc1f2728115e52/TFDecisionTrees_Final.ipynb

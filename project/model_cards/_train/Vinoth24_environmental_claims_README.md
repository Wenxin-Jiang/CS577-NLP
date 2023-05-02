---
widget:
- text: "The reduction of carbon emissions is improving for the last 2 years."
  example_title: "Example 1"
  candidate_labels: "Related to Environmental Claims, Not related to Environmental Claims"
- text: "The weather is very sunny today."
  example_title: "Example 2"
  
  
language: en
datasets:
- climatebert/environmental_claims
tags:
- Text Classification
- environmental-claims
- bert-base-uncased
model-index:
- name: Vinoth24/environmental_claims
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: environmental-claims
      type: environmental-claims
      config: environmental-claims
      split: validation & test
    metrics:
    - name: Loss
      type: loss
      value: 0.488700
---


# Model Card for environmental-claims
### Model Description
The environmental-claims model is fine-tuned using the EnvironmentalClaims dataset on Bert base-uncased model. This model is fine-tuned with the help of Happy Transformers on the Bert base-uncased model. The EnvironmentalClaims dataset is annotated by finance and sustainable finance students and authors of Zurich University. This model is expected to predict whether the input sequence is related to real-time environmental claims or not. 


# Usage
### loading the model :
```python
from happytransformer import HappyTextClassification
happy_class = HappyTextClassification(model_type="BERT", model_name="Vinoth24/environmental_claims")
```
### prediction :
```python
result = happy_class.classify_text('The reduction of carbon emissions is improving for the last 2 years.')
print(result) -- TextClassificationResult(label='LABEL_1', score=0.9948860359191895)
print(result.label) -- LABEL_1
print(result.score) -- 0.994
```

### Result Interpretation:
LABEL_1 - Related to Environmental Claims <br />
LABEL_0 - Not Related to Environmental Claims

Feel free to train the model more with your custom Environmental claims data. Any queries will be answered. <br />Thank you! :)

Created by Kasi Vinoth S from India
---
tags:
- tabular-classification
- sklearn
dataset:
- titanic
widget:
  structuredData:
    PassengerId:
      - 1191
    Pclass:
      - 1
    Name:
      - Sherlock Holmes
    Sex:
      - male
    SibSp:
      - 0
    Parch:
      - 0
    Ticket:
      - C.A.29395
    Fare:
      - 12
    Cabin:
      - F44
    Embarked:
      - S
---

## Titanic (Survived/Not Survived) - Binary Classification

### How to use

```python
from huggingface_hub import hf_hub_url, cached_download
import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

REPO_ID = 'danupurnomo/dummy-titanic'
PIPELINE_FILENAME = 'final_pipeline.pkl'
TF_FILENAME = 'titanic_model.h5'

model_pipeline = joblib.load(cached_download(
    hf_hub_url(REPO_ID, PIPELINE_FILENAME)
))

model_seq = load_model(cached_download(
    hf_hub_url(REPO_ID, TF_FILENAME)
))
```

### Example A New Data
```python
new_data = {
    'PassengerId': 1191,
    'Pclass': 1, 
    'Name': 'Sherlock Holmes', 
    'Sex': 'male', 
    'Age': 30, 
    'SibSp': 0,
    'Parch': 0, 
    'Ticket': 'C.A.29395', 
    'Fare': 12, 
    'Cabin': 'F44', 
    'Embarked': 'S'
}
new_data = pd.DataFrame([new_data])
```

### Transform Inference-Set
```python
new_data_transform = model_pipeline.transform(new_data)
```

### Predict using Neural Networks
```python
y_pred_inf_single = model_seq.predict(new_data_transform)
y_pred_inf_single = np.where(y_pred_inf_single >= 0.5, 1, 0)
print('Result : ', y_pred_inf_single)
# [[0]]
```
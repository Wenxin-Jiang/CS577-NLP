---
license: mit
tags:
- tabular-classification
- sklearn
- imodels
datasets:
- imodels/compas-recidivism
widget:
  structuredData:
    age:
      - 40.0
      - 25.0
      - 36.0
      - 23.0
      - 29.0
    priors_count:
      - 0.0
      - 1.0
      - 11.0
      - 1.0
      - 0.0
    days_b_screening_arrest:
      - -1.0
      - -1.0
      - -1.0
      - -1.0
      - 0.0
    c_jail_time:
      - 0.0
      - 1.0
      - 2.0
      - 0.0
      - -1.0
    juv_fel_count:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    juv_other_count:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    juv_misd_count:
      - 0.0
      - 0.0
      - 0.0
      - 1.0
      - 0.0
    c_charge_degree:F:
      - 0.0
      - 1.0
      - 0.0
      - 0.0
      - 0.0
    c_charge_degree:M:
      - 1.0
      - 0.0
      - 1.0
      - 1.0
      - 1.0
    race:African-American:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    race:Asian:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    race:Caucasian:
      - 1.0
      - 0.0
      - 1.0
      - 1.0
      - 1.0
    race:Hispanic:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    race:Native_American:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    race:Other:
      - 0.0
      - 1.0
      - 0.0
      - 0.0
      - 0.0
    age_cat:25_-_45:
      - 1.0
      - 1.0
      - 1.0
      - 0.0
      - 1.0
    age_cat:Greater_than_45:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    age_cat:Less_than_25:
      - 0.0
      - 0.0
      - 0.0
      - 1.0
      - 0.0
    sex:Female:
      - 0.0
      - 0.0
      - 0.0
      - 0.0
      - 0.0
    sex:Male:
      - 1.0
      - 1.0
      - 1.0
      - 1.0
      - 1.0
---


### Load the data

```python
from datasets import load_dataset
import imodels
import numpy as np
from sklearn.model_selection import GridSearchCV
import joblib

dataset = load_dataset("imodels/compas-recidivism")
df = pd.DataFrame(dataset['train'])
X_train = df.drop(columns=['is_recid'])
y_train = df['is_recid'].values

df_test = pd.DataFrame(dataset['test'])
X_test = df.drop(columns=['is_recid'])
y_test = df['is_recid'].values
```

### Load the model

```python
from huggingface_hub import hf_hub_url, cached_download
import joblib
import pandas as pd

REPO_ID = "imodels/figs-compas-recidivism"
FILENAME = "sklearn_model.joblib"

model = joblib.load(cached_download(
    hf_hub_url(REPO_ID, FILENAME)
))

# model is a `imodels.FIGSClassifier`
```

### Make prediction

```
preds = model.predict(X_test)
print('accuracy', np.mean(preds==y_test))
# accuracy 0.6759165485112416
```

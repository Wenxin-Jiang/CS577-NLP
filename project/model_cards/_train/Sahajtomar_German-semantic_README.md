---
language: de
tags:
- semantic
- sentence-transformers
- sentence-similarity
datasets:
- sts
---
# German STS

## STS dev (german)
87.9%
## STS test (german)
84.3%

#### STS pipeline
```python

!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('..model_path..')
sentences1 = ['Die Katze sitzt draußen',
             "Ein Mann spielt Gitarre",
             'Der neue Film ist großartig']

sentences2 = ['Der Hund spielt im Garten',
              "Eine Frau sieht fern",
              'Der neue Film ist so toll']
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

for i in range(len(sentences1)):
    for j in range(len(sentences2)):
        print(cosine_scores[i][j]))
"""
Die Katze sitzt draußen  Der Hund spielt im Garten  Score: 0.1259
Die Katze sitzt draußen  Eine Frau sieht fern Score: 0.0567
Die Katze sitzt draußen  Der neue Film ist so toll Score: 0.0557
Ein Mann spielt Gitarre  Der Hund spielt im Garten  Score: 0.1031
Ein Mann spielt Gitarre  Eine Frau sieht fern Score: 0.0098
Ein Mann spielt Gitarre  Der neue Film ist so toll  Score: 0.0828
Der neue Film ist großartig Der Hund spielt im Garten  Score: 0.1008
Der neue Film ist großartig Eine Frau sieht fern  Score: 0.0674
""" 
```
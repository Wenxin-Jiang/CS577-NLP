---
language: fr
tags:
- semantic
- sentence-transformers
- sentence-similarity
- fr
datasets:
- sts
---
# French STS
## STS dev (french)
87.4%
## STS test (french)
85.8%
#### STS pipeline
```python
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('..model_path..')
sentences1 = ["J'aime mon téléphone",
    "Mon téléphone n'est pas bon.",
    "Votre téléphone portable est superbe."]
    
sentences2 = ["Est-ce qu'il neige demain?",
    "Récemment, de nombreux ouragans ont frappé les États-Unis",
    "Le réchauffement climatique est réel",]
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
for i in range(len(sentences1)):
    for j in range(len(sentences2)):
        print(cosine_scores[i][j]))
"""
""" 
```
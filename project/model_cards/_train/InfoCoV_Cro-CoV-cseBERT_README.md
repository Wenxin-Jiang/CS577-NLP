## Usage:
```
from sentence_transformers import models
from sentence_transformers import SentenceTransformer

word_embedding_model = models.Transformer('Cro-CoV-cseBERT')
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens=True,
                               pooling_mode_cls_token=False,
                               pooling_mode_max_tokens=False)
model = SentenceTransformer(modules=[word_embedding_model, pooling_model], device='')  ## device = 'gpu' or 'cpu'
texts_emb = model.encode(texts)
```

## Datasets:
https://github.com/InfoCoV/InfoCoV

## Paper:
Please cite https://www.mdpi.com/2076-3417/11/21/10442
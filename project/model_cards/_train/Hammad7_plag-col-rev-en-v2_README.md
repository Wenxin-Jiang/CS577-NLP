---
license: apache-2.0
language: 
  - en
tags:
- plagiarism
- cross-encoder
---

## Usage:
from sentence_transformers.cross_encoder import CrossEncoder

model = CrossEncoder('Hammad7/plag-col-rev-en-v2')

model.predict(["duplicate first paragraph","original second paragraph"])
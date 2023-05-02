---
license: apache-2.0
---

## Usage:
from sentence_transformers.cross_encoder import CrossEncoder

model = CrossEncoder('Hammad7/plag-col-rev-en')

model.predict(["duplicate first paragraph","original second paragraph"])
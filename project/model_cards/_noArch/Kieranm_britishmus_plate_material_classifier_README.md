---
tags:
- fastai
- image-classification
---

# Model card

## Model description
A model trained to classify the material of European plates, as found in the British Museum collection. Initial model was trained using basic fastai workflow with timm integration.

## Intended uses & limitations
Should be able to predict the Material used (as defined by the British Museum) if that material was either porcelain,porcelain and gold, or earthenware with ~80% accuracy.
## Training and evaluation data
Was trained on images from the British Museum site, see link below
Examples to test can be found at: https://www.britishmuseum.org/collection/search?keyword=plate&object=plate&place=Europe&image=true&dateFrom=1700&eraFrom=ad&view=grid&sort=object_name__asc&page=1

Architecture: "vit_base_patch16_224_in21k"


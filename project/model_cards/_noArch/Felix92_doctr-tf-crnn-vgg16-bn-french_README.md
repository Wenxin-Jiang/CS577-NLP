---
language:
- en
- fr
- multilingual
pipeline_tag: image-to-text
---

<p align="center">
<img src="https://github.com/mindee/doctr/releases/download/v0.3.1/Logo_doctr.gif" width="60%">
</p>

**Optical Character Recognition made seamless & accessible to anyone, powered by TensorFlow 2 & PyTorch**

## Task: recognition

https://github.com/mindee/doctr

### Example usage:

```python
>>> from doctr.io import DocumentFile
>>> from doctr.models import ocr_predictor, from_hub

>>> img = DocumentFile.from_images(['<image_path>'])
>>> # Load your model from the hub
>>> model = from_hub('mindee/my-model')

>>> # Pass it to the predictor
>>> # If your model is a recognition model:
>>> predictor = ocr_predictor(det_arch='db_mobilenet_v3_large',
>>>                           reco_arch=model,
>>>                           pretrained=True)

>>> # If your model is a detection model:
>>> predictor = ocr_predictor(det_arch=model,
>>>                           reco_arch='crnn_mobilenet_v3_small',
>>>                           pretrained=True)

>>> # Get your predictions
>>> res = predictor(img)
```

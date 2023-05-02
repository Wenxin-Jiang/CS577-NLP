---
tags:
- generated_from_trainer
- endpoints-template
library_name: transformers
pipeline_tag: object-detection
widget:
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png"
  example_title: invoice
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/contract.jpeg"
  example_title: contract
datasets:
- funsd
model-index:
- name: layoutlm-funsd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlm-funsd

This model is a fine-tuned version of [microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased) on the funsd dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0045
- Answer: {'precision': 0.7348314606741573, 'recall': 0.8084054388133498, 'f1': 0.7698646262507357, 'number': 809}
- Header: {'precision': 0.44285714285714284, 'recall': 0.5210084033613446, 'f1': 0.47876447876447875, 'number': 119}
- Question: {'precision': 0.8211009174311926, 'recall': 0.8403755868544601, 'f1': 0.8306264501160092, 'number': 1065}
- Overall Precision: 0.7599
- Overall Recall: 0.8083
- Overall F1: 0.7866
- Overall Accuracy: 0.8106

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

## Deploy Model with Inference Endpoints

Before we can get started, make sure you meet all of the following requirements:

1. An Organization/User with an active plan and *WRITE* access to the model repository.
2. Can access the UI: [https://ui.endpoints.huggingface.co](https://ui.endpoints.huggingface.co/endpoints)



### 1. Deploy LayoutLM and Send requests

In this tutorial, you will learn how to deploy a [LayoutLM](https://huggingface.co/docs/transformers/model_doc/layoutlm) to [Hugging Face Inference Endpoints](https://huggingface.co/inference-endpoints) and how you can integrate it via an API into your products. 

This tutorial is not covering how you create the custom handler for inference. If you want to learn how to create a custom Handler for Inference Endpoints, you can either checkout the [documentation](https://huggingface.co/docs/inference-endpoints/guides/custom_handler) or go through [“Custom Inference with Hugging Face Inference Endpoints”](https://www.philschmid.de/custom-inference-handler) 

We are going to deploy [philschmid/layoutlm-funsd](https://huggingface.co/philschmid/layoutlm-funsd) which implements the following `handler.py` 

```python
from typing import Dict, List, Any
from transformers import LayoutLMForTokenClassification, LayoutLMv2Processor
import torch
from subprocess import run

# install tesseract-ocr and pytesseract
run("apt install -y tesseract-ocr", shell=True, check=True)
run("pip install pytesseract", shell=True, check=True)

# helper function to unnormalize bboxes for drawing onto the image
def unnormalize_box(bbox, width, height):
    return [
        width * (bbox[0] / 1000),
        height * (bbox[1] / 1000),
        width * (bbox[2] / 1000),
        height * (bbox[3] / 1000),
    ]

# set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class EndpointHandler:
    def __init__(self, path=""):
        # load model and processor from path
        self.model = LayoutLMForTokenClassification.from_pretrained(path).to(device)
        self.processor = LayoutLMv2Processor.from_pretrained(path)

    def __call__(self, data: Dict[str, bytes]) -> Dict[str, List[Any]]:
        """
        Args:
            data (:obj:):
                includes the deserialized image file as PIL.Image
        """
        # process input
        image = data.pop("inputs", data)

        # process image
        encoding = self.processor(image, return_tensors="pt")

        # run prediction
        with torch.inference_mode():
            outputs = self.model(
                input_ids=encoding.input_ids.to(device),
                bbox=encoding.bbox.to(device),
                attention_mask=encoding.attention_mask.to(device),
                token_type_ids=encoding.token_type_ids.to(device),
            )
            predictions = outputs.logits.softmax(-1)

        # post process output
        result = []
        for item, inp_ids, bbox in zip(
            predictions.squeeze(0).cpu(), encoding.input_ids.squeeze(0).cpu(), encoding.bbox.squeeze(0).cpu()
        ):
            label = self.model.config.id2label[int(item.argmax().cpu())]
            if label == "O":
                continue
            score = item.max().item()
            text = self.processor.tokenizer.decode(inp_ids)
            bbox = unnormalize_box(bbox.tolist(), image.width, image.height)
            result.append({"label": label, "score": score, "text": text, "bbox": bbox})
        return {"predictions": result}
```

### 2. Send HTTP request using Python

Hugging Face Inference endpoints can directly work with binary data, this means that we can directly send our image from our document to the endpoint. We are going to use `requests` to send our requests. (make your you have it installed `pip install requests`)

```python
import json
import requests as r
import mimetypes

ENDPOINT_URL="" # url of your endpoint
HF_TOKEN="" # organization token where you deployed your endpoint

def predict(path_to_image:str=None):
    with open(path_to_image, "rb") as i:
      b = i.read()
    headers= {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": mimetypes.guess_type(path_to_image)[0]
    }
    response = r.post(ENDPOINT_URL, headers=headers, data=b)
    return response.json()

prediction = predict(path_to_image="path_to_your_image.png")

print(prediction)
# {'predictions': [{'label': 'I-ANSWER', 'score': 0.4823932945728302, 'text': '[CLS]', 'bbox': [0.0, 0.0, 0.0, 0.0]}, {'label': 'B-HEADER', 'score': 0.992474377155304, 'text': 'your', 'bbox': [1712.529, 181.203, 1859.949, 228.88799999999998]},
```


### 3. Draw result on image

To get a better understanding of what the model predicted you can also draw the predictions on the provided image. 

```python
from PIL import Image, ImageDraw, ImageFont

# draw results on image
def draw_result(path_to_image,result):
  image = Image.open(path_to_image)
  label2color = {
      "B-HEADER": "blue",
      "B-QUESTION": "red",
      "B-ANSWER": "green",
      "I-HEADER": "blue",
      "I-QUESTION": "red",
      "I-ANSWER": "green",
  }

  # draw predictions over the image
  draw = ImageDraw.Draw(image)
  font = ImageFont.load_default()
  for res in result:
      draw.rectangle(res["bbox"], outline="black")
      draw.rectangle(res["bbox"], outline=label2color[res["label"]])
      draw.text((res["bbox"][0] + 10, res["bbox"][1] - 10), text=res["label"], fill=label2color[res["label"]], font=font)
  return image

draw_result("path_to_your_image.png", prediction["predictions"])
```
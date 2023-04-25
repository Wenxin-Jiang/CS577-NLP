---
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-distilled-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.94
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# Neuron conversation

# MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-distilled-clinc

This model is a fine-tuned version of [nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large](https://huggingface.co/nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.9389999

## Deploy/use Model

If you want to use this model checkout the following notenbook: [sagemaker/18_inferentia_inference](https://github.com/huggingface/notebooks/blob/main/sagemaker/18_inferentia_inference/sagemaker-notebook.ipynb)

```python
from sagemaker.huggingface.model import HuggingFaceModel


# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
   model_data=s3_model_uri,       # path to your model and script
   role=role,                    # iam role with permissions to create an Endpoint
   transformers_version="4.12",  # transformers version used
   pytorch_version="1.9",        # pytorch version used
   py_version='py37',            # python version used
)

# Let SageMaker know that we've already compiled the model via neuron-cc
huggingface_model._is_compiled_model = True

# deploy the endpoint endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1,      # number of instances
    instance_type="ml.inf1.xlarge" # AWS Inferentia Instance
)
```
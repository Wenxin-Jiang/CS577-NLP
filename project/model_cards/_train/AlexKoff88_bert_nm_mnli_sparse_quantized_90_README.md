---
license: apache-2.0
datasets:
- mnli
metrics:
- accuracy
tags:
- sequence-classification
- int8
---
 # Quantized BERT-base MNLI model with 90% of usntructured sparsity
 The pruned and quantized model in the OpenVINO IR. The pruned model was taken from this [source](https://huggingface.co/neuralmagic/oBERT-12-downstream-pruned-unstructured-90-mnli) and quantized with the code below using HF Optimum for OpenVINO:
 
 ```python
from functools import partial
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from optimum.intel.openvino import OVConfig, OVQuantizer

model_id = "neuralmagic/oBERT-12-downstream-pruned-unstructured-90-mnli" #"typeform/distilbert-base-uncased-mnli" 
model = AutoModelForSequenceClassification.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
save_dir = "./nm_mnli_90"

def preprocess_function(examples, tokenizer):
    return tokenizer(examples["premise"], examples["hypothesis"], padding="max_length", max_length=128, truncation=True)

# Load the default quantization configuration detailing the quantization we wish to apply
quantization_config = OVConfig()
# Instantiate our OVQuantizer using the desired configuration
quantizer = OVQuantizer.from_pretrained(model, feature="sequence-classification")
# Create the calibration dataset used to perform static quantization

calibration_dataset = quantizer.get_calibration_dataset(
    "glue",
    dataset_config_name="mnli",
    preprocess_function=partial(preprocess_function, tokenizer=tokenizer),
    num_samples=100,
    dataset_split="train",
)
# Apply static quantization and export the resulting quantized model to OpenVINO IR format
quantizer.quantize(
    quantization_config=quantization_config,
    calibration_dataset=calibration_dataset,
    save_directory=save_dir,
)
# Save the tokenizer
tokenizer.save_pretrained(save_dir)
 ```
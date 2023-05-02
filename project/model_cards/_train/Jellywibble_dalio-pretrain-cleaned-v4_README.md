---
tags:
- text-generation
library_name: transformers
widget:
- text: "This is a conversation where Ray Dalio is giving advice on being a manager and building a successful team.\nUser: Hi Ray, thanks for talking with me today. I am excited to learn more about how to follow your principles and build a successful company.\nRay: No problem, I am happy to help. What situation are you facing?\nUser: It feels like I keep making decisions without thinking first - I do something without thinking and then I face the consequences afterwards.\nRay:"
  example_title: "Q&A"
- text: "It’s easy to tell an open-minded person from a closed-minded person because they act very differently. Here are some cues to tell you whether you or others are being closed-minded: "
  example_title: "Principles"
---

## Model Description
Pre-training on cleaned version of Principles
- removing numeric references to footnotes
- removing numeric counts, i.e. 1) ... 2) ... 3) ...
- correcting gramma, i.e. full stops must be followed by a space
- finetuning OPT-30B model on the dataset above
- Dataset location: Jellywibble/dalio-principles-cleaned-v3

## Metrics
- Checkpoint 8 served
- Hellaswag Perplexity: 30.65
- 2.289 eval loss

wandb link: https://wandb.ai/jellywibble/huggingface/runs/2jqc504o?workspace=user-jellywibble

## Model Parameters
Trained on 4xA40, effective batchsize = 8
- base_model_name facebook/opt-30b
- dataset_name Jellywibble/dalio-principles-cleaned-v3
- block_size 1024
- gradient_accumulation_steps 2
- per_device_train_batch_size 1
- seed 2
- num_train_epochs 1
- learning_rate 3e-6

## Notes
- It is important for the effective batch size to be at least 8
- Learning rate higher than 3e-6 will result in massive overfitting, i.e. much worse Hellaswag metrics
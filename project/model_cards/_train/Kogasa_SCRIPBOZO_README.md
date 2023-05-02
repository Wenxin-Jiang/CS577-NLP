---
license: gpl-3.0


widget:
  - text: "@MOONMOON TAUNTED ELYOUEL SO BALD\n"
    example_title: "Taunted"
  - text: "JOHNSOULS\n"
    example_title: "JOHNSOULS"
  - inference:
      parameters:
        temperature: 0.6
        top_k: 0
        top_p: 0.92
        no_repeat_ngram_size: 6
        repetition_penalty: 1.6
        min_length: 1
        max_new_tokens: 256
---

# SCRIPBOZO

This model is based on GPT2-Medium finetuned on chat logs from twitch.tv/MOONMOON.

## Data 
The data consists of ~3.8GB of plaintext across 632 days of logs, ranging from 2021-01-01 to 2022-09-26. They were sourced from https://logs.ivr.fi/. The logs were cleaned by dropping
  - bots: messages from a (manually determined, non-exhaustive) list of bots
  - links: messages matching the regex
  
      `r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"`
      
  - long messages: messages longer than 300 characters
  - short messages: messages shorter than 2 characters
  - caps spam: messages containing more than 100 characters that are more than 80% capital letters
  - commands: messages starting with !
  
  
The data was batched into groups of up to 512 tokens, preferring to end on a newline (`\n`) rather than start another line and truncate it. The batches were then padded to 512 tokens using a pad token added to the model and tokenizer.
  
 10% of the data was set aside for validation.  
  
  
 ## Training
 Training was done on a system with a 6800XT (16GB of VRAM) and 32GB of RAM.  The following hyperparameters were used:
  - epochs: 1
  - learning rate: 3e-4
  - weight decay: 1e-4
  - warmup ratio: 0.01
  - optimizer: `adamw_torch`
  - gradient accumulation steps: 1
  - gradient checkpointing: `true`
  - fp16: true

## Evaluation
Evaluation was performed 10 times throughout training. Accuracy and perplexity were calculated. 
<details>
<summary>View Metrics</summary>

![Accuracy](./wandb_accuracy.png)
![Loss](./wandb_loss.png)

## Training Metrics
| Epochs | Validation Loss | Accuracy
 |--- |--- |--- |
| 0.1| 1.778| 0.6789|
| 0.2| 1.721| 0.6858|
| 0.3| 1.687| 0.6899|
| 0.4| 1.664| 0.6925|
| 0.5| 1.645| 0.695|
| 0.6| 1.63| 0.6969|
| 0.7| 1.616| 0.6987|
| 0.8| 1.604| 0.7003|
| 0.9| 1.594| 0.7017|
| 1.0| 1.588| 0.7025



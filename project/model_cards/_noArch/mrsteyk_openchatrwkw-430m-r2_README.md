---
license: agpl-3.0
language:
- en
pipeline_tag: text-generation
---

# OpenChatRWKV 430m r2

This is a finetune of RWKV-v4neo 430m on `openchatgpt safe r2` dataset. `r2` shares no data with the `r1`, even the greetings, making this finetune, in some ways, inferiour to the original on `r1`.

## Key differences with `openchatrwkv-430m`

One of the key differences is using an actual token for the instant message separation, apart from the new dataset.

## Differences with `openchatgpt-neox-125m`

Increased parameter size and different dataset.

## Training data

New dataset was obviously made at a later point in time. Many speculate that ChatGPT has degraded over the months, and I am a strong believer of that aswell - style in which model speaks started to sound different compared to 2-3 months ago.

This model was trained on a mix of natural language and code.

This model does not know how to greet you.
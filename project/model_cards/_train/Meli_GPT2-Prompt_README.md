---
language: 
- en
tags:
- gpt2
- text-generation
pipeline_tag: text-generation
widget:
- text: "A person with a high school education gets sent back into the 1600s and tries to explain science and technology to the people. [endprompt]"
- text: "A kid doodling in a math class accidentally creates the world's first functional magic circle in centuries. [endprompt]"
---

# GPT-2 Story Generator

## Model description

Generate a short story from an input prompt.

Put the vocab ` [endprompt]` after your input.

Example of an input:
```
A person with a high school education gets sent back into the 1600s and tries to explain science and technology to the people. [endprompt]
```

#### Limitations and bias

The data we used to train was collected from reddit, so it could be very biased towards young, white, male demographic.

## Training data

The data was collected from scraping reddit.
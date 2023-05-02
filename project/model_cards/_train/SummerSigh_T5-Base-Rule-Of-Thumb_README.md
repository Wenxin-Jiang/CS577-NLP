---
license: apache-2.0
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

This is a Flan-T5-Base model finetuned for different safety tasks. This model is planned to be used in Open Assistant, an Open Source chatGPT alternative. 

## Model Description

<!-- Provide a longer summary of what this model is. -->



- **Developed by:** SummerSigh 
- **Model type:** Flan-t5
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Finetuned from model [optional]:** flan-t5-base 

# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Used to generate Rules of Thumb. 

## Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
``` <user>"prompt" ```

``` <user>"prompt"<assistant>"response" ``` (you can keep chaining these for mutiple dialogue turns)

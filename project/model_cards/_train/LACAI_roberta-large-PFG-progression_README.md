---
license: mit
---

Base model: [roberta-large](https://huggingface.co/roberta-large)

Fine tuned as a progression model (to predict the acceptability of a dialogue) on the [Persuasion For Good Dataset](https://gitlab.com/ucdavisnlp/persuasionforgood) (Wang et al., 2019):

Given a complete dialogue from (or in the style of) Persuasion For Good, the task is to predict a numeric score typically in the range (-3, 3) where a higher score means a more acceptable dialogue in context of the donation solicitation task.

**Example input**: `How are you?</s>Good! how about yourself?</s>Great. Would you like to donate today to help the children?</s>`

For more context and usage information see [https://github.rpi.edu/LACAI/dialogue-progression](https://github.rpi.edu/LACAI/dialogue-progression).
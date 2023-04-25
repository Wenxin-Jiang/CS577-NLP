---
library_name: fastpitch
task: text-to-speech
tags:
- fastpitch
- waveglow
- text-to-speech
language: rw
datasets:
- mbazaNLP/kinyarwanda-tts-dataset
widget:
- text: "Muraho neza, murakaza neza mu Rwanda."
  example_title: "Muraho neza, murakaza neza mu Rwanda."
---

**Model card - Kinyarwanda TTS model**

**Model details**
- Kinyarwanda Text to Speech model
- Developed by [Digital Umuganda](digitalumuganda.com), [Arxia](https://www.arxia.com/home.html) and [Zevo Tech](https://zevo-tech.com/)
- Model based from: Fastspeech and Waveglow
- License: Mozilla 2.0 License
- Feedback on the model: samuel@digitalumuganda.com

**Metrics**
- We use Mean Opinion Score (MOS) to evaluate the model with a maximum score being 5

|Test Corpus|MOS|
|-----------|---|
|Custom phrases|3|

**Challenges**
- The model does not always capture the Kinyarwanda tones

**Recommendations**
- Use a tonal dictionary to train future models
- Add a numbers and symbols Dictionary
- Create a code-switching dictionary containing foreign words used in Kinyarwanda
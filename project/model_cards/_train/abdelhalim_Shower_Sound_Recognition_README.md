---
datasets:
- SHD-2
tags:
- audio
- audio-classificaiton
- shower detection
metrics:
- Accuracy 

---

**Context**

Most of our great brilliant ideas happen in periods of relaxation, like taking a
shower, however, once we leave the shower, we forget the brilliant idea. What if
we do not forget, and collect your ideas in the shower?

**What is the Shower Ideas concept?**

This is an app that detects when someone is taking a shower (douche) and asks
“do you have any idea?”, and the person will speak while taking the shower telling
the idea. And also will ask questions after taking a shower.

**Abstract about the model**

This model was trained based on *facebook/wav2vec2-base-960h* (which is a pretrained model on 960 hours of Librispeech on 16kHz sampled speech audio.) in order to classify the audio input into shower or no_shower. 

**Dataset**

The SHD-2 dataset is a labeled collection of 2260 audio recordings of shower and no shower sounds.

The dataset consists of 6-second-long recordings organized into 2 classes (with 1130 examples per class).

# Usage
In order to use the model in your Python script just copy the following code:
```python
from transformers import pipeline

audio_input = 'example.wav'
classifier = pipeline("audio-classification", model="abdelhalim/Shower_Sound_Recognition")
labels = classifier(audio_input)
labels

 ```
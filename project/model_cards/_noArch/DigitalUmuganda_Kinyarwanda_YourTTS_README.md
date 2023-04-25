---
language:
- rw
pipeline_tag: text-to-speech
---



## Model Description

<!-- Provide a longer summary of what this model is. -->
This model is an end-to-end deep-learning-based Kinyarwanda Text-to-Speech (TTS). Due to its zero-shot learning capabilities, new voices can be introduced with 1min speech.
The model was trained using the Coqui's TTS library,  and the YourTTS[1] architecture. It was trained on 67 hours of Kinyarwanda bible data, for 100 epochs.


## Data Sources

<!-- Provide the basic links for the model. -->

- **Audio data:** [www.faithcomesbyhearing.com, version -> Common Language Version audio Old Testament]
- **Text data:** [www.bible.com, version -> Bibiliya Ijambo ry'imana(BIR)(only the Old Testament was used)]

# Usage

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Install the Coqui's TTS library:
```
pip install git+https://github.com/coqui-ai/TTS@0910cb76bcd85df56bf43654bb31427647cdfd0d#egg=TTS
```
Download the files from this repo, then run: 

```
tts --text "text" --model_path model.pth --encoder_path SE_checkpoint.pth.tar --encoder_config_path config_se.json --config_path config.json --speakers_file_path speakers.pth --speaker_wav conditioning_audio.wav --out_path out.wav
```
Where the conditioning audio is a wav file(s) to condition a multi-speaker TTS model with a Speaker Encoder, you can give multiple file paths. The d_vectors is computed as their average.
# References
<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information should go in this section. -->
[1] [YourTTS paper](https://arxiv.org/pdf/2112.02418.pdf)

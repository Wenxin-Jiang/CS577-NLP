# Quran Speech Recognizer
This application will listen to the user's Quran recitation, and take the 
user to the position of the Quran from where the s/he had recited.
You can also take a look at our [presentation slides](https://docs.google.com/presentation/d/1dbbVYHi3LQRiggH14nN36YV2A-ddUAKg67aX5MWi0ys/edit?usp=sharing).

# Methodology
We used transfer learning to make our application. We fine-tuned the pretrained
model available at https://huggingface.co/elgeish/wav2vec2-large-xlsr-53-arabic
using the data available at https://www.kaggle.com/c/quran-asr-challenge/data.
Our model can be found at https://huggingface.co/Nuwaisir/Quran_speech_recognizer.

# Usage
Run all the cells of run_ui.ipynb. The last cell will hear your
recitation for 5 seconds (changeable) from the time you run that cell. And then convert your
speech to Arabic text and show the most probable corresponding parts of 30th juzz
(Surah 78 - 114) of the Quran as the output based on edit distance value.

Currently, we are searching from Surah 78 to Surah 114 as the searching
algorithm needs some time to search the whole Quran. This range can be changed
in the 6th cell of the notebook.
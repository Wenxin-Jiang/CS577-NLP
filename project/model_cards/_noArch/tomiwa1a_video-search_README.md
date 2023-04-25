---
license: gpl-3.0
tags:
- audio
- automatic-speech-recognition
- endpoints-template
library_name: generic
inference: false
duplicated_from: philschmid/openai-whisper-endpoint
---

# Video Search

This project contains 3 different models that can be used for searching videos.

1. Whisper to convert mp3 files to audio
2. BART Sentence Transformer to generate vector embeddings from text
3. BART LFQA to generate long form answers given a context

For more context, see: [Atlas: Find Anything on Youtube](https://atila.ca/blog/tomiwa/atlas)

Inspired by [philschmid/openai-whisper-endpoint](https://huggingface.co/philschmid/openai-whisper-endpoint)
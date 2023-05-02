---
language: en
datasets:
 - cnn_dailymail
 
license: apache-2.0
---

## DistilLED Large CNN 16384

*distil-led-large-cnn-16384* was initialized from [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6), in a fashion similar to [allenai/led-large-16384](https://huggingface.co/allenai/led-large-16384).

To be able to process 16K tokens, *sshleifer/distilbart-cnn-12-6*'s position embedding matrix was simply copied 16 times.

This checkpoint should be loaded into `LEDForConditionalGeneration.from_pretrained`. See the [LED documentation](https://huggingface.co/transformers/model_doc/led.html) for more information.
---
tags:
- ocr
- computer vision
- object detection
- image-to-text
license:
- cc0-1.0
---

## Keras Implementation of OCR model for reading captcha 🤖🦹🏻

This repo contains the model and the notebook [to this Keras example on OCR model for reading captcha](https://keras.io/examples/vision/captcha_ocr/).

Full credits to: [Aakash Kumar Nain](https://twitter.com/A_K_Nain)

## Background Information 
This example demonstrates a simple OCR model built with the Functional API. Apart from combining CNN and RNN, it also illustrates how you can instantiate a new layer and use it as an "Endpoint layer" for implementing CTC loss. 
This model uses subclassing, learn more about subclassing from [this guide](https://keras.io/guides/making_new_layers_and_models_via_subclassing/).
![ocr](https://keras.io/img/examples/vision/captcha_ocr/captcha_ocr_19_1.png)


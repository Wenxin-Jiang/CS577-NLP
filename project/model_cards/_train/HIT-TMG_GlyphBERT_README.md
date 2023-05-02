---
language: 
  - zh  
tags:  
- bert-base-chinese  
license: afl-3.0
---
This project page is about the pytorch code implementation of GlyphBERT by the HITsz-TMG research group.  
 
![img.png](https://s3.amazonaws.com/moonup/production/uploads/1661697350102-621a2b96100edd793f521ab6.png)  


GlyphBERT is a Chinese pre-training model that includes Chinese character glyph features.It renders the input characters into images and designs them in the form of multi-channel location feature maps, and designs a two-layer residual convolutional neural network module to extract the image features of the characters for training.  
  

The experimental results show that the performance of the pre-training model can be well improved by fusing the features of Chinese glyphs. GlyphBERT is much better than BERT in multiple downstream tasks, and has strong transferability.


For more details about using it, you can check the [github repo](https://github.com/HITsz-TMG/GlyphBERT)
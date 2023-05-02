---
license: other
widget:
- text: "There was a ghost"
  example_title: "First Prompt used in video"
- text: "I was playing Terraria but then"
  example_title: "Second prompt used in video"
inference:
  parameters:
    temperature: 0.6
    repetition_penalty: 1.15
    min_length: 128
    max_length: 468
---

This is the model trained for this video:

https://www.youtube.com/watch?v=OEPL5Tm3mmQ

Due to hardware limitations, I trained this model with only a batch size of 2. (I know this isn't ideal).

The quality of the model may be affected.

After training was complete, the best model according to a hold-out set was used.

This model was trained using a filtered version of this dataset:
 
https://www.kaggle.com/datasets/thomaskonstantin/3500-popular-creepypastas

This dataset had a lot of blank entries and missing text.

Please subscribe to my YouTube Channel for bad quality videos and poorly trained models. 

https://www.youtube.com/channel/UCLXxfueCPZRZnyGFWJ07uqA
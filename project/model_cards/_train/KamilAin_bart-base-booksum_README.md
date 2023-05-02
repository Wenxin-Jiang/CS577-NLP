---
language: en
license: apache-2.0

tags:
- booksum
- summary
- summarization
- book
metrics:
- rouge
widget:
- text: "In the dead night, Frodo lay in a dream without light. Then he saw the young moon rising; under its thin light there loomed before him a black wall of rock, pierced by a dark arch like a great gate. It seemed to Frodo that he was lifted up, and passing over he saw that the rock-wall was a circle of hills, and that within it was a plain, and in the midst of the plain stood a pinnacle of stone, like a vast tower but not made by hands. On its top stood the figure of a man. The moon as it rose seemed to hang for a moment above his head and glistened in his white hair as the wind stirred it. Up from the dark plain below came the crying of fell voices, and the howling of many wolves. Suddenly a shadow, like the shape of great wings, passed across the moon. The figure lifted his arms and a light flashed from the staff that he wielded. A mighty eagle swept down and bore him away. The voices wailed and the wolves yammered. There was a noise like a strong wind blowing, and on it was borne the sound of hoofs, galloping, galloping, galloping from the East. ‘Black Riders!’ thought Frodo as he wakened, with the sound of the hoofs still echoing in his mind. He wondered if he would ever again have the courage to leave the safety of these stone walls. He lay motionless, still listening; but all was now silent, and at last he turned and fell asleep again or wandered into some other unremembered dream."
  example_title: "book example"
  
datasets:
- kmfoda/booksum
---
# BART-base-Booksum

This is a BART-base model fine-tuned on a BookSum dataset

- **Use cases:** book summarization, general text summarization. 
- This is a [`https://huggingface.co/facebook/bart-base`](https://huggingface.co/facebook/bart-base), fine-tuned for five epochs 

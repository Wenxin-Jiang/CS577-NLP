---

widget:
- text: "Earth [MASK] is a growing field."
- text: "Multiple [MASK] channels enable full polarimetry"
- text: "The [MASK] is capable of measuring in limb and nadir geometry"

---

# RemoteSensing Distilbert

![alt text](https://media.istockphoto.com/photos/space-communications-satellite-in-low-orbit-around-the-earth-elements-picture-id1062473882?b=1&k=20&m=1062473882&s=170667a&w=0&h=KWJwGSiXBffLgKdaQTxY-eY7ljJE5_3khXgQyAQHPbU=)

The field of earth observation is increasingly growing. More and more data scientists are interested about this domain, and they're developing computer vision applications that do amazing things, while NLP doesn't seem to be given much consideration in this area
That's why I posted [Chramer/remote-sensing-distilbert-cased](https://huggingface.co/Chramer/remote-sensing-distilbert-cased). This is masked language model trained on a corpus of technical information about space missions, instruments, and sensors.

The model is based on [distilbert-base-cased](https://huggingface.co/distilbert-base-uncased), but I didn't have the chance to play with the hyperparameters of the model because of the limited computational capabilities I have. So there's a lot to improve! 😆

It was fun to publish my first model on hugging face! 🤩

**Author:** Marcello Politi ([Twitter 🐦](https://twitter.com/_March08_) ,[LinkedIn 💼](https://www.linkedin.com/in/marcello-politi/)).

# Perplexity 

Test set: 4.5k sentences about technical space stuff.

| Model | Perplexity | 
| ------ | ------ | 
| remote-sensing-distilbert-cased | **6.45**  | 
| distilbert-base-cased | 33.77  |


# Usage

```python
from transformers import AutoModel, AutoTokenizer
model_name = "Chramer/remote-sensing-distilbert-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
```

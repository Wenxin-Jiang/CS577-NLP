---
tags:
- image-to-text
- image-captioning
license: apache-2.0
widget:
- src: https://pixabay.com/get/ga187b8f146a9fa30b1f553d63fa94271e023868cd247fbad7ce02b6ffb5718a52fc04809be440f997f57dad90614dde2e9821edf8e628925f0042c6584fc04ec809421a040e3bc9561324249ab6e09c4_1280.jpg
  example_title: Horse Riding
- src:  https://static1.bigstockphoto.com/6/8/2/large1500/286059499.jpg
  example_title: Bicycle 
---


This is an image captioning model training by Zayn


```python

from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer

model = VisionEncoderDecoderModel.from_pretrained("Zayn/AICVTG_What_if_a_machine_could_create_captions_automatically")
feature_extractor = ViTFeatureExtractor.from_pretrained("Zayn/AICVTG_What_if_a_machine_could_create_captions_automatically")
tokenizer = AutoTokenizer.from_pretrained("Zayn/AICVTG_What_if_a_machine_could_create_captions_automatically")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)



max_length = 20
num_beams = 8
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_paths):
  images = []
  for image_path in image_paths:
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  return preds


predict_step(['Image URL.jpg'])


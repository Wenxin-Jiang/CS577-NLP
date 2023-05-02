# CLIPfa: Connecting Farsi Text and Images
OpenAI released [`the paper Learning Transferable Visual Models From Natural Language Supervision`](https://arxiv.org/abs/2103.00020) in which they present the CLIP (Contrastive Language–Image Pre-training) model. This model is trained to connect text and images, by matching their corresponding vector representations using a contrastive learning objective. CLIP consists of two separate models, a vision encoder and a text encoder. These were trained on 400 Million images and corresponding captions. We have trained a Farsi (Persian) version of OpenAI's CLIP on a dataset of 400,000 (image, text) pairs. We used [`Farahani's RoBERTa-fa`](https://huggingface.co/m3hrdadfi/roberta-zwnj-wnli-mean-tokens) as the text encoder and [‍‍`ViT‍`](https://huggingface.co/openai/clip-vit-base-patch32) as the vision encoder from Original CLIP and finetuned them.


- It should be noted that only 400K pairs were used for this training, whereas 4 million pairs were used for the Original CLIP. Also, the training took 30 days across 592 GPUs powered by the V100 chip.
 

## How to use?
Both models generate vectors with 768 dimensions.
```python
from transformers import CLIPVisionModel, RobertaModel, AutoTokenizer, CLIPFeatureExtractor
# download pre-trained models
vision_encoder = CLIPVisionModel.from_pretrained('SajjadAyoubi/clip-fa-vision')
preprocessor = CLIPFeatureExtractor.from_pretrained('SajjadAyoubi/clip-fa-vision')
text_encoder = RobertaModel.from_pretrained('SajjadAyoubi/clip-fa-text')
tokenizer = AutoTokenizer.from_pretrained('SajjadAyoubi/clip-fa-text')
# define input image and input text
text = 'something'
image = PIL.Image.open('my_favorite_image.jpg')
# compute embeddings
text_embedding = text_encoder(**tokenizer(text,
                                          return_tensors='pt')).pooler_output
image_embedding = vision_encoder(**preprocessor(image, 
                                                return_tensors='pt')).pooler_output
text_embedding.shape == image_embedding.shape
```

## Demo:
The followings are just some use cases of CLIPfa on 25K [`Unsplash images`](https://github.com/unsplash/datasets)
- use `pip install -q git+https://github.com/sajjjadayobi/clipfa.git`
```python
from clipfa import CLIPDemo
demo = CLIPDemo(vision_encoder, text_encoder, tokenizer)
demo.compute_text_embeddings(['گاو' ,'اسب' ,'ماهی'])
demo.compute_image_embeddings(test_df.image_path.to_list())
```

## Online Demo: [CLIPfa at Huggingface🤗 spaces](https://huggingface.co/spaces/SajjadAyoubi/CLIPfa-Demo)
We used a small set of images (25K) to keep this app almost real-time, but it's obvious that the quality of image search depends heavily on the size of the image database. 

> Made with ❤️ in my basement🤫

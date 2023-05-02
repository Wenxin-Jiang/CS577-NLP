Pretrained K-mHas with multi-label model with "koelectra-v3"

You can use tokenizer of this model with "monologg/koelectra-v3-base-discriminator"

dataset : https://huggingface.co/datasets/jeanlee/kmhas_korean_hate_speech

pretrained_model : https://huggingface.co/monologg/koelectra-base-v3-discriminator

label maps are like this.
>>>
    {'origin': 0,
     'physical': 1,
     'politics': 2,
     'profanity': 3,
     'age': 4,
     'gender': 5,
     'race': 6,
     'religion': 7,
     'not_hate_speech': 8}

You can use label map with below code.
>
    
    from huggingface_hub import hf_hub_download

    repo_id = "JunHwi/kmhas_multilabel"

    filename = "kmhas_dict.pickle" # 위 repo_id에 업로드한 파일 이름

    label_dict = hf_hub_download(repo_id, filename)

    with open(label_dict, "rb") as f:
        label2num = pickle.load(f)
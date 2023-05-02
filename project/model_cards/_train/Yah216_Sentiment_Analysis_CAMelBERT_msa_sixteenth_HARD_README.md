---
language: ar
widget:
 - text: "ممتاز"
 - text: "أنا حزين"
 - text: "لا شيء"
---

# Model description

This model is an Arabic language sentiment analysis pretrained model.
The model is built on top of the CAMelBERT_msa_sixteenth BERT-based model.
We used the HARD dataset of hotels review to fine tune the model.
The dataset original labels based on a five-star rating were modified to a 3 label data: 
- POSITIVE: for ratings > 3 stars
- NEUTRAL: for a 3 star rating
- NEGATIVE: for ratings < 3 stars

This first prototype was trained on 3 epochs for 1 hours using Colab and a TPU acceleration.
# Examples

Here are some examples in Arabic to test :
- Excellent -> ممتاز(Happy)
- I'am sad -> أنا حزين (Sad)
- Nothing -> لا شيء (Neutral)

# Contact
If you have questions or improvement remarks, feel free to contact me on my LinkedIn profile: https://www.linkedin.com/in/yahya-ghrab/
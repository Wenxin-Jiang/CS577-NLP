---
language: 
  - eng
tags:
- Tweet
- Twitter
- Clickbait
- Spam
license: apache-2.0
datasets:
- Webis-Clickbait-17
widget:
- text: "In just 4 days you can increase your net worth."
- text: "Nasa aborts second attempt to launch giant Moon rocket"
- text: "The most successful people do these 18 things next Tuesday."
- text: "Two guns used in shooting that killed nine-year-old"
---

This model classifies whether a tweet is clickbait or not. It has been trained using [Webis-Clickbait-17](https://webis.de/data/webis-clickbait-17.html) dataset. Input is composed of 'postText'. Achieved ~0.7 F1-score on test data. 

In order to test this model, try a tweet on the right!
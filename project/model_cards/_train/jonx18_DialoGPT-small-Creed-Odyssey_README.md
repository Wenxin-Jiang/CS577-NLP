# Summary
The app was conceived with the idea of recreating and generate new dialogs for existing games.
In order to generate a dataset for training the steps followed were:
1. Download from [Assassins Creed Fandom Wiki](https://assassinscreed.fandom.com/wiki/Special:Export) from the category "Memories relived using the Animus HR-8.5".
2. Keep only text elements from XML.
3. Keep only the dialog section.
4. Parse wikimarkup with [wikitextparser](https://pypi.org/project/wikitextparser/).
5. Clean description of dialog's context.
Due to the small size of the dataset obtained, a transfer learning approach was considered based on a pretrained ["Dialog GPT" model](https://huggingface.co/microsoft/DialoGPT-small).
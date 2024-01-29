# Auto Tagger for searches

This repository is created to categorize searches, titles, and question bodies based on the programming language they pertain to.

Within this repository, you'll find three Google Colab notebooks:

SCAI_dataprep.ipynb is dedicated to data preparation.
The next two notebooks correspond to different approaches employed for tagging:

SCAI_NER.ipynb utilizes Named Entity Recognition (NER).
SCAI_class_tagger.ipynb employs a multi-label, multi-class classification approach.
The models for NER and classification are constructed using basic models with libraries such as spaCy and scikit-learn, as well as advanced transformer-based models like DistilBERT.


Additionally, there is a main.py file that serves as an API.


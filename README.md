# Starbucks Capstone Project

This project is taking test data from Starbucks about offers and their inference on customers and does data analysis for creating value out of this data.

An attempt was made to answer the following questions:
1. Which income does most of the customers have and how it affects their spending?
2. How does Membership duration affect customer behavior?
3. How do different demographics respond to offers?

Please finy my blog post here:
https://medium.com/@dan-winter/how-starbucks-could-improve-their-offers-67c3ec00bada

Used Frameworks:
- pandas
- numpy
- datetime
- json
- scikit-learn (was not used for the final outcome but was used to play around with my data)

Data in this repository:
```plaintext
.
├── README.md README ** file with the most important information **
├── Starbucks_Capstone_notebook.ipynb ** Jupyter Notebook where all steps from my Blog post were performed **
├── data ** folder where all the data files are stored **
│   ├── cleaned_portfolio.csv ** cleaned portfolio data **
│   ├── cleaned_profile.csv ** cleaned profile data **
│   ├── cleaned_transcript.csv ** cleaned transcript data **
│   ├── merged_data.csv ** merged dataset where all cleaned datasets were used for **
│   ├── merged_dataset_features.csv ** merged dataset with features **
│   ├── portfolio.json ** original Portfolio data **
│   ├── profile.json ** original Profile data **
│   └── transcript.json ** original transcript data **
├── future_model.py ** python file where I wanted to train a model, just for me to come back at a later point **
├── output ** folder where my graphics are saved **
│   ├── demo_gender.png
│   ├── demo_offer_type.png
│   ├── event_membership_duration.png
│   ├── income_overall.png
│   ├── income_relative.png
│   └── offer_type_membership_duration.png
├── pic1.png ** file for description use **
└── pic2.png ** file for description use **
```
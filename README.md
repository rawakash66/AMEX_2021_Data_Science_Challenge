# AMEX_2021_Data_Science_Challenge
Data downloaded from the Competition portal. Data is proprietary content of American Express. Shared for educational purpose only.

## Problem Statement
Given all the text that might appear in an invoice image, classify all the text segments into pre-defined categories such as merchant name/address/total, etc. The details of input and output method can be found [here](https://github.com/rawakash66/AMEX_2021_Data_Science_Challenge/blob/main/Amex%20Campus%20Challenge%20Data%20Science.pdf).

## Expected Result
Predicted Label/Class information for every text segment in the validation and test observations

## Evaluation Metrics
Label fields for every text segment appearing in input JSON would be used to evaluate the F1 Score for each image. Final score is the average F1 scores across all test invoice.
Ref: [Scikit-Learn F1 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)

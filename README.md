# FetchMLEassessment
This is my code for the Fetch MLE assessment 2023

## How to execute

To execute, go to your terminal and navigate to the directory that "Fetch_assesment.py" is in. Then type "python3 Fetch_assessment.py" and enter the number of the month you want to see the number of receipts for, or type "exit" to quit.

## Methodology

Since the problem states that we want the number of receipts in a particular month of 2022, I understood that as the total number of receipts in that month. Thus, I took the total number of receipts for the months of 2021 and used that as my dataset. Because the number of days varies by month, I decided to use the number of days in the month as a feature.

I decided to make a linear classifier for this problem. To find the optimal weights, I took the closed-form formula of $ w = (X^T X)^{-1} X^T y $, where w is the weight, X is the feature matrix, and y is the desired output (number of receipts). With the way I formed the data, w has two values (weights), the first for the month number and the second for the number of days in that month, so the output goes like this: # receipts = w1 * month + w2 * # days in month

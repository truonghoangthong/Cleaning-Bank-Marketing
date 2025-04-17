# Cleaning Bank Marketing 

## Project Overview

I put this project together to help a bank clean up their marketing data for a personal loan campaign. The goal was to take a messy `bank_marketing.csv` file, tidy it up, and split it into three neat DataFrames—`client`, `campaign`, and `economics`.

This project has few key tasks:

- Splits and cleans the `bank_marketing.csv` dataset into three focused DataFrames based on the bank’s requirements.
- Reformats the data to match specific columns and data types outlined in the notebook.
- Saves the results as `client.csv`, `campaign.csv`, and `economics.csv` for easy database import.
- Sets the stage for analyzing personal loan campaigns, which are a big deal with UK banks earning \~£300M in interest from £1.5B in loans in September 2022 alone!

## Dataset
- `bank_marketing.csv`: The raw dataset with customer, campaign, and economic details from the bank’s loan marketing campaign.

The raw data was provided by the bank, and the notebook guided the column selection and formatting.

## Analysis

I used Python to clean, split, and reformat the data. Here’s how I tackled it:

1. **Data Cleaning**:
   - Loaded `bank_marketing.csv` and dug into its columns to identify customer, campaign, and economic data.
   - Dealt with some messy entries—like inconsistent data types or missing values.
2. **Data Splitting**:
   - Subset the data into three DataFrames: `client`, `campaign`, and `economics`, based on the notebook’s column requirements.
   - Made sure each DataFrame only included the specified columns, keeping things lean and focused.
3. **Data Reformatting**:
   - Converted columns to the exact data types listed in the notebook (e.g., strings for names, integers for counts, floats for rates).
4. **Data Storage**:
   - Saved the three DataFrames as `client.csv`, `campaign.csv`, and `economics.csv` in the `result/` folder, without indices for clean database loading.
   - Kept the process organized so the bank can easily use the files for their database and future campaigns.

## Repository Structure
- `result/`: Holds the Output data files (`client.csv`, `campaign.csv`, `economics.csv`).
- `main.py`: My Python script for the full analysis
- `bank-marketing.csv`: File of Summary Results

## Results
The script outputs:
- The client list contains customer information.
- The campaign list holds campaign-related data.
- The economics list includes economic indicators.

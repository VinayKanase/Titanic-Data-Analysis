# Titanic Data Analysis Project

## Overview

This project is part of an internal assessment for the Principles of Data Science (PDS) subject. It involves analyzing the Titanic dataset to extract meaningful insights and visualize the data. The analysis is performed using Python, with libraries such as Pandas, Matplotlib, and Seaborn.

## Files

- **main.py**: The main script that performs data analysis on the Titanic dataset.
- **output/output.txt**: Contains the results of the data analysis, including survival rates, gender proportions, and more.
- **PDS_IA2_project_2024.pdf**: A PDF document related to the project.

## Data Analysis

The analysis performed in `main.py` includes:

1. **Survival Rate Calculation**:
   - Overall survival rate of passengers.
2. **Gender Proportion**:
   - Distribution of male and female passengers.
3. **Survival Rate by Class**:
   - Survival rates for 1st, 2nd, and 3rd class passengers.
   - Identification of the class with the highest survival rate.
4. **Passengers with Siblings or Spouses Aboard**:
   - Count of passengers traveling with siblings or spouses.
5. **Average Fare by Class**:
   - Average fare paid by passengers in each class.
6. **Passengers by Port of Embarkation**:
   - Count of passengers who embarked from Cherbourg, Queenstown, and Southampton.
7. **Survival Rate by Gender**:
   - Survival rates for male and female passengers.
8. **Unique Ticket Numbers**:
   - Count of unique ticket numbers in the dataset.

## Visualizations

The script also generates visualizations for:

- **Age Distribution**: A histogram showing the distribution of passenger ages.
- **Fare Distribution by Class**: A boxplot showing fare distribution across different passenger classes.

## Output

The output is saved to `output/output.txt` and visualized figures are saved to `output/figures`.

## Usage

### Installation

```bash
pip3 install pandas matplotlib seaborn
# OR
pip3 install -r requirements.txt
```

### Running the analysis

To run the analysis, execute the `main.py` script. Ensure that the Titanic dataset is available at the specified file path in the script.

```bash
python main.py
```

## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

#=================================================
# Shizza Fatima Shafqat 
# June 2024
# covid19.py
# This program uses pandas for statistical analysis on covid19 data. 
# https://www.kaggle.com/datasets/patricklford/covid-19 (this is where I got my dataset)
#================================================= 
import pandas as pd
from sklearn.model_selection import train_test_split

# Reading in the data 
df = pd.read_csv('COVID-19.csv', low_memory=False)

# Cleaning the dataset
df = df.drop(columns=['Country', 'Week number', 'Gender', 'Age', 'VARIABLE', 'Year'])  # Removing redundant columns 
df = df.drop(columns=['Flag Codes', 'Flags'])  # Removing columns I will not need 

print("------------------ Statistical Analysis ------------------")
# Calculating mean 
mean_value = df['Value'].mean()

# Calculating median 
median_value = df['Value'].median()

# Calculating mode
mode_variable = df['Variable'].mode()[0] 

# Calculating minimum value 
min_value = df['Value'].min()

# Calculating maximum value 
max_value = df['Value'].max()

# Calculating 75th percentile 
percentile_75 = df['Value'].quantile(0.75)

# Calculating distinct count 
distinct_count_year = df['YEAR'].nunique()

# Calculating total count 
total_count_age = df['AGE'].count()

def calculate_correlation(df, col1, col2):
    correlation = df[col1].corr(df[col2])
    return correlation

# Calculate correlation
correlation_value = calculate_correlation(df, 'YEAR', 'Value')

# Creating a DataFrame to show the results more neatly 
stats_df = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode', 'Minimum', 'Maximum', '75th Percentile', 'Distinct Count for YEAR', 'Total Count for AGE', 'Correlation(Year and Value)'],
    'Value': [mean_value, median_value, mode_variable, min_value, max_value, percentile_75, distinct_count_year, total_count_age, correlation_value]
})
stats_df.index = stats_df.index + 1  # So the index starts from 1 instead of 0 

print(stats_df)

print("------ Splitting the dataset for training and testing ------")

# Preparing the data for training/testing split
X = df.drop(['Value'], axis=1)  # Features (dropping the target variable)
y = df['Value']  # Target variable

# Split the data into a training set and a testing set (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Printing shapes of the train and test sets to confirm the split
print("Train set shape:", X_train.shape, y_train.shape)
print("Test set shape:", X_test.shape, y_test.shape)
# The split was successful since the testing set is smaller (20%) than the training set.

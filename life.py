import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/S21B0069/new-project-DS/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(data)

# Checking for Null Values
df.isnull().sum()

df = pd.DataFrame(df)
del df['GDP']

df.isnull().sum()

df.dropna(inplace=True)

df.isnull().sum()
df.shape
df.describe()

import matplotlib.pyplot as plt
# Creating dataset
data=df['Adult Mortality']
fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.boxplot(data)

# show plot
plt.show()


# Now you can use plt to create figures and plots:
fig = plt.figure(figsize=(10, 7))


import numpy as np
# Identify and remove outliers using the IQR method
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = (data < lower_bound) | (data > upper_bound)

# Print the indices of the outliers
print("Indices of outliers:", np.where(outliers))

# Remove outliers from the dataset
cleaned_data = data[~outliers]

# Creating a new boxplot without outliers
fig, ax = plt.subplots(figsize=(10, 7))
ax.boxplot(cleaned_data)

# Show the updated plot
plt.show()

new_df=df[df['Adult Mortality']<upper_bound]

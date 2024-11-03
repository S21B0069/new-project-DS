import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/S21B0069/new-project-DS/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

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

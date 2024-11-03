import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/S21B0069/new-project-DS/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

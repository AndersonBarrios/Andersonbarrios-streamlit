import pandas as pd
import matplotlib.pyplot as plt

# using pandas read_csv function to load the dataset
df = pd.read_csv("RTADataset.csv")
# target variable classes counts and bar plot
import matplotlib.pyplot as plt
print(df['Accident_severity'].value_counts())
print(df['Accident_severity'].value_counts().plot(kind='bar'))

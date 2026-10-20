
import pandas as pd

df = pd.read_csv("data/crop dataset/Crop_recommendation.csv")

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- First Five Rows ---")
print(df.head())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Crop Distribution ---")
print(df["label"].value_counts())

print("\n--- Summary Statistics ---")
print(df.describe())

import pandas as pd

try:
    df = pd.read_csv("fake_or_real_news.csv")
    print("Successfully read CSV.")
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
    print("First 5 rows of 'text' column:")
    print(df['text'].head())
except Exception as e:
    print("Error reading CSV:")
    print(e)

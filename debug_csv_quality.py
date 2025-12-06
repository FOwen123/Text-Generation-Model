import pandas as pd

try:
    df = pd.read_csv("fake_or_real_news.csv")
    print("Shape:", df.shape)
    print("Null values:\n", df.isnull().sum())
    print("Empty strings in text:", (df['text'] == "").sum())
    print("Whitespace only strings in text:", df['text'].str.isspace().sum())
    
    # Check if 'text' column exists
    if 'text' not in df.columns:
        print("ERROR: 'text' column not found!")
        print("Columns found:", df.columns)
    else:
        print("'text' column found.")
        
except Exception as e:
    print(e)

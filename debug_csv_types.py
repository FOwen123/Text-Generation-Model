import pandas as pd

df = pd.read_csv("fake_or_real_news.csv")
non_strings = df[~df['text'].apply(lambda x: isinstance(x, str))]
print("Non-string rows:", len(non_strings))
if len(non_strings) > 0:
    print(non_strings.head())

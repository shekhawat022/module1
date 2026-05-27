import pandas as pd


df = pd.read_csv("matches.csv")


print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())


print("\n--- MATCHES PER SEASON ---")
print(df['season'].value_counts().sort_index())


print("\n--- MOST SUCCESSFUL TEAM ---")
print(df['winner'].value_counts().head(1))


venue = "Wankhede Stadium"
print(f"\n--- MATCHES AT {venue} ---")
print(df[df['venue'] == venue])


print("\n--- TOP 5 PLAYERS OF THE MATCH ---")
print(df['player_of_match'].value_counts().head(5))


print("\n--- MISSING VALUES ---")
print(df.isnull().sum())


df_clean = df.dropna()
print("\n--- CLEANED DATA INFO ---")
print(df_clean.info())

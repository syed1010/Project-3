import pandas as pd
import matplotlib.pyplot as plt

# path to your CSV file
mentalHealthCSV = 'Music_mentalhealth.csv'

# CSV file into a DataFrame
mentalHealthdf = pd.read_csv(mentalHealthCSV)

# print(mentalHealthdf)

# new df with just music effect columm
df_music_effects = mentalHealthdf[['Music effects']]

# print(df_music_effects)

# removing empty rows
df_music_effects_clean = df_music_effects.dropna()

# Counting how many of each answer there was
music_effects_counts = df_music_effects_clean['Music effects'].value_counts()
print(music_effects_counts)

# print(df_music_effects_clean)

# Pie chart with total results overall
plt.figure(figsize=(8, 6))
plt.pie(music_effects_counts, labels=music_effects_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Music Effects Responses')
plt.show()
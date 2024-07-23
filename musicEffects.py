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
print(f'Overall for all ages: {music_effects_counts}')

# print(df_music_effects_clean)

custom_colors = ['violet', 'lightblue', 'pink']

# Pie chart with total results overall
# plt.figure(figsize=(8, 6))
# plt.pie(music_effects_counts, labels=music_effects_counts.index, autopct='%1.1f%%', startangle=140, colors=custom_colors)
# plt.title('Music Effects Responses')
# plt.show()

#-------------------------------------------------------------------------
# Age column data frame
df_ages = mentalHealthdf[['Age']]

# average age, median age
# Calculate the average age
average_age = df_ages['Age'].mean()
print(f"The average age is: {average_age}")

# Calculate the median age
median_age = df_ages['Age'].median()
print(f"The median age is: {median_age}")

# Calculate the min and max age
min_age = df_ages['Age'].min()
print(f"The minimun age is: {min_age}")

max_age = df_ages['Age'].max()
print(f"The maximum age is: {max_age}")

#-------------------------------------------------------------------------
# 13-25
# 26-40
# 41-55
# 56 and up
# what mental illness is most common in each age group and preferred genre
# and how they reported the effects of music overall

#-------------------------------------------------------------------------
# Data frame with both age and music effect column
df_age_and_music_effects = mentalHealthdf[['Age', 'Music effects']]
df_age_and_music_effects_clean = df_age_and_music_effects.dropna()

# DataFrame for the age range 13 to 25
df_13to25 = df_age_and_music_effects_clean[(df_age_and_music_effects_clean['Age'] >= 13) & 
                                             (df_age_and_music_effects_clean['Age'] <= 25)]
# Count the occurrences of each 'Music effects' value in the filtered DataFrame
music_effects_counts_13to25 = df_13to25['Music effects'].value_counts()
print(f'Overalls for Age ranges 13 to 25: {music_effects_counts_13to25}')

# DataFrame for the age range 26 to 40
df_26to40 = df_age_and_music_effects_clean[(df_age_and_music_effects_clean['Age'] >= 26) & 
                                           (df_age_and_music_effects_clean['Age'] <= 40)]

# Count the occurrences of each 'Music effects' value in the filtered DataFrame
music_effects_counts_26to40 = df_26to40['Music effects'].value_counts()
print(f'Overalls for Age ranges 26 to 40: {music_effects_counts_26to40}')

# DataFrame for the age range 41 to 55
df_41to55 = df_age_and_music_effects_clean[(df_age_and_music_effects_clean['Age'] >= 41) & 
                                           (df_age_and_music_effects_clean['Age'] <= 55)]

# Count the occurrences of each 'Music effects' value in the filtered DataFrame
music_effects_counts_41to55 = df_41to55['Music effects'].value_counts()
print(f'Overalls for Age ranges 41 to 55: {music_effects_counts_41to55}')

# DataFrame for the age range 56 and up
df_56andUp = df_age_and_music_effects_clean[df_age_and_music_effects_clean['Age'] >= 56]

# Count the occurrences of each 'Music effects' value in the filtered DataFrame
music_effects_counts_56andUp = df_56andUp['Music effects'].value_counts()
print(f'Overalls for Age range 56 and up: {music_effects_counts_56andUp}')

#-------------------------------------------------------------------------

# Data Frame for which mental illness is most common in each age group
df_age_and_mentalIllness = mentalHealthdf.loc[:, ['Age', 'Anxiety', 'Depression', 'Insomnia', 'OCD']]

# Filter the DataFrame for the age range 13 to 25
df_age_13to25 = df_age_and_mentalIllness[(df_age_and_mentalIllness['Age'] >= 13) & 
                                          (df_age_and_mentalIllness['Age'] <= 25)]

# Sum the values in each of the specified columns
sums = df_age_13to25[['Anxiety', 'Depression', 'Insomnia', 'OCD']].sum()

# Find the column with the highest sum
max_column = sums.idxmax()
max_value = sums.max()

print(f'The highest reported mental illness for the age range 13 to 25 is "{max_column}".')

# Filter the DataFrame for the age range 26 to 40
df_age_26to40 = df_age_and_mentalIllness[(df_age_and_mentalIllness['Age'] >= 26) & 
                                          (df_age_and_mentalIllness['Age'] <= 40)]

# Sum the values in each of the specified columns
sums = df_age_26to40[['Anxiety', 'Depression', 'Insomnia', 'OCD']].sum()

# Find the column with the highest sum
max_column = sums.idxmax()
max_value = sums.max()

print(f'The highest reported mental illness for the age range 26 to 40 is "{max_column}".')

# Filter the DataFrame for the age range 41 to 55
df_age_41to55 = df_age_and_mentalIllness[(df_age_and_mentalIllness['Age'] >= 41) & 
                                          (df_age_and_mentalIllness['Age'] <= 55)]

# Sum the values in each of the specified columns
sums = df_age_41to55[['Anxiety', 'Depression', 'Insomnia', 'OCD']].sum()

# Find the column with the highest sum
max_column = sums.idxmax()
max_value = sums.max()

print(f'The highest reported mental illness for the age range 41 to 55 is "{max_column}".')

# Filter the DataFrame for the age range 56 and up
df_age_56andUp = df_age_and_mentalIllness[df_age_and_mentalIllness['Age'] >= 56]

# Sum the values in each of the specified columns
sums = df_age_56andUp[['Anxiety', 'Depression', 'Insomnia', 'OCD']].sum()

# Find the column with the highest sum
max_column = sums.idxmax()
max_value = sums.max()

print(f'The highest reported mental illness for the age range 56 and up is "{max_column}".')

#-------------------------------------------------------------------------
# 13-25
# 26-40
# 41-55
# 56 and up
# DataFrame with the columns "Age" and "Fav genre"
df_age_and_fav_genre = mentalHealthdf.loc[:, ['Age', 'Fav genre']]

# Filter the DataFrame for the age range 13 to 25
df_age_13to25 = df_age_and_fav_genre[(df_age_and_fav_genre['Age'] >= 13) & 
                                     (df_age_and_fav_genre['Age'] <= 25)]

# Count the occurrences of each "Fav genre" in the filtered DataFrame
fav_genre_counts = df_age_13to25['Fav genre'].value_counts()

# Get the top 2 most common genres
top_2_genres = fav_genre_counts.head(2)

# Display the top 2 most common genres and their counts
for genre, count in top_2_genres.items():
    print(f'The genre "{genre}" is among the top 2 preferred genres for age ranges 13 to 25 with {count} occurrences.')

# Filter the DataFrame for the age range 26 to 40
df_age_26to40 = df_age_and_fav_genre[(df_age_and_fav_genre['Age'] >= 26) & 
                                     (df_age_and_fav_genre['Age'] <= 40)]

# Count the occurrences of each "Fav genre" in the filtered DataFrame
fav_genre_counts = df_age_26to40['Fav genre'].value_counts()

# Get the top 2 most common genres
top_2_genres = fav_genre_counts.head(2)

# Display the top 2 most common genres and their counts
for genre, count in top_2_genres.items():
    print(f'The genre "{genre}" is among the top 2 preferred genres for the age range 26 to 40 with {count} occurrences.')

# Filter the DataFrame for the age range 41 to 55
df_age_41to55 = df_age_and_fav_genre[(df_age_and_fav_genre['Age'] >= 41) & 
                                     (df_age_and_fav_genre['Age'] <= 55)]

# Count the occurrences of each "Fav genre" in the filtered DataFrame
fav_genre_counts = df_age_41to55['Fav genre'].value_counts()

# Get the top 2 most common genres
top_2_genres = fav_genre_counts.head(2)

# Display the top 2 most common genres and their counts
for genre, count in top_2_genres.items():
    print(f'The genre "{genre}" is among the top 2 preferred genres for the age range 41 to 55 with {count} occurrences.')

# Filter the DataFrame for the age range 56 and up
df_age_56andUp = df_age_and_fav_genre[df_age_and_fav_genre['Age'] >= 56]

# Count the occurrences of each "Fav genre" in the filtered DataFrame
fav_genre_counts = df_age_56andUp['Fav genre'].value_counts()

# Get the top 2 most common genres
top_2_genres = fav_genre_counts.head(2)

# Display the top 2 most common genres and their counts
for genre, count in top_2_genres.items():
    print(f'The genre "{genre}" is among the top 2 preferred genres for the age range 56 and up with {count} occurrences.')
    
       
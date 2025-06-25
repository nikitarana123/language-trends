import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('survey_results_public.csv')

# Use the correct column name from the 2021 survey
language_col = 'LanguageHaveWorkedWith'

# Drop rows with missing values in that column
df = df.dropna(subset=[language_col])

# Split and count each language
all_languages = df[language_col].str.split(';').explode()
language_counts = all_languages.value_counts()
top_10 = language_counts.head(10)

# Print top 10 in terminal
print("Top 10 programming languages:")
for lang, count in top_10.items():
    print(f"{lang}: {count}")

# Plot bar chart
plt.figure(figsize=(10, 6))
top_10.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Programming Languages (Stack Overflow Survey 2021)')
plt.xlabel('Programming Language')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

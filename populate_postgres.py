import pandas as pd
from sqlalchemy import create_engine

# Correct file path
file_path = '/Users/syedshahid/Project 3/Music_mentalhealth.csv'

# Load data into a DataFrame
df = pd.read_csv(file_path)

# Create connection string with URL-encoded password
conn_string = 'postgresql://postgres:Welcome%402024@localhost/music_mentalhealth'

# Create SQLAlchemy engine
engine = create_engine(conn_string)

# Write DataFrame to PostgreSQL
df.to_sql('music_data', engine, if_exists='replace', index=False)

print("PostgreSQL database created and data inserted successfully.")
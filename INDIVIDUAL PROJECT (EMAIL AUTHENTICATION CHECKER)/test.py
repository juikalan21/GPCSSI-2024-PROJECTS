import pandas as pd

# Load the CSV file
file_path = '/mnt/data/cdr.csv'
cdr_data = pd.read_csv(file_path)

# Calculate the total duration of calls for each caller
caller_duration = cdr_data.groupby('caller')['duration'].sum().reset_index(name='total_duration')

# Identify the caller with the highest total duration
top_caller = caller_duration.sort_values(by='total_duration', ascending=False).head(1)

print(top_caller)

import pandas as pd

# Create a dictionary with your data
weather = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

# Create a DataFrame (i.e., tabulation) from the dictionary
df = pd.DataFrame(weather)

# Display the table
print(df)
# Save the DataFrame to 'weather_data.csv' without including the index column
df.to_csv('weather_data.csv', index=False)
# Read data from 'weather_data.csv' into a DataFrame
import pandas as pd
df = pd.read_csv("weather_data.csv")  
#simple operations usig dataframe
df.shape  # Returns the shape (rows, columns) of the DataFrame → (6, 4)

df.head()  # Displays the first 5 rows of the DataFrame

df[1:3]  # Slices the DataFrame to return rows with index 1 and 2 (not including 3)

df['event']  # Extracts the 'event' column as a Series

df['day']  # Extracts the 'day' column as a Series


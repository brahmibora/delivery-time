import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("deliverytime.txt")

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Function to calculate distance using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Difference in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

# Apply the Haversine formula to calculate distance
data['Distance_km'] = data.apply(
    lambda row: haversine(
        row['Restaurant_latitude'], row['Restaurant_longitude'],
        row['Delivery_location_latitude'], row['Delivery_location_longitude']
    ), axis=1
)

# Select relevant features
features = ['Delivery_person_Age', 'Delivery_person_Ratings', 'Distance_km', 'Type_of_vehicle', 'Time_taken(min)']
data = data[features]

# Convert categorical variables to numerical using one-hot encoding
data = pd.get_dummies(data, columns=['Type_of_vehicle'], drop_first=True)

# Save the preprocessed data
data.to_csv("preprocessed_data.csv", index=False)
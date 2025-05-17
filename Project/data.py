import pandas as pd
import numpy as np
import random

# Function to generate a synthetic dataset
def generate_synthetic_data(num_rows=500):
    data = {
        'Gender': np.random.choice(['M', 'F'], size=num_rows),
        'Age': np.random.randint(18, 60, size=num_rows),
        'Name': ['Person_' + str(i) for i in range(1, num_rows + 1)],
        'Diabetes': np.random.choice(['Y', 'N'], size=num_rows),
        'Weight': [str(random.randint(50, 100)) + ' kg' for _ in range(num_rows)],
        'Wanna Loose Weight': np.random.choice(['YES', 'NO'], size=num_rows),
        'Height': [str(random.randint(150, 190)) + ' cm' for _ in range(num_rows)],
        'BMI': np.round(np.random.uniform(18.5, 30, num_rows), 2),
        'Calories': np.random.choice([1800, 2000, 2200, 2400, 2600, 2800, 3000, 3100], size=num_rows),
        'Exercise': np.random.choice(['Sedentary', 'Lightly Active', 'Moderate', 'Very Active', 'Super Active'], size=num_rows),
        'Workout': np.random.choice(['Sedentary Lifestyle', 'Light Exercise', 'Moderate Exercise', 'High intensity Exercise'], size=num_rows),
        'Meal Type': np.random.choice(['V', 'NV'], size=num_rows),
        'Diet': np.random.choice(['Balanced Diet', 'Energy boost diet', 'Light Activity Fuel', 'Fitness Diet'], size=num_rows)
    }

    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    return df

# Generate the synthetic data with 500 rows
synthetic_data = generate_synthetic_data(500)

# Display the first few rows of the generated dataset
print(synthetic_data.head())

# Save the generated data to a CSV file
synthetic_data.to_csv('synthetic_diet_data.csv', index=False)
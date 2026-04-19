import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

def generate_poll_data(n=1000):
    options = ["Apple", "Samsung", "OnePlus", "Xiaomi"]
    regions = ["North", "South", "East", "West"]
    age_groups = ["18-25", "26-35", "36-45", "46+"]
    genders = ["Male", "Female"]
    occupations = ["Student", "Working Professional", "Business", "Other"]

    start_date = datetime(2026, 1, 1)

    data = []

    for i in range(1, n + 1):
        row = {
            "Respondent_ID": i,
            "Date": start_date + timedelta(days=np.random.randint(0, 90)),
            "Question": "Preferred Smartphone Brand",
            "Selected_Option": np.random.choice(
                options,
                p=[0.35, 0.30, 0.20, 0.15]
            ),
            "Region": np.random.choice(regions),
            "Age_Group": np.random.choice(age_groups),
            "Gender": np.random.choice(genders),
            "Occupation": np.random.choice(occupations)
        }
        data.append(row)

    df = pd.DataFrame(data)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/poll_data.csv", index=False)

    print("poll_data.csv created successfully!")

if __name__ == "__main__":
    generate_poll_data()

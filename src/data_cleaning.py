import pandas as pd
import os

def clean_data():
    df = pd.read_csv("data/poll_data.csv")

    print("Original Shape:", df.shape)

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df["Selected_Option"] = df["Selected_Option"].str.strip()
    df["Region"] = df["Region"].str.strip()

    df["Date"] = pd.to_datetime(df["Date"])

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/cleaned_data.csv", index=False)

    print("Cleaned data saved successfully!")
    print("Cleaned Shape:", df.shape)

    return df

if __name__ == "__main__":
    clean_data()

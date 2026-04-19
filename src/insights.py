import pandas as pd

def generate_insights():
    summary = pd.read_csv("outputs/summary_report.csv")

    top_brand = summary.iloc[0]["Brand"]
    top_percentage = summary.iloc[0]["Percentage"]

    print("\n===== KEY INSIGHTS =====\n")
    print(f"Leading Brand: {top_brand}")
    print(f"Market Share: {top_percentage}%")
    print("This brand shows the strongest customer preference.")

if __name__ == "__main__":
    generate_insights()

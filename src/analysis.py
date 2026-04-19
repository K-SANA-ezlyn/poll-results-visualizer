import pandas as pd

def analyze_data():
    df = pd.read_csv("outputs/cleaned_data.csv")

    summary = df["Selected_Option"].value_counts().reset_index()
    summary.columns = ["Brand", "Votes"]

    total_votes = summary["Votes"].sum()
    summary["Percentage"] = round(
        (summary["Votes"] / total_votes) * 100, 2
    )

    region_analysis = pd.crosstab(
        df["Region"],
        df["Selected_Option"]
    )

    summary.to_csv("outputs/summary_report.csv", index=False)
    region_analysis.to_csv("outputs/region_analysis.csv")

    print("\nVote Share Summary:\n")
    print(summary)

    print("\nRegion-wise Analysis:\n")
    print(region_analysis)

    return summary, region_analysis

if __name__ == "__main__":
    analyze_data()

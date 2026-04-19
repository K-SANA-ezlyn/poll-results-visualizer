import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visualizations():
    summary = pd.read_csv("outputs/summary_report.csv")
    df = pd.read_csv("outputs/cleaned_data.csv")

    os.makedirs("outputs/charts", exist_ok=True)

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(summary["Brand"], summary["Votes"])
    plt.title("Vote Share by Brand")
    plt.xlabel("Brand")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.savefig("outputs/charts/bar_chart.png")
    plt.close()

    # Pie Chart
    plt.figure(figsize=(7, 7))
    plt.pie(
        summary["Votes"],
        labels=summary["Brand"],
        autopct="%1.1f%%"
    )
    plt.title("Vote Share Distribution")
    plt.savefig("outputs/charts/pie_chart.png")
    plt.close()

    # Region-wise chart
    region_analysis = pd.crosstab(
        df["Region"],
        df["Selected_Option"]
    )

    region_analysis.plot(
        kind="bar",
        figsize=(10, 6)
    )
    plt.title("Region-wise Brand Preference")
    plt.xlabel("Region")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.savefig("outputs/charts/region_chart.png")
    plt.close()

    print("Charts saved successfully!")

if __name__ == "__main__":
    create_visualizations()

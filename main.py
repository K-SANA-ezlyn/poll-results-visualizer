from src.generate_data import generate_poll_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import create_visualizations
from src.insights import generate_insights

def main():
    print("STEP 1: Generating Poll Data")
    generate_poll_data()

    print("\nSTEP 2: Cleaning Data")
    clean_data()

    print("\nSTEP 3: Running Analysis")
    analyze_data()

    print("\nSTEP 4: Creating Visualizations")
    create_visualizations()

    print("\nSTEP 5: Generating Insights")
    generate_insights()

    print("\nProject Completed Successfully!")

if __name__ == "__main__":
    main()

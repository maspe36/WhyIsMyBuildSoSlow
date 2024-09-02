import sys

import matplotlib.pyplot as plt
import pandas as pd

def main(log_path):
    csv_files = [f"{log_path}/one_include_path.csv",
                 f"{log_path}/ten_include_paths.csv",
                 f"{log_path}/hundred_include_paths.csv",
                 f"{log_path}/thousand_include_paths.csv"]

    # Load each CSV file into a DataFrame and store them in a list
    df = [pd.read_csv(file).T.values.flatten() for file in csv_files]

    boxes = plt.boxplot(df)

    for median in boxes['medians']:
        y = median.get_ydata()[0]  # Get the y-coordinate of the median
        plt.text(median.get_xdata()[0], y + 0.2, f'{y:.2f}', ha='center')  # Adjust the label position as needed


    # Add labels, title, and legend
    plt.xlabel("Number of Include Paths")
    plt.xticks([1,2,3,4], ["One", "Ten", "Hundred", "Thousand"])
    plt.ylabel("Time (ms)")
    plt.title("Excessive Include Paths")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    args = sys.argv[1:]
    
    # Just expect the first non-script arg to be a log dir
    main(args[0])

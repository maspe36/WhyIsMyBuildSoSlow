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

    # Add labels, title, and legend
    tick_names = ["1", "10", "100", "1000"]

    plt.xlabel("Include Paths", fontsize=24)
    plt.xticks([1,2,3,4], tick_names, fontsize=18)
    plt.yticks(fontsize=18)
    plt.ylabel("Time (ms)", fontsize=24)
    plt.title("Excessive Include Paths", fontsize=36)

    # medians = [f"{median.get_ydata()[0]:.0f} ms" for median in boxes['medians']]

    # legend_entries = [f"{label} (Median: {median})" for label, median in zip(tick_names, medians)]
    # plt.legend(legend_entries, fontsize=18)

    for i, median_line in enumerate(boxes['medians']):
        # Get x-coordinate of the median line
        x = median_line.get_xdata()[0]

        # Get y-coordinate of the median line, which is also the value we want to display :)
        y = median_line.get_ydata()[0]
        plt.text(x + 0.22, y + 0.2, f"{y:.0f} ms", ha='center', va='bottom', fontsize=18)


    sample_counts = [len(group) for group in df]
    new_labels = [f"{label} Paths (n={count + 1})" for label, count in zip(tick_names, sample_counts)]
    plt.xticks(range(1, len(tick_names) + 1), new_labels)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    args = sys.argv[1:]
    
    # Just expect the first non-script arg to be a log dir
    main(args[0])

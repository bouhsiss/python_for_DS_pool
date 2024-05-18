from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def main():
    population_df = load("population_total.csv")
    try:
        # define the countries to filter
        countries_to_filter = ["Morocco", "Afghanistan", "France"]
        filtered_population_df = population_df[
            population_df["country"].isin(countries_to_filter)
        ]

        # set the country column as the index and transpose the dataframe
        filtered_population_df.set_index("country", inplace=True)
        transposed_filtered_population_df = filtered_population_df.T
    
        # replace the K, M, B suffixes with the corresponding values
        # and convert the values to integers
        for country in countries_to_filter:
            transposed_filtered_population_df[country] = transposed_filtered_population_df[country].replace({"K": "*1e3", "M": "*1e6", "B": "*1e9"}, regex=True).apply(pd.eval).astype(int)
        # plot the data
        transposed_filtered_population_df.plot(color=["blue", "green", "red"])
        # set the y-axis labels
        max_population = transposed_filtered_population_df.max().max()
        y_ticks_count = int(max_population/1e7) + 1
        y_ticks = [i * 1e7 for i in range(y_ticks_count)]
        y_ticks_labels = ["{:,.0f}M".format(tick/1e6) for tick in y_ticks]
        plt.yticks(y_ticks, y_ticks_labels)
        plt.show()

    except KeyError as e:
        print("Key not found: {0}".format(e))


if __name__ == "__main__":
    main()

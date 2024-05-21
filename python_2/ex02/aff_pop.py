from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def generate_colors(n):
    """
    Generate n colors for the plot.

    Parameters:
    n (int): The number of colors to generate.

    Returns:
    list: The list of colors.
    """
    try:
        assert isinstance(n, int) and n > 0, "n should be a positive integer."
        # generate n colors
        colors = plt.cm.viridis(range(0, 256, int(256/n)))
        return colors

    except AssertionError as e:
        print("AssertionError: {0}".format(e))
    except Exception as e:
        print("an error has occured: {0}".format(e))


def plot_population(population_df, countries_to_filter):
    """
    Load the total population dataset and plot a line plot of the total \
population for the given countries.

    Parameters:
    population_df (DataFrame): The total population dataset.
    countries_to_filter (list): The list of countries to filter the data for.

    Returns:
    None
    """
    try:
        assert isinstance(
            population_df, pd.DataFrame
        ), "population_df should be a pandas DataFrame"

        assert (
            isinstance(countries_to_filter, list) and
            len(countries_to_filter) > 1
        ), "countries_to_filter should be a list with at least 2 countries."

        # generate colors depending on the number of countries to filter
        countries_to_filter_colors = generate_colors(len(countries_to_filter))

        # filter the data for the given countries
        filtered_population_df = population_df[
            population_df["country"].isin(countries_to_filter)
        ]

        # set the country column as the index and transpose the dataframe
        filtered_population_df.set_index("country", inplace=True)
        transposed_filtered_population_df = filtered_population_df.T
        transposed_filtered_population_df.columns.name = None
        transposed_filtered_population_df = (
            transposed_filtered_population_df.loc['1800':'2050']
        )

        # replace the K, M, B suffixes with the corresponding values
        # and convert the values to integers
        for country in countries_to_filter:
            transposed_filtered_population_df[country] = (
                transposed_filtered_population_df[country]
                .replace({"K": "*1e3", "M": "*1e6", "B": "*1e9"}, regex=True)
                .apply(pd.eval)
                .astype(int)
            )

        # plot the data
        transposed_filtered_population_df.plot(
            color=countries_to_filter_colors
        )

        # set the y-axis labels
        max_population = transposed_filtered_population_df.max().max()
        y_ticks_count = int(max_population/1e7) + 1
        y_ticks = [i * 1e7 for i in range(y_ticks_count)]
        y_ticks_labels = ["{:,.0f}M".format(tick/1e6) for tick in y_ticks]
        plt.yticks(y_ticks, y_ticks_labels)

        plt.legend(loc="lower right")
        plt.ylabel("Population")
        plt.xlabel("Year")
        plt.title("Population Projections")
        plt.show()

    except KeyError as e:
        print("Key not found: {0}".format(e))
    except Exception as e:
        print("an error has occured: {0}".format(e))


def main():
    """
    A dynamic program that loads the total population dataset and plot the \
total population for the specified countries from the years 1800 to 2050.
    """
    # load the total population dataset
    population_df = load("population_total.csv")
    if population_df is not None:
        plot_population(
            population_df,
            ["Morocco", "Algeria"]
        )


if __name__ == "__main__":
    main()

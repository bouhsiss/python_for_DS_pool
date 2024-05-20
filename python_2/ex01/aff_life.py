from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load the life expectancy dataset and plot the life expectancy projections \
for Morocco.

    Load the life expectancy dataset and filter the data for Morocco.
    Plot the life expectancy in a line plot:
        x-axis: year,
        y-axis: life expectancy,
        title: "Morocco Life expectancy Projections"
    """
    life_expectancy_df = load("life_expectancy_years.csv")

    if life_expectancy_df is not None:
        try:
            morocco_row = life_expectancy_df.loc[
                life_expectancy_df["country"] == "Morocco"
            ]
            if morocco_row.empty:
                raise KeyError("no data for Morocco found.")
            morocco_data = morocco_row.drop("country", axis=1).T
            morocco_data.plot(
                legend=False,
                xlabel="Year",
                ylabel="Life excpectancy",
                title="Morocco Life expectancy Projections"
            )
            plt.show()

        except KeyError as e:
            print("Key not found: {0}".format(e))


if __name__ == "__main__":
    main()

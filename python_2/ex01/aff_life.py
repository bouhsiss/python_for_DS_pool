from load_csv import load
import matplotlib.pyplot as plt


def main():
    life_expectancy_df = load("life_expectancy_years.csv")

    if life_expectancy_df is not None:
        try:
            morocco_row = life_expectancy_df.loc[
                life_expectancy_df["country"] == "France"
            ]
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

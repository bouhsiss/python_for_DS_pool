from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def observe_data(income_per_person_gdppercapita_df, life_expectancy_df):
    """
    plot histograms of the income_per_person_gdppercapita_df and \
life_expectancy_df data to observe their distribution.

    Parameters:
        income_per_person_gdppercapita_df (Series): The income per person \
(GDP per Capita) data.
        life_expectancy_df (Series): The life expectancy data.

    Returns:
        None
    """
    # Create figure and subplots for data distribution
    fig, axs = plt.subplots(2)

    # plot histogram of income_per_person_gdppercapita_df_1900 on first subplot
    axs[0].hist(income_per_person_gdppercapita_df, bins=20, color='blue')
    axs[0].set_title('Income per Person (GDP per Capita) in 1900')

    # plot histogram of life_expectancy_df_1900 on second subplot
    axs[1].hist(life_expectancy_df, bins=20, color='green')
    axs[1].set_title('Life Expectancy in 1900')

    # Display the figure with subplots
    plt.tight_layout()
    plt.show()


def main():
    """
    Load the income_per_person_gdppercapita and life_expectancy datasets \
and plot a scatter plot of the data of life expetancy in relation to the \
gross national product of the year 1900 for each country.
    """
    # load the datasets into a dataframe
    income_per_person_gdppercapita_df = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_df = load(
        "life_expectancy_years.csv"
    )

    if (income_per_person_gdppercapita_df is not None and
            life_expectancy_df is not None):
        # filter the data for the year 1900
        income_per_person_gdppercapita_df_1900 = (
            income_per_person_gdppercapita_df["1900"]
        )
        life_expectancy_df_1900 = life_expectancy_df["1900"]

        # plot our data distribution
        # observe_data(
        #     income_per_person_gdppercapita_df_1900, life_expectancy_df_1900
        # )

        # the gdppercapita data is skewed to the right, so we will use the log
        # scale to normalize the distribution of the data
        income_per_person_gdppercapita_df_1900_log = np.log10(
            income_per_person_gdppercapita_df_1900
        )

        plt.scatter(
            income_per_person_gdppercapita_df_1900_log,
            life_expectancy_df_1900
        )

        # define the x-axis ticks and labels for the scatter plot
        # ([2.477, 3, 4] are the log10 of 300, 1000, 10000)
        plt.xticks(ticks=[2.477, 3, 4], labels=["300", "1K", "10K"])
        plt.title("1900")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.show()


if __name__ == "__main__":
    main()

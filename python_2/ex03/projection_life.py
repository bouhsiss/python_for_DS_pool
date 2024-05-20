from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def observe_data(income_per_person_gdppercapita_df, life_expectancy_df):
    # Create a figure and a set of subplots to plot the distribution of our data
    fig, axs = plt.subplots(2)

    # plot histogram of income_per_person_gdppercapita_df_1900 on first subplot
    axs[0].hist(income_per_person_gdppercapita_df, bins=20, color='blue', alpha=0.7)
    axs[0].set_title('Income per Person (GDP per Capita) in 1900')

    # plot histogram of life_expectancy_df_1900 on second subplot
    axs[1].hist(life_expectancy_df, bins=20, color='green', alpha=0.7)
    axs[1].set_title('Life Expectancy in 1900')

    # Display the figure with subplots
    plt.tight_layout()
    plt.show()


def main():
    income_per_person_gdppercapita_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    print(income_per_person_gdppercapita_df.head())
    life_expectancy_df = load("life_expectancy_years.csv")
    if income_per_person_gdppercapita_df is not None and life_expectancy_df is not None:
        income_per_person_gdppercapita_df_1900 = income_per_person_gdppercapita_df["1900"]
        life_expectancy_df_1900 = life_expectancy_df["1900"]

        # plot our data distribution
        #    observe_data(income_per_person_gdppercapita_df_1900, life_expectancy_df_1900)

        # the gdppercapita data is skewed to the right, so we will use the log scale to normalize the distribution of the data
        income_per_person_gdppercapita_df_1900_log = np.log10(income_per_person_gdppercapita_df_1900)


        plt.scatter(income_per_person_gdppercapita_df_1900_log, life_expectancy_df_1900)
        # define the x-axis ticks and labels for the scatter plot ([2.477, 3, 4] are the log10 of 300, 1000, 10000)
        plt.xticks(ticks=[2.477, 3, 4], labels=["300", "1K", "10K"])
        plt.title("1900")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.show()


if __name__ == "__main__":
    main()

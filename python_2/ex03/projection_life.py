from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    income_per_person_gdppercapita_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_df = load("life_expectancy_years.csv")
    if income_per_person_gdppercapita_df is not None and life_expectancy_df is not None:
       income_per_person_gdppercapita_df_1900 = income_per_person_gdppercapita_df["1900"]
       life_expectancy_df_1900 = life_expectancy_df["1900"]
       plt.scatter(income_per_person_gdppercapita_df_1900, life_expectancy_df_1900)
       plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1K", "10K"])
       plt.show()


if __name__ == "__main__":
    main()
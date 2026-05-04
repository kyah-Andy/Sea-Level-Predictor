import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os


def draw_plot():
    # PATH SETUP 
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "epa-sea-level.csv")

    output_dir = os.path.join(current_dir, "docs")
    os.makedirs(output_dir, exist_ok=True)

    # LOAD DATA
    df = pd.read_csv(data_path)

    # CREATE SCATTER PLOT
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # LINE OF BEST FIT (ALL DATA)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = pd.Series(range(df["Year"].min(), 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    ax.plot(x_all, y_all, color="red", label="Best Fit (All Data)")

    # LINE OF BEST FIT (2000+)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = res_2000.slope * x_2000 + res_2000.intercept
    ax.plot(x_2000, y_2000, color="green", label="Best Fit (2000+)")

    # LABELS & TITLE
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # SAVE FILE TO docs/
    output_path = os.path.join(output_dir, "sea_level_plot.png")
    fig.savefig(output_path)

    return fig
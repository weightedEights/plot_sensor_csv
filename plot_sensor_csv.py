import os
import pandas as pd


def main():

    # get data to plot
    dat_list_to_plt = get_dat_to_plot()

    # create pandas df time series
    dat_df = df_from_dat_list(dat_list_to_plt)

    # plot using pandas built-in
    # maybe in future use bokeh


if __name__ == "__main__":
    main()


def get_dat_to_plot():

    dat_list = []

    return dat_list


def df_from_dat_list(dat_list):

    return dat_list
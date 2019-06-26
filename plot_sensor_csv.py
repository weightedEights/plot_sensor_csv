import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as pltstyle


dat_files_to_plot = ["temps_20190626.txt"]


def main():

    # get data to plot
    dat_list_to_plt = get_dat_to_plot(dat_files_to_plot)

    # create pandas df time series
    dat_df = df_from_dat_list(dat_list_to_plt)
    print(dat_df.head())

    # plot using pandas built-in
    # maybe in future use bokeh
    pandas_plot(dat_df)


def get_dat_to_plot(file_list):

    dat_list_paths = []

    for file in file_list:
        dat_list_paths.append(os.path.join("./data", file))

    return dat_list_paths


def df_from_dat_list(dat_list):

    # parse dates and use as index
    dat_df = pd.read_csv(dat_list[0], parse_dates=True, index_col=0)

    return dat_df


def pandas_plot(df):

    plt.interactive(True)
    # pltstyle.use('Solarize_Light2')
    pltstyle.use('fivethirtyeight')
    # pltstyle.use('ggplot')

    # df["Temp_A"].plot(style='r-', linewidth=1.0, label="Top Shelf Temp")
    # df["Temp_B"].plot(style='b-', linewidth=1.0, label="Bottom Shelf Temp")
    ax = df.plot(style=['r-', 'b-'])
    ax.legend(["Top Shelf Temp", "Bottom Shelf Temp"])

    # get index of max value from Temp_A to annotate
    # i_max_val = df.index.get_loc(df["Temp_A"]["2019-06-25 07":"2019-06-25 08"].idxmax())

    # ax.annotate("Sleep system egress,\nurine bottle fill.",
    #             (df.index[i_max_val], df["Temp_A"][i_max_val]),
    #             xytext=(-240, 10),
    #             textcoords='offset points',
    #             arrowprops=dict(arrowstyle='-|>', lw=3, ec='r'))

    # ax.grid(which='major', linestyle='-', linewidth='0.5')
    # ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    plt.title("Overnight Temps, Purple Fish Hut #2")
    plt.ylabel("Temp [$\degree$C]")
    plt.xlabel("Date Time [UTC]")

    plt.show(block=True)


if __name__ == '__main__':
    main()

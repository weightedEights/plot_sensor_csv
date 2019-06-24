

def main():

    with open("./data/temps_20190622.txt", 'r') as fin:
        with open("./data/temps_corrected.txt", 'w') as fout:

            # column headers
            fout.write("Date,Temp\n")

            for line in fin:
                dat_list = line.split(' ')
                dat_date = dat_list[0][0:4] + '-' + dat_list[0][4:6] + '-' + dat_list[0][6:8]
                dat_time = dat_list[0][9:11] + ':' + dat_list[0][11:13] + ':' + dat_list [0][13:15]
                dat_data = dat_list[1][:-1]
                # print("{} {} {}".format(dat_date, dat_time, dat_data))

                # iso8601 date format
                fout.write("{} {},{}\n".format(dat_date, dat_time, dat_data))


if __name__ == "__main__":
    main()

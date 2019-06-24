import os
import pandas


def main():
    with open("./temps_20190623.txt", 'r') as fin:
        with open("./temps_snippet.csv", 'w') as fout:
            for line in fin:
                # convert to excel-friendly time format, "yyyy-mm-dd HH:mm:ss"
                print(line.split(',')[1])
                # fout.write(line[:4] + '-' + line[4:6] + '-' + line[6:8] + ' ' + line[9:11] + ':' + line[11:13] + ':' + line[13:15])
                # fout.write(',')
                # fout.write(line[16:22])
                # fout.write('\n')


if __name__ == "__main__":
    main()

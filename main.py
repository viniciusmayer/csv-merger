import os
import glob
import pandas as pd

dir_name = ''
file_name = ''
if __name__ == '__main__':
    os.chdir(dir_name)
    all_filenames = [i for i in glob.glob(f'*.csv')]
    combined_csv_data = pd.concat([pd.read_csv(f, delimiter=';', encoding='UTF-8') for f in all_filenames])
    combined_csv_data.to_csv(file_name)

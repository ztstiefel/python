import os
import pandas as pd

dir = 'C:\\Users\\<USER>\\<DIRECTORY'

def convert_csv_xlsx():
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            df = pd.read_csv(os.path.join(dir, f))
            xlsx_file = os.path.splitext(f)[0] + '.xlsx'
            xlsx_path = os.path.join(dir, xlsx_file)
            df.to_excel(xlsx_path, index=False)

convert_csv_xlsx()

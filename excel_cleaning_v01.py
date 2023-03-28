import pandas as pd
import os

dir = '<user_dir>' # directory with input files
new_dir = '<user_dir>' # directory where output files should go

def del_rows_and_cols():
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            df = pd.read_excel(file) # open excel file
            df.drop(df.index[range(7)],inplace=True) # delete first 8 rows (index 0-7)
            df.drop(df.columns[2], axis = 1, inplace = True) # drop 3rd column (C)
            df.reset_index(drop=True, inplace=True) # reset row index
            df.columns = df.iloc[0] #set row index 0 = header
            df = df[1:] # remove now unnecessary first row
            df = df.dropna(axis=1,how='all') # drop columns with all NaN values
            df.to_excel(os.path.join(new_dir,os.path.basename(file)),  index=False, header=True) # write out modified file

del_rows_and_cols()

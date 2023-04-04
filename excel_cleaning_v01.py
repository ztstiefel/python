import pandas as pd
import os

dir = 'C:\\Users\\ztsti\\Downloads\\grades' # directory with input files
new_dir = 'C:\\Users\\ztsti\\Downloads\\grades\\cleaned' # directory where output files should go

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

def clean_col_headers():
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            df = pd.read_excel(file) # open excel file
            df.columns = df.columns.str.replace('\n', '-',) # replace newline chars in column titles with dash char
            df.columns = df.columns.str.replace(" ","_") # replace space chars in column titles with underscore char
            df.columns = df.columns.str.replace("/","-") # replace forward slash chars in column titles with dash char
            df.columns = df.columns.str.lower() # set all column titles to lowercase
            df.to_excel(os.path.join(new_dir,os.path.basename(file)),  index=False, header=True) # write out modified file

clean_col_headers()

def data_cleaning():
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            df['average'] = df['average'].str[:-1] # remove the last character in this column. (in this case, a '%' sign)
            df['average'] = df['average'].astype('float64') # convert this column with type 'object' to type 'float64'
            df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x) # remove all whitespace in all rows/cols
            df = df.dropna(axis=1,how='all') # drop columns with all NaN values
            df.replace('X',pd.NA,inplace=True, regex=True) # replace 'X' char with NaN
            df.fillna(0, inplace=True) # replace all NaN values with a 0
            # The following lines are specific to a certain set of files being worked with. Can be modified/removed as needed
            df['col_title'] = df['col_title'].astype('float64') # convert this column with type 'object' to type 'float64'
            df['col_title'] = df['col_title'].astype('float64') # convert this column with type 'object' to type 'float64'
            df['col_title'] = df['col_title'].astype('float64') # convert this column with type 'object' to type 'float64'
            df['col_title'] = df['col_title'].astype('float64') # convert this column with type 'object' to type 'float64'
            df.to_excel(os.path.join(new_dir,os.path.basename(file)),  index=False, header=True) # write out modified file

data_cleaning()

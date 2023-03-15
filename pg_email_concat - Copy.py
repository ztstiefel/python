import pandas as pd

def p01_merge():
    df_p01_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_1', skiprows=9,header=0)
    df_p01_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_1', skiprows=9,header=0)
    df_p01_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_1', skiprows=9,header=0)
    df_p01_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_1', skiprows=9,header=0)
    
    df_p01_cmb = pd.concat([df_p01_aaa,df_p01_bbb,df_p01_ccc,df_p01_ddd], ignore_index=True, sort = True)
    df_p01_cmb.drop('Student Name', axis=1, inplace=True)
    df_p01_cmb_alpha = df_p01_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p01_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p01_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p01_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p01_merged = pd.concat([df_p01_cmb,df_p01_cmb_alpha], ignore_index=True)
    df_p01_merged.to_csv('C:\\YOUR\\ztaaa\\Downloads\\pg_email\\df_p01_cmb_a.csv', index=False, header=True)

p01_merge()

def p02_merge():
    df_p02_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_2', skiprows=9,header=0)
    df_p02_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_2', skiprows=9,header=0)
    df_p02_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_2', skiprows=9,header=0)
    
    df_p02_cmb = pd.concat([df_p02_aaa,df_p02_bbb,df_p02_ccc], ignore_index=True, sort = True)
    df_p02_cmb.drop('Student Name', axis=1, inplace=True)
    df_p02_cmb_alpha = df_p02_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p02_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p02_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p02_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p02_merged = pd.concat([df_p02_cmb,df_p02_cmb_alpha], ignore_index=True)
    df_p02_merged.to_csv('C:\\YOUR\\ztaaa\\Downloads\\pg_email\\df_p02_cmb_a.csv', index=False, header=True)

p02_merge()

def p03_merge():
    df_p03_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_3', skiprows=9,header=0)
    df_p03_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_3', skiprows=9,header=0)
    df_p03_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_3', skiprows=9,header=0)
    df_p03_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_2', skiprows=9,header=0)
    
    df_p03_cmb = pd.concat([df_p03_aaa,df_p03_bbb,df_p03_ccc,df_p03_ddd], ignore_index=True, sort = True)
    df_p03_cmb.drop('Student Name', axis=1, inplace=True)
    df_p03_cmb_alpha = df_p03_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p03_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p03_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p03_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p03_merged = pd.concat([df_p03_cmb,df_p03_cmb_alpha], ignore_index=True)
    df_p03_merged.to_csv('C:\\YOUR\\ztaaa\\Downloads\\pg_email\\df_p03_cmb_a.csv', index=False, header=True)

p03_merge()

def p04_merge():
    df_p04_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_4', skiprows=9,header=0)
    df_p04_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_4', skiprows=9,header=0)
    df_p04_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_4', skiprows=9,header=0)
    df_p04_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_3', skiprows=9,header=0)
    
    df_p04_cmb = pd.concat([df_p04_aaa,df_p04_bbb,df_p04_ccc,df_p04_ddd], ignore_index=True, sort = True)
    df_p04_cmb.drop('Student Name', axis=1, inplace=True)
    df_p04_cmb_alpha = df_p04_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p04_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p04_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p04_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p04_merged = pd.concat([df_p04_cmb,df_p04_cmb_alpha], ignore_index=True)
    df_p04_merged.to_csv('C:\\YOUR\\FILE\\PATH\\HERE\\df_p04_cmb_a.csv', index=False, header=True)

p04_merge()

def p05_merge():
    df_p05_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_5', skiprows=9,header=0)
    df_p05_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_4', skiprows=9,header=0)
    
    df_p05_cmb = pd.concat([df_p05_aaa,df_p05_ddd], ignore_index=True, sort = True)
    df_p05_cmb.drop('Student Name', axis=1, inplace=True)
    df_p05_cmb_alpha = df_p05_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p05_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p05_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p05_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p05_merged = pd.concat([df_p05_cmb,df_p05_cmb_alpha], ignore_index=True)
    df_p05_merged.to_csv('C:\\YOUR\\FILE\\PATH\\HERE\\df_p05_cmb_a.csv', index=False, header=True)

p05_merge()

def p07_merge():
    df_p01_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_5', skiprows=9,header=0)
    df_p01_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_6', skiprows=9,header=0)
    df_p01_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_6', skiprows=9,header=0)
    
    df_p07_cmb = pd.concat([df_p01_bbb,df_p01_ccc,df_p01_ddd], ignore_index=True, sort = True)
    df_p07_cmb.drop('Student Name', axis=1, inplace=True)
    df_p07_cmb_alpha = df_p07_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p07_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p07_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p07_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p07_merged = pd.concat([df_p07_cmb,df_p07_cmb_alpha], ignore_index=True)
    df_p07_merged.to_csv('C:\\YOUR\\FILE\\PATH\\HERE\\df_p07_cmb_a.csv', index=False, header=True)

p07_merge()

def p08_merge():
    df_p08_aaa = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (2).xlsx', 
        sheet_name='Page1_7', skiprows=9,header=0)
    df_p08_bbb = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (5).xlsx', 
        sheet_name='Page1_6', skiprows=9,header=0)
    df_p08_ccc = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (10).xlsx', 
        sheet_name='Page1_7', skiprows=9,header=0)
    df_p08_ddd = pd.read_excel(
        'C:\\YOUR\\FILE\\PATH\\GOES\\HERE - My Guardian Email Verification (3).xlsx', 
        sheet_name='Page1_7', skiprows=9,header=0)
    
    df_p08_cmb = pd.concat([df_p08_aaa,df_p08_bbb,df_p08_ccc,df_p08_ddd], ignore_index=True, sort = True)
    df_p08_cmb.drop('Student Name', axis=1, inplace=True)
    df_p08_cmb_alpha = df_p08_cmb[['Name First-Middle-Last - Guardian.1','Email - Guardian.1']].copy()
    df_p08_cmb.drop(columns=['Name First-Middle-Last - Guardian.1','Email - Guardian.1'], inplace=True)
    df_p08_cmb.rename(columns={'Name First-Middle-Last - Guardian': 'Full Name', 'Email - Guardian': 'Email'}, inplace=True)
    df_p08_cmb_alpha.rename(columns={'Name First-Middle-Last - Guardian.1': 'Full Name', 'Email - Guardian.1': 'Email'}, inplace=True)
    df_p08_merged = pd.concat([df_p08_cmb,df_p08_cmb_alpha], ignore_index=True)
    df_p08_merged.to_csv('C:\\YOUR\\FILE\\PATH\\HERE\\df_p08_cmb_a.csv', index=False, header=True)

p08_merge()
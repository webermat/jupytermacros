import numpy as np
import pandas as pd

def convert_exposure(value):
    #exposure in float, listed as string of two numbers a/b
    try:
        list_string=value.split('/')
        if (len(list_string)==1):
            return float(value)
        else:
            return float(list_string[0])/float(list_string[1])
    except AttributeError:
        return np.NaN

def convert_mm(value):
    #length in mm transformed to float
    try:
        new_value = value.replace(' mm','')
        return float(new_value)    
    except AttributeError:
        return np.NaN

def shorten_sourceFile(value):
    new_value=value.replace('/Volumes/INTENSO/Backups.backupdb/Matthias’s MacBook Pro/Latest/Macintosh HD/Users/matthiasweber/Pictures/','')
    return new_value

def run_analysis():
    dataframe_list=[]

    for input in range(2006,2019):
        df=pd.read_csv("/Users/matthiasweber/outputEXIFcsvs/PhotoEXIFDataDayType_%s.csv"%(str(input)))
    #push back year index as additional list 
    #print(df.columns,df.head)
    #print(df.dtypes)
        df.replace('/Volumes/INTENSO/Backups.backupdb/Matthias', '')
        df['SourceFile']=df['SourceFile'].apply(shorten_sourceFile)    
        df['FocalLength']=df['FocalLength'].apply(convert_mm) 
    #print('before',df['ExposureTime'])
    #df['ExposureTime']=pd.to_numeric(df['ExposureTime'],errors='coerce')
    #print(df['ExposureTime'])
        df['ExposureTime']=df['ExposureTime'].apply(convert_exposure)
        df['year']=int(input)
        df.rename(columns={'DateTimeOriginal':'Date','FocalLength':'FocalLength in mm'},inplace=True) 
    #print('did something happen')

    #print(df.dtypes)
    #print('final loop')
        dataframe_list.append(df)


        
    for data in dataframe_list:
        print(df.head)

run_analysis()

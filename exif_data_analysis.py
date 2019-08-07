import numpy as np
import pandas as pd

def run_analysis():

    file_list=[]

    for input in range(2006,2019):
        file_list.append(pd.read_csv("/Users/matthiasweber/outputEXIFcsvs/PhotoEXIFDataDayType_%s.csv"%(str(input))))
    

    print (file_list[0])


run_analysis()

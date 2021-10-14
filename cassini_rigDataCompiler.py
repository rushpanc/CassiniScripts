# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:19:44 2021

@author: rushi.panchal
"""

import pandas as pd
import glob 
import os 

#use glob to get all the csv files in the folder 
# pathToParentFolder = r"C:\Users\rushi.panchal\Documents\Cassini\Fluidics_Testing\Rig1"
pathToParentFolder = r"M:\Yiran\Cassini\Fluidics_testing_rig_syringe\Rig1\Tecan_run01"
##empty dataframe --> will be overwritten in loop
df = pd.DataFrame(list())
##empty csv to write over 
# df.to_csv('CompiledData.csv')
#find csv files 
# csv_files_to_process=glob.glob(os.path.join(pathToParentFolder, "Tricon*//*//data.csv"))
csv_files_to_process=glob.iglob(os.path.join(pathToParentFolder, "*/data.csv"))
print(csv_files_to_process)

pathToOutput = r"C:\Users\rushi.panchal\Documents\Cassini\Fluidics_Testing"

# loop over the list of csv files
for f in csv_files_to_process:
    
    # read the csv file
    df_n = pd.read_csv(f)
    
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
    rigNameText = os.path.normpath(pathToParentFolder)
    df_n.insert(0, 'RigName', df_n.shape[0]*[os.path.basename(rigNameText)])
    df_n.insert(1, 'Experiment Name', f.split("\\")[-2])
    
    df = df.append(df_n)
    
#convert df to csv 
df.to_csv(os.path.join(pathToParentFolder, 'CompiledData.csv'),index=False)

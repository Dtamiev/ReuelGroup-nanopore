import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline
print('***Initialized***')
seqAlignment=pd.read_csv('simple_aligner_barcode_compact_quick-v1 (1).csv') #EPI2ME output
print('***Data loaded***')

#create new dataFrame
hits=pd.DataFrame(columns=seqAlignment.columns)

#select from DataFrame 1
cond=seqAlignment.end>1
rows=seqAlignment.loc[cond,:] #should work as long as the data in not bigger than you memory
hits=hits.append(rows, ignore_index=True)
hits.to_csv('hits.csv')

print('***Hits indexing saved***')

#extract individual sequences from text files using hits.csv

print('*** END ***')
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
#hits.to_csv('hits.csv')
print('***Hits indexing saved***')

#TODO: extract individual sequences from text files using hits.csv

#input (working directory)
wdir=r'F:\NanoporeOut\OneDrive - Iowa State University\1593\1593\168\20210223_1459_X1_FAO67831_535ea5c3\fastq_pass'

#saving dir
sdir=r'F:\NanoporeOut\OneDrive - Iowa State University\alignment\out'

#while loop over the csv
for i in hits.index:

    # 1. Get file name
    fullName=hits['filename'][i]
    read_id=hits['read_id'][i]
    #read_id="21439ee0-39c6-4c44-aec5-a72bb8f1ac41" ###fake name from the Line 5

    #2. parse the file name to contain the fastq file name
    fnameParsed=fullName.split('_',8)
    fname=wdir + "\\" + fnameParsed[8]
    fastqname=fnameParsed[8]

    #3 Open the fastq file
    thisFastq=open(fname)
    content=thisFastq.readlines()

    #4 Loop through each line of input
    for id, lines in enumerate(content):

        #find the line with correct id
        x=lines.find(read_id)

        #write 3 lines to new fastq file.
        if x > 0:

            fileId=read_id
            outname=sdir + "\\" + fileId + "_" + fastqname #change this to accomodate the save directory

            outFastqFile=open(outname,"w+")

            outFastqFile.write(content[id])
            outFastqFile.write(content[id+1])
            outFastqFile.write(content[id+2])
            outFastqFile.write(content[id + 3])

            outFastqFile.close()
    print(i, "Sequence")


print('*** END ***')
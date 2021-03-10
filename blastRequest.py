import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import pandas as pd
import numpy as np

print("*** Initialization Complete ***")

q2 = SeqIO.read("q2.fastq", format="fastq")

flRef = SeqIO.read("fullConstruct.fasta", format="fasta")
cRef = SeqIO.read("BS168.fasta", format="fasta")

q1 = SeqIO.read("q1.fastq", format="fastq")
alignments = pairwise2.align.globalxx(cRef.seq, q1.seq)

df=pd.DataFrame(alignments)

print(max(df.score))
for i, val in enumerate(alignments):

    print(alignments[i].score)


#result=Bio.Blast.NCBIWWW.qblast("blastn", "nt", flReference.seq)

print("*** END ***")
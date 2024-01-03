from os import listdir
from PyPDF2 import PdfMerger

mypath="C:/Users/praty/OneDrive/Desktop/merge"

ndir = [mypath+"/"+f for f in listdir(mypath)]

merger = PdfMerger()

for pdf in ndir:
    print(pdf)
    merger.append(pdf)

merger.write(mypath+"/"+"no_dup_merge.pdf")
merger.close()
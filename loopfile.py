## wrtre python codes that will loop through a file

import os

#creae a cvariable for the path

path='Users/clementayeni/Documents:'
ext=('txt','exe')
collectfile=[]
#write  you code that will loop through and collect all the files

for file in path:
    if file.endswith(ext):
        print(file)
        collectfile.append(file)
    else:
        continue    
        
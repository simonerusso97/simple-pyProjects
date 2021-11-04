#tempo 1:30:00

#how do we represent a dataset in Python?
#-list
#We can use the Panda librariy in which datasets are object of class DataFrame

#naive approce
#....


#using Pandas library, Matplotlib - Numpy (da installare)

#you can install any library using a number of tool like pip, pip3...

import pandas as pd
sale_stats = {
    'District' : ['Provenence', 'Normadie', 'Guascogne'],
    'Roquefort_sales' : [12300, 24980, 34870]
}

dataset_2 = pd.DataFrame(sale_stats)
print(dataset_2, "\n")
dataset_2.set_index('District')
print(dataset_2, "\n")
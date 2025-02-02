# Christy's work:

import numpy as np
import pandas as pd

df = pd.read_csv("speeddating.csv", low_memory=False)
df = df.applymap(lambda x: np.nan if x == '?' else x)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df.isnull().any())

print(df.loc[2])

#--------------------------

# Haleigh's edits/cleaning:

# remove NAs
df2 = df.dropna()
df2.shape #only have 1048 rows left - should we use this one?
df.shape #compared to 8378 rows when there are NAs
df2.dtypes #objects and integers (binned integers are objects)

#will continue with df2 but can just copy/paste with df if we decide to use that one instead

#I think it's okay to keep some of the numeric data binned since that might help to find patterns between variables later, but I can be convinced otherwise. What do you all think?

#remove single quotes from race, race_o cols, and field cols
cols_to_check = ['race', 'race_o', 'field']
df2[cols_to_check] = df2[cols_to_check].replace({'\'':''}, regex=True)
df2['race'] #check
df2['race_o'] #check
df2['field'] #check

#lowercase everything (including field since they weren't all upper or lowercase in field)
df2['field'] = df2['field'].apply(lambda x: x.lower()) #I couldn't get this to work using cols_to_check for some reason. also tried str.lower but it didn't work, so did it individually instead since only three cols
df2['race'] = df2['race'].apply(lambda x: x.lower())
df2['race_o'] = df2['race_o'].apply(lambda x: x.lower())
df2['race'] #check
df2['race_o'] #check
df2['field'] #check

#check that all ? were removed/detected as NA -- if use df instead, make sure to convert all ? to NA 
"?" in df2 #false, so they were removed 

# export to csv
df2.to_csv('clean_speeddating.csv')



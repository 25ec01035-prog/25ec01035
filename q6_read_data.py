import pandas as pd
df = pd.read_csv("id-vds .csv")
print ("column names:")
print (df.columns)
print ("\nshape:")
print (df.shape)
print ("\nstatistical summary:")
print(df.describe())

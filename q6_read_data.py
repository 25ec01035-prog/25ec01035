import pandas as pd
df = pd.read_csv("id-vds.csv")
print ("column names:")
print (df.columns)
print ("\n shape:")
print (df.shape)
print ("\n statistical summary:")
print(df.describe())

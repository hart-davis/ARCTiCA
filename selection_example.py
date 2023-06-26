# to import the appropriate modules
import pandas as pd
import numpy as np

# path + name of dataset
fname = 'ArcTiCA.txt'

# load the data
df = pd.read_csv(fname,sep="\t")

# to select an individual site
ind = np.where(df[’site’]=="Beaufort_A")[0]
# to select all sites from an individual source, in this case WHOI
ind = np.where(df[’source_id’]==27)[0]
# to select an individual constituent, in this case only M2
ind = np.where(df[’cons’]=="M2")[0]
# to select an individual instrument type, in this case OBP
ind = np.where(df[’instrument’]=="OBP")[0]

# applying the indexing / selection
df = df.iloc[ind].reset_index(drop=True)

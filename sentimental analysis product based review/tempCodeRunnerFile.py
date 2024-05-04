plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import warnings
warnings.filterwarnings('ignore') # Hides warning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore",category=UserWarning)
sns.set_style("whitegrid") # Plotting style
np.random.seed(42) # seeding random number generator

df = pd.read_csv('C:\\Users\\shiva\\Desktop\\sentimental analysis product based review\\amazon.csv')

df.head()
data = df.copy()
data.describe()
data.info()
data["asins"].unique()
asins_unique = len(data["asins"].unique())
print("Number of Unique ASINs: " + str(asins_unique))
data["reviews.numHelpful"].hist(figsize=(20,5))
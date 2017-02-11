###import
import json
import pandas as pd

# json_data=open('train.json').read()
# data = json.loads(json_data)

#import data 
#separate price from the dataset
#display data 
data = pd.read_json('train.json')
data.drop(['price'],axis = 1, inplace = True)
print 'price is separated from data'

###display data 
from IPython.display import display
display(data.describe())
###

###print sample
# indices = [86,150,95]
# samples = pd.DataFrame(data.loc[indices], columns = data.keys()).reset_index(drop = True)

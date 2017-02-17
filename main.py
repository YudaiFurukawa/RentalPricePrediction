###import
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
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

###display data stats
from IPython.display import display
display(data.describe())

###drop features
#features not needed
del data['photos'], data['manager_id'], data['listing_id'], data['description'],data['building_id'], data['created']
#features maybe needed
del data['features'], data['display_address'],data['street_address'],data['interest_level']
print data.keys()

###reset index
data = data.reset_index(drop=True)

###pick some samples 
#print samples
indices = [30,150,95]
# Create a DataFrame of the chosen samples
samples = pd.DataFrame(data.loc[indices], columns = data.keys())
print "Chosen samples:"#from matplotlib import rcParams, rcParamsDefault, get_backend
#
display(samples)

#from matplotlib import rcParams, rcParamsDefault, get_backend
from pandas.tools.plotting import scatter_matrix
scatter_matrix(data, alpha = 0.3, figsize = (6,6), diagonal = 'kde');
plt.show()
###


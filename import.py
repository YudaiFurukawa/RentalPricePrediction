###import
import json
import pandas as pd

# json_data=open('train.json').read()
# data = json.loads(json_data)
# print data

data = pd.read_json('train.json')
###

###display data 
from IPython.display import display
display(data.describe())
###
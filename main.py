import pandas as pd
import json
from datetime import datetime, timedelta
import features

# load the data in the dataset
df = pd.read_csv("data/data.csv")
contacts = df['contracts']

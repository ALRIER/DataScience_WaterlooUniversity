#!pip3 install pandas_profiling
#!pip3 install matplotlib
#!pip3 install mkdocs
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas_profiling
from pandas_profiling import ProfileReport
canada = pd.read_csv('/home/alrier/Waterloo_week3/Canada_visitors.csv', index_col=0)
canada.head()
print(canada.info)
print(canada.describe())
from numpy import nan as NA  
#can=canada.dropna(how='all')
can=canada.fillna(0)
can
can.shape
data= can.sample(20)
data.shape
report = can.profile_report(sort=None, html={'style':{'full_width':True}})
report
report.to_file(output_file="miReporte.html")

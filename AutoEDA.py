# Load the Data
import pandas as pd

df = pd.read_csv(r"C:\Users\manoj\OneDrive\Desktop\360DigiTMG\Project\Money_Laundering_Dataset.csv")

# Auto EDA
# ---------
# Sweetviz
# Autoviz
# Dtale
# Pandas Profiling
# Dataprep


# Sweetviz
###########
#pip install sweetviz
import sweetviz as sv

s = sv.analyze(df)
s.show_html()


# Autoviz
###########
# pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"C:\Users\manoj\OneDrive\Desktop\360DigiTMG\Project\Money_Laundering_Dataset.csv", chart_format = 'html')

import os
os.getcwd()

# If the dependent variable is known:
a = av.AutoViz(r"C:\Users\manoj\OneDrive\Desktop\360DigiTMG\Project\Money_Laundering_Dataset.csv", depVar = 'isFraud') # depVar - target variable in your dataset



# D-Tale
########

# pip install dtale   # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale

d = dtale.show(df)
d.open_browser()


# Pandas Profiling
###################

# pip install pandas_profiling
from pandas_profiling import ProfileReport 

p = ProfileReport(df)
p
p.to_file("output.html")

import os
os.getcwd()

# Dataprep
##########

# pip install dataprep
from dataprep.eda import create_report

report = create_report(df, title = 'My Report')

report.show_browser()




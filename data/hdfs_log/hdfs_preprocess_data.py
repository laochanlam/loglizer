import pandas as pd

data = pd.read_csv("label.csv")
data = data.replace('Normal', 0)
data = data.replace('Anomaly', 1)


data['Label'].to_csv('label_hdfs.txt', header=None, index=None, sep=' ')
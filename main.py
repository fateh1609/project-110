import csv
import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

mean = statistics.mean(data)
print("mean =",mean)
std_deviation = statistics.stdev(data)
print("standard deviation =",std_deviation)

dataset = []
for i in range(0,1000):
  random_index = random.randint(0, len(data))
  value = data[random_index]
  dataset.append(value)
means = statistics.mean(dataset)
standard_deviation = statistics.stdev(dataset)
print("mean of 1000 values:",means)
print("standard deviation of 1000 values:",standard_deviation)

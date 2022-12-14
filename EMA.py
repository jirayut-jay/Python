import pandas as pd
import matplotlib.pyplot as plt

# load data into a pandas dataframe
df = pd.read_csv('data.csv')

# calculate the EMA values for the data
ema = df.ewm(span=10).mean()

# create a line chart that shows the EMA values over time
plt.plot(ema)

# add labels and a title to the chart
plt.xlabel('Time')
plt.ylabel('EMA Value')
plt.title('EMA Tool Viewer')

# display the chart
plt.show()
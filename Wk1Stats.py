import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from statistics import variance, stdev
from scipy import stats

speed = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
print("Mean:", np.mean(speed))
print("Median:", np.median(speed))
print("Mode:", stats.mode(speed).mode)

#outliers and visualisation
delivery_times = [12, 15, 14, 16, 15, 14, 13, 14, 120]
plt.boxplot(delivery_times)
plt.show()

#Question: why does the outlier affect the mean more than the median?
#The outlier affects the mean more than the median because the mean is calculated by summing all the values and dividing by the number of values. When there is an outlier, it can significantly increase or decrease the total sum, which in turn affects the mean. While the median only focuses on the middle value of the dataset, it is less sensitive to extreme values. Therefore, the median remains relatively stable even in the presence of outliers, while the mean can be skewed by them.

#Variance and Standard Deviation

game_points=[35, 56,43, 59, 63,79,35,41,64,43,93,60,77,24,82]
print("Variance: ",variance(game_points))
print("Standard Deviation: ",stdev(game_points))

#Percentiles and Quartiles
ages=[5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 32, 2, 8, 6, 25, 36, 27, 61, 31]
print(np.percentile(ages, [25, 50, 75, 90]))
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

#IQR Outlier Detection Challange 
transactions= [25, 30, 18, 27, 29, 24, 31, 22, 4500] 

#Correlation
hours_studied=[1,2,3,4,5,6,7]
exam_scores=[45,50,58,62,70,81,90]
print(np.corrcoef(hours_studied, exam_scores))

#Normal Distribution
x=np.random.normal(50, 10, 10000)
plt.hist(x,bins=50)
plt.show()

#Hypothesis Testing
xbar=900
mu0=1000
s=12.5
n=30
t=(xbar-mu0)/(s/np.sqrt(n))
print("t-statistic:", t)

#Type I and Type II Errors
#Question: Disucss which is worse in cancer detection: False Positive or False Negative?
#In cancer detection, both errors would be serious, but a false negative (Type II error) is generally considered worse than a false positive (Type I error). A false negative means that a person who actually has cancer is incorrectly told that they do not have it, which can lead to delayed treatment and potentially life-threatening consequences. On the other hand, a false positive means that a person who does not have cancer is incorrectly told that they do, which can cause unnecessary stress and additional testing, but it does not pose an immediate threat to their health. Therefore, minimizing false negatives is often prioritized in cancer detection to ensure that cases are identified and treated as early as possible.

#Confusion Matrix and Deepfake Detection
TP, TN, FP, FN=80,170,20,30
accuracy=(TP+TN)/(TP+TN+FP+FN)
print(accuracy)

#Entropy and Information Gain
#Question: Which coin has lower entropy: 50/50 or 90/10? why?
#The coin with a 90/10 distribution has lower entropy compared to the 50/50 coin. Entropy is a measure of uncertainty or randomness in a system. A 50/50 coin flip represents maximum uncertainty because there is an equal chance of landing on either side, leading to higher entropy. In contrast, a 90/10 coin flip is more predictable, as there is a much higher probability of landing on one side (90%) than the other (10%), resulting in lower entropy. Therefore, the 90/10 coin has lower entropy because it is less random and more predictable than the 50/50 coin.

#Synthetic Data Generation
x=np.random.uniform(0,5,250)
plt.hist(x,50)
plt.show()

#Mini Project
#Predict student performance using attendance, study hours and coursework marks.
#1. Explore data
#2. Visualise data
#3. Detect outliers
#4. Calculate correlation
#5. Train a model
#6.Evaluate performance
#Mini Project
#Predict student performance using attendance, study hours and coursework marks.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#1. Explore data
#2. Visualise data
#3. Detect outliers
#4. Calculate correlation
#5. Train a model
#6.Evaluate performance

data = {
    "Attendance": [80, 90, 75, 85, 95],
    "Study_Hours": [5, 7, 4, 6, 8],
    "Coursework_Marks": [70, 85, 65, 80, 90],   
    "Final_Marks": [75, 88, 70, 82, 92]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.info())
print(df.describe())
#Mental note:(these above arecalled EDA - Exploratory Data Analysis)

plt.scatter(df['Attendance'], df['Final_Marks'])
plt.xlabel('Attendance')
plt.ylabel('Final Marks')
plt.title('Relationship between Attendance and Final Marks')
plt.show()
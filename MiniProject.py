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
    "attendance": [80, 90, 75, 85, 95],
    "study_hours": [5, 7, 4, 6, 8],
    "coursework_marks": [70, 85, 65, 80, 90],   
    "FinalMarks": [75, 88, 70, 82, 92]
}

df = pd.DataFrame(data)

print(df)
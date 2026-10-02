import numpy as np
# import pandas as pd
#import matplotlib.pyplot as plt
from scipy import stats

speed = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
print("Mean:", np.mean(speed))
print("Median:", np.median(speed))
print("Mode:", stats.mode(speed).mode)
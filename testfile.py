import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("BankChurners.csv")

data.head()

def get_unique(x: np.ndarray, y: np.ndarray):
    x_set = np.array([x[0, :], ])
    y_set = np.array([y[0]])
    for i in range(len(x)):
        for j in range(len(x_set)):
            if all(x_set[j, :] == x[i, :]):
                break
        else:
            x_set = np.vstack((x_set, x[i, :]))
            y_set = np.vstack((y_set, y[i]))
    return x_set, y_set


bins_number = data["Attrition_Flag"].unique().shape[0]
Le = LabelEncoder()
y = Le.fit_transform(data["Attrition_Flag"].values)
# sns.set(rc={'figure.figsize':(11.7,12)})
plt.figure(figsize=((20, 50)))
figures_numb_in_row = 2
for idx, feature in enumerate(data):
    if(True):
        plt.subplot(data.shape[1] // figures_numb_in_row + (0 if(data.shape[1] % figures_numb_in_row == 0) else 1),
                    figures_numb_in_row, idx + 1)
        sns.histplot(x=feature, data=data, color="blue", hue="Attrition_Flag")

x = data.drop(["Attrition_Flag"], axis=1).values[0: 1000, :]
trash_features = ["CLIENTNUM",
                 "Customer_Age",
                 "Gender",
                 "Dependent_count",
                 ""]
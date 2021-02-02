import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from math import sqrt
import statistics
#
import seaborn as sea
import matplotlib as mpl
import csv
#
a=pd.read_csv('BankChurners.csv') 


#identify data types and values (numeric, categorical, ordinal)
print(a.dtypes,"\n\n")  # показує тип
a.columns.to_series().groupby(a.dtypes).groups
numeric_data = ["CLIENTNUM","Customer_Age","Months_on_book","Credit_Limit","Total_Revolving_Bal","Total_Relationship_Count","Contacts_Count_12_mon","Contacts_Count_12_mon",
                     "Avg_Open_To_Buy","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt","Total_Trans_Ct","Total_Ct_Chng_Q4_Q1","Avg_Utilization_Ratio",
                     "Months_Inactive_12_mon", "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
                     "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]
categorical_data = ["Attrition_Flag","Gender","Marital_Status","Card_Category"]
ordinal_data = ["Education_Level","Income_Category","Dependent_count"]
print("Data types and values \n")
print("Numeric - ",numeric_data,"\n")
print("Categorical - ",categorical_data,"\n")
print("Ordinal - ",ordinal_data,"\n")

#visualize data using at least in two different ways: histograms, scatter, pie, box, violin plots, trend line, oth

arr = []
info = a["Income_Category"].value_counts()
for t in range (0,len(info)):
    arr.append(info[t])
plt.figure(figsize=(10, 11))
plt.pie(arr, explode = None, labels = list(info.keys()), shadow = True, startangle = 90)
plt.title("% of salary", y=1.02)
plt.show()



names=["Blue","Gold","Silver"]
i=0;
j=0
e=0
for row in a.values:
   if row[8]=="Blue":
      i=i+1
   elif row[8]=="Gold":
      j=j+1
   else:
      e=e+1
values=[i,j,e]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.grid(True)
plt.bar(names, values)
plt.subplot(132)
plt.grid(True)
plt.scatter(names, values)
plt.subplot(133)
plt.grid(True)
plt.plot(names, values)
plt.suptitle('Card Type')
plt.show()


data = a[["Customer_Age","Income_Category"]]
x = data["Customer_Age"]
y = data["Income_Category"]
plt.scatter(x, y)
plt.show()

 #calculate statistics (mean, standard deviation, correlation matrix, frequency) where possible
mas_mean=[]
for row in a.values:
    mas_mean.append(row[2])

print("Mean is - ",statistics.mean(mas_mean))

mas_months_on_book=[]
for row in a.values:
   mas_months_on_book.append(row[9])
print("Standard Deviation of the Months on book is % s ",(statistics.stdev(mas_months_on_book)))

A=[]
B=[]
C=[]
for colon in a.values:
   A.append(colon[10])
   B.append(colon[11])
   C.append(colon[12])
data = {"A":A,
        "B":B,
        "C":C
        }
df = pd.DataFrame(data,columns=['A','B','C'])
corrMatrix = df.corr()
sea.heatmap(corrMatrix, annot=True)
plt.show()

a_list=[]
for colon in a.values:
   a_list.append(colon[5])

frequencies = {}
for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1
print(frequencies)

#check the correspondence of plots and statistical values
age=[]
nam=[]
for n in range(19,80):
    age.append(n)
    nam.append(0)    
for m in a.values:
   nam[m[2]-19]=nam[m[2]-19]+1      
plt.subplot
plt.grid(True)
plt.plot(age,nam)
plt.show()
print("The graph matches the data mean")


from sklearn import preprocessing # нормалізація даних
import numpy as np 
import pandas as pd

df=pd.read_csv('BankChurners.csv') 
#print(df.head())
#print(df["CLIENTNUM"].isnull())
#to_drop=["Attrition_Flag","Gender","Marital_Status"]
#df.drop(to_drop,inplace=True,axis=1)
#print(a.head())
#print(a.loc[7])
#a.get_dtype_counts()
#a.into()
#a.index()
#print(df.filter(["CLIENTNUM","Customer_Age"]))

# find and filter out missing and incorrect values
#print(df.dropna())###видалити всі рядки з відсутніми значеннями

numeric_data = []
to_drop=[  "Months_Inactive_12_mon","Avg_Utilization_Ratio","Total_Trans_Ct","Total_Amt_Chng_Q4_Q1","Dependent_count","CLIENTNUM","Customer_Age","Months_on_book","Total_Relationship_Count","Contacts_Count_12_mon","Contacts_Count_12_mon",
                      "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
                     "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]
df.drop(to_drop,inplace=True,axis=1)
print(df.describe())
# Total_Revolving_Bal 
# Total_Ct_Chng_Q4_Q1 !!!!!!


test = pd.read_csv('BankChurners.csv', na_values='Unknown')
for i in range(1, 23):
    test[test.columns[i]].fillna(test[test.columns[i]].value_counts().idxmax(), inplace=True)



  
        
        
        
            




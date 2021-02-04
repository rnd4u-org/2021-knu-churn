import pandas
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot as plt

Churners = pandas.read_csv("BankChurners.csv")
print(Churners)

numerical = ["Customer_Age", "Dependent_count", "Months_on_book", "Total_Relationship_Count", "Months_Inactive_12_mon", "Contacts_Count_12_mon", "Credit_Limit", "Total_Revolving_Bal", "Avg_Open_To_Buy", "Total_Amt_Chng_Q4_Q1", "Total_Trans_Amt", "Total_Trans_Ct","Total_Ct_Chng_Q4_Q1", "Avg_Utilization_Ratio", "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"]
nonnumerical = ["Education_Level", "Income_Category", "Attrition_Flag", "Gender", "Marital_Status", "Card_Category"]
print(Churners.isnull().sum())


# Removing Unknown from rows using probabilities based on known data
def find_percantage(cat_name):
    cat_variables = [var for var in Churners[cat_name].to_list() if var != "Unknown" and type(var) != float]
    cat_probability = {}
    cat_len = len(cat_variables)
    for var in cat_variables:
        prob = cat_variables.count(var) / cat_len
        if prob in cat_probability.values():
            continue
        else:
            cat_probability[var] = prob

    return cat_probability


marital = ["Married", "Single", "Divorced"]
education = ["Uneducated", "Graduate", "College", "High School", "Doctorate", "Post-Graduate"]
income = ["Less than $40K", "$40K - $60K", "$80K - $120K", "$60K - $80K", "$120K +"]

marital_probability = list(find_percantage("Marital_Status").values())
education_probability = list(find_percantage("Education_Level").values())
income_probability = list(find_percantage("Income_Category").values())

print(education, " : ", education_probability)
print(income, " : ", income_probability)
print(marital, " : ", marital_probability)

for i, elem in enumerate(Churners["Marital_Status"]):
    if elem == "Unknown" or type(elem) == float:
        arr = np.random.choice(marital, 1, p=marital_probability)
        upd = "".join(arr)
        Churners.at[i, "Marital_Status"] = upd

for i, elem in enumerate(Churners["Income_Category"]):
    if elem == "Unknown" or type(elem) == float:
        arr = np.random.choice(income, 1, p=income_probability)
        upd = "".join(arr)
        Churners.at[i, "Income_Category"] = upd

for i, elem in enumerate(Churners["Education_Level"]):
    if elem == "Unknown" or type(elem) == float:
        arr = np.random.choice(education, 1, p=education_probability)
        upd = "".join(arr)
        Churners.at[i, "Education_Level"] = upd

print(Churners)


# Building plots of numerical data
def show_boxes():
    fig, axs = plt.subplots(8, 2, figsize=(25, 40))
    axes = [item for sublist in axs for item in sublist]
    ax_num = 0

    for num in numerical:
        sns.boxplot(data=Churners, x=Churners[num], ax=axes[ax_num])
        ax_num += 1

    plt.show()


show_boxes()

# Converting non-numeric values to numeric values
for cat in ["Attrition_Flag", "Gender", "Education_Level", "Marital_Status"]:
    enc = LabelEncoder()
    enc.fit(Churners[cat])
    Churners[cat] = enc.transform(Churners[cat])

income_map = {"Less than $40K": 20000,
              "$40K - $60K": 50000,
              "$80K - $120K": 100000,
              "$60K - $80K": 70000,
              "$120K +": 130000}

card_map = {"Blue": 1,
            "Silver": 2,
            "Gold": 3,
            "Platinum": 4}

Churners["Income_Category"] = Churners["Income_Category"].map(income_map)
Churners["Card_Category"] = Churners["Card_Category"].map(card_map)
print(Churners)

# Removing outliers
Churners = Churners[(np.abs(stats.zscore(Churners)) < 3).all(axis=1)]
print(Churners)
show_boxes()

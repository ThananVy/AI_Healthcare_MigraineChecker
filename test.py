import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

#load the format csv
df = pd.read_csv("migraine_symptom_classification.csv", header=0)

#df['type'] = 


print(df.head())
print(df.columns)

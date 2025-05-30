import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib


#load the format csv
df = pd.read_csv("migraine_symptom_classification.csv", header=0)


#df['type'] = 

X = df.drop("Type", axis=1)
y = df["Type"]

#Conver strings to numbers if needed
X =pd.get_dummies(X)

#Split into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

# create the model
model = RandomForestClassifier(n_estimators= 100, random_state= 42)

# train the model
model.fit(X_train,y_train)

# Save the model
joblib.dump(model, 'migraine_model.pkl')

# Make predictions
y_pred = model.predict(X_test)

# Show accuracy and report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("/nClassification Report:/n", classification_report(y_test,y_pred))

# Plot
importances = model.feature_importances_
features = X.columns

# Plot
plt.figure(figsize=(10, 6))
plt.barh(features, importances)
plt.xlabel("Importance")
plt.title("Feature Importance in Migraine Classification")
plt.show()







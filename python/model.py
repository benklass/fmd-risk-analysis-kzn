import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load dataset header with Pandas
df = pd.read_csv("KZN_FMD_dataset.csv")

print(df.head())

# Set target variable
y = df["outbreak_present"]

# Set feature variables
X = df[["road_norm", "dma_norm", "protected_area_norm"]]

# Set data train/test split and random Numpy number generation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Random Forest classifier
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict using model
y_pred = model.predict(X_test)

# Evaluate model accuracy
print(classification_report(y_test, y_pred))

# Evaluate feature importance
importances = model.feature_importances_
features = X.columns

plt.bar(features, importances)
plt.title("Feature Importance")
plt.show()





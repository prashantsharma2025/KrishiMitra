
from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay,
)

# 1. Define file paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "crop dataset" / "Crop_recommendation.csv"
MODEL_DIR = BASE_DIR / "ml"
MODEL_DIR.mkdir(exist_ok=True)

# 2. Load the dataset
df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# 3. Separate inputs and target
features = [
    "N", "P", "K", "temperature",
    "humidity", "ph", "rainfall"
]

X = df[features]
y = df["label"]

# 4. Check for missing values
if X.isnull().any().any() or y.isnull().any():
    raise ValueError("Dataset contains missing values. Clean it first.")

# 5. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 6. Create and train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
)

print("\nTraining model...")
model.fit(X_train, y_train)

# 7. Evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nTest accuracy: {accuracy:.4f}")
print(f"Test accuracy percentage: {accuracy * 100:.2f}%")

print("\nClassification report:")
print(classification_report(y_test, y_pred))

# 8. Save the confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    xticks_rotation=90,
)

plt.tight_layout()
plt.savefig(MODEL_DIR / "confusion_matrix.png")
plt.close()

# 9. Save the trained model
joblib.dump(model, MODEL_DIR / "crop_model.joblib")

print("\nModel saved successfully!")
print("Model path:", MODEL_DIR / "crop_model.joblib")
print("Confusion matrix:", MODEL_DIR / "confusion_matrix.png")
